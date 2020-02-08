#!/usr/bin/env python
import rospy
from std_msgs.msg import String

"""
information is refreshed, callback function is called to proces
the information.
"""
def callback(data):
    rospy.loginfo('The  content: %s', data.data)

def simpleSubscriber():
    rospy.init_node('subscriberNode', anonymous = False)
    rospy.Subscriber('publishedTopic', String, callback)
    rospy.spin() # keeps python from exiting until this node is stopped

if __name__ == '__main__':
    simpleSubscriber()
