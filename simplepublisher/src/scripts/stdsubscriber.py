#!/usr/bin/env python
import rospy
from simplepublisher.msg import Num
from std_msgs.msg import String

"""
information is refreshed, callback function is called to proces
the information.
"""
def callback(data):
    rospy.loginfo('\n Person %d \n Name: %s \n Lastname: %s \n Age: %d \n Score: %d', data.num, data.first_name, data.last_name, data.age, data.score)

def stdSubscriber():
    rospy.init_node('NumSubscriberNode', anonymous = False)
    rospy.Subscriber('numTopic', Num, callback)
    rospy.spin() # keeps python from exiting until this node is stopped

if __name__ == '__main__':
    stdSubscriber()
