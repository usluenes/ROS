#!/usr/bin/env python
# Simple String Publisher

import rospy
from simplepublisher.msg import Num

def stdPublisher():
    std_publisher = rospy.Publisher('numTopic', Num, queue_size=10)
    rospy.init_node('NumPublisherNode', anonymous = False)
    rate = rospy.Rate(30)


    # Create a new Num object and fill its contents
    num_info = Num()

    num_info.num = 1
    num_info.first_name = 'Enes'
    num_info.last_name = 'Uslu'
    num_info.age = 25
    num_info.score = 100

    while not rospy.is_shutdown():
        std_publisher.publish(num_info)
        rate.sleep()
if __name__ == '__main__':
    try:
        stdPublisher()
    except rospy.ROSInterruptException:
        pass
