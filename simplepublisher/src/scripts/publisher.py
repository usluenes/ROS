#!/usr/bin/env python

# Simple String Publisher

import rospy
from std_msgs.msg import String

def simplePublisher():
    simple_publisher = rospy.Publisher('publishedTopic', String, queue_size=10)
    rospy.init_node('simplePublisherNode', anonymous = False)
    rate = rospy.Rate(30)

    topic_info = 'Suppp Bitchezzz !!'

    while not rospy.is_shutdown():
        simple_publisher.publish(topic_info)
        rate.sleep()

if __name__ == '__main__':
    try:
        simplePublisher()
    except rospy.ROSInterruptException:
        pass
