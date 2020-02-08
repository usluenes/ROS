#! /usr/bin/env python

# Subscribe to the topic that
# publishes sensor information. Then, you will transform the sensor reading from
# the reference frame of the sensor to compute the height of a box based on the
# illustration shown in the assignment document. Then, publish the box height
# on a new message type ONLY if the height of the box is more than 10cm.

# All necessary python imports go here.
import rospy
from senspublisher.msg import SensorInformation, BoxHeightInformation

def sensor_info_callback(data, bhi_pub):

    height_box = data.sensor_data.range

    # Compute the height of the box.
    # Boxes that are detected to be shorter than 10cm are due to sensor noise.
    # Do not publish information about them.
    if height_box > 1.99:
        pass
    else:
        # Declare a message object for publishing the box height information.
        box_height_info = BoxHeightInformation()
        # Update height of box.
        box_height_info.box_height = height_box
        # Publish box height using the publisher argument passed to the callback function.
        bhi_pub.publish(box_height_info)

if __name__ == '__main__':
    # Initialize the ROS node here.
    rospy.init_node('compute_box_height', anonymous = False)

    # Wait for the topic that publishes sensor information to become available - Part1
    rospy.loginfo('Waiting for topic %s to be published...', 'sensorInfo')
    rospy.wait_for_message('sensorInfo', SensorInformation)
    rospy.loginfo('%s topic is now available!', 'sensorInfo')

    # Create the publisher for Part3 here
    sensor_info_publisher = rospy.Publisher('sensorInfo', SensorInformation, queue_size=10)

    # Create the publisher for Part3 here
    bhi_publisher = rospy.Publisher('box_height_info', BoxHeightInformation, queue_size=10)

    # Create the publisher for Part1 here
    rospy.Subscriber('sensorInfo', SensorInformation, sensor_info_callback, bhi_publisher)

    # Prevent this code from exiting until Ctrl+C is pressed.
    rospy.spin()
