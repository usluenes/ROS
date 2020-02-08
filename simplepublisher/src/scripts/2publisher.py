#!/usr/bin/env python

# Simple String Publisher

import rospy
from std_msgs.msg import String
#from simplepublisher.msg import Num


def simplePublisher0():
    rospy.init_node('simplePublisherNode', anonymous = False)
    simple_publisher = rospy.Publisher('publishedTopic', String, queue_size=10)
    topic_info = 'Suppp Bitchezzz !!'

    simple_publisher0 = rospy.Publisher('publishedTopic2', String, queue_size=10)
    topic_info2 = 'hi'
    rate = rospy.Rate(5)

    while not rospy.is_shutdown():
        simple_publisher.publish(topic_info)
        simple_publisher0.publish(topic_info2)
        rate.sleep()
"""

def simplePublisher1():
    simple_publisher0 = rospy.Publisher('publishedTopic0', String, queue_size = 10)
    rospy.init_node('simplePublisherNode', anonymous = False)
    rate0 = rospy.Rate(20)

    topic_info0 = 'Hiiiii!'

    while not rospy.is_shutdown():
        simple_publisher0.publish(topic_info0)
        rate0.sleep()
"""

"""
def simplePublisher2():
    simple_publisher2 = rospy.Publisher('publishedTopic2', String, queue_size = 10)
    rospy.init_node('simplePublisherNode', anonymous = False)
    rate = rospy.Rate(20)

    topic_info2 = 'How you doin?'

    while not rospy.is_shutdown():
        simple_publisher2.publish(topic_info2)
        rate.sleep()
"""
if __name__ == '__main__':
    try:
       simplePublisher0()
       #simplePublisher1()
       #simplePublisher2()
    except rospy.ROSInterruptException:
        pass
