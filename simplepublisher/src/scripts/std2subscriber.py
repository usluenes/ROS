#!/usr/bin/env python
import rospy
from simplepublisher.msg import Num
from std_msgs.msg import String

"""
information is refreshed, callback function is called to proces
the information.
"""
def callback1(data):
    rospy.loginfo('\n Person %d \n Name: %s \n Lastname: %s \n Age: %d \n Score: %d', data.num, data.first_name, data.last_name, data.age, data.score)

def callback2(data):
    rospy.loginfo('%s', data.data)

def callback3(data):
    rospy.loginfo('%s', data.data)

def stdSubscriber():
    rospy.init_node('Num2SubscriberNode', anonymous = False)
    rospy.Subscriber('numTopic', Num, callback1)
    rospy.Subscriber('publishedTopic', String, callback2)
    rospy.Subscriber('publishedTopic2', String, callback3)

    rospy.spin() # keeps python from exiting until this node is stopped

if __name__ == '__main__':
    stdSubscriber()
