#!/usr/bin/env python

# Node to publish sensor information topic

import rospy
from senspublisher.msg import SensorInformation
import random

def distSensorData(sensor_type, min_range, max_range):
  if (sensor_type != 0):
    print('Sensor type not supported!')
    return -1
  else:
    if(random.uniform(0.0, 1.0) < 0.95):
      return max_range
    else:
      return random.uniform(min_range, max_range)

def sensorInfoPublisher():
    sensor_publisher = rospy.Publisher('sensorInfo', SensorInformation, queue_size = 10)
    rospy.init_node('sensor_info_publisherNode', anonymous = False) #initialize node
    rate = rospy.Rate(10) # topic publishing frequency

    # Create a new SensorInformation object and fill in its comments
    sensor_info = SensorInformation()

    # Fill in the header information
    sensor_info.sensor_data.header.stamp = rospy.Time.now()
    sensor_info.sensor_data.header.frame_id = 'distance_sensor_frame'

    # Fill in the sensor data information
    sensor_info.sensor_data.radiation_type = sensor_info.sensor_data.ULTRASOUND
    sensor_info.sensor_data.field_of_view = 0.5 # Feild of view of the sensor in rad.
    sensor_info.sensor_data.min_range = 0.02 # minimum distance range of the sensor in m.
    sensor_info.sensor_data.max_range = 2.00 # maximum distance range of the sensor in m

    # Fill in the manufacturer name and part name
    sensor_info.maker_name = 'The Ultrasound Company'
    sensor_info.part_number = 123456

    while not rospy.is_shutdown():
        # Read the sensor data from a simulated sensor
        sensor_info.sensor_data.range = distSensorData(sensor_info.sensor_data.radiation_type,
                sensor_info.sensor_data.min_range, sensor_info.sensor_data.max_range)
        # Publish the sensor information the /sensorInfo topic
        sensor_publisher.publish(sensor_info)
	rospy.loginfo('Topic is published!')
        rate.sleep() #to ensure topic is published at specified frequency

if __name__ == '__main__':
    try:
        sensorInfoPublisher()
    except rospy.ROSInterruptException:
        pass
