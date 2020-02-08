#!/usr/bin/env python

import sys
import rospy
from senspublisher.srv import ConvertMetersToFeet, ConvertMetersToFeetRequest, ConvertMetersToFeetResponse

def meters_to_feet_client(x):
    # First wait for the service to become available.
    rospy.loginfo("Waiting for service...")
    rospy.wait_for_service('meters_to_feet')
    try:
        # Create a service proxy.
        meters_to_feet = rospy.ServiceProxy('meters_to_feet', ConvertMetersToFeet)

        # Call the service here.
        service_response = meters_to_feet(x)

        print("I only got here AFTER the service call was completed!")

        # Return the response to the calling function.
        return service_response

    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":

    # Initialize the client ROS node.
    rospy.init_node("meters_to_feet_client", anonymous = False)

    # The distance to be converted to feet.
    dist_meters = 0.25

    rospy.loginfo("Requesting conversion of %4.2f m to feet"%(dist_meters))

    # Call the service client function.
    service_response = meters_to_feet_client(dist_meters)

    # Process the service response and display log messages accordingly.
    if(not service_response.success):
        rospy.logerr("Conversion unsuccessful! Requested distance in meters should be a positive real number.")
    else:
        rospy.loginfo("%4.2f(m) = %4.2f feet"%(dist_meters, service_response.distance_feet))
        rospy.loginfo("Conversion successful!")
