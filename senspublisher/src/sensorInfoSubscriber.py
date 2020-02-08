#!/usr/bin/env python
import rospy
from senspublisher.msg import SensorInformation

def sensorInfoSubscriber():
    rospy.init_node('sensor_info_subscriberNode', anonymous = False)
    rospy.Subscriber('sensorInfo', SensorInformation, sensorInfoCallback)
    rospy.spin()

def sensorInfoCallback(data):
    rospy.loginfo('Distance: %f', data.sensor_data.range)

if __name__ == '__main__':
    sensorInfoSubscriber()
