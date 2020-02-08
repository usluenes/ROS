#!/usr/bin/env python

import rospy
import actionlib
from senspublisher.msg import CounterWithDelayAction, CounterWithDelayFeedback, CounterWithDelayResult

# Python class of the action server
class CounterWithDelayActionClass(object):
    # create messages that are used to publish feedback/result
    _feedback = CounterWithDelayFeedback()
    _result = CounterWithDelayResult()

    def __init__(self, name):
        # This will be the name of the action server which clients can use to connect to.
        self._action_name = name

        # Create a simple action server of the newly defined action type and
        # specify the execute callback where the goal will be processed.

        # CounterWithDelayAction type of the action
        # Processes the goal in execute_cb function

        self._as = actionlib.SimpleActionServer(self._action_name,
        CounterWithDelayAction, execute_cb = self.execute_cb, auto_start = False)

        # Start the action server
        self._as.start()
        rospy.loginfo("Action server started...")

    def execute_cb(self, goal):
        # Variable for 1s delay
        r = rospy.Rate(1)

        # Variable to decide the final state of the action server.
        success = True

        # Initiate the feedback value
        self._feedback.counts_elapsed = 0

        # Publish info to the console for the user
        rospy.loginfo('%s action server is counting up to %i with 1s delay between each count'% (self._action_name, goal.num_counts))

        # start executing the action
        for counter_idx in range(0, goal.num_counts):
            # check that preempt has bot been requested by the client
            if self._as.is_preempt_requested():
                rospy.loginfo('%s: Preempted' % self._action_name)
                self._as.set_preempted()
                success = False
                break
            # publish the feedback
            self._feedback.counts_elapsed = counter_idx
            self._as.publish_feedback(self._feedback)
            # Wait for 1s before incrementing the counter
            r.sleep()

        if success:
            self._result.result_message = "Successfully completed counting"
            rospy.loginfo('%s: Succeeded'% self._action_name)
            self._as.set_succeeded(self._result)

if __name__ == '__main__':
    # Initialize a ROS node for this action server
    rospy.init_node('counter_with_delay')

    # Create an instance of the action server here.
    server = CounterWithDelayActionClass(rospy.get_name())
    rospy.spin()
