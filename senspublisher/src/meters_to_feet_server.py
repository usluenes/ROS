#!/usr/bin/env python

import rospy
import numpy as np
from senspublisher.srv import ConvertMetersToFeet, ConvertMetersToFeetRequest, ConvertMetersToFeetResponse

_ConvFactorMeters2Feet = 3.28

# Service callback function.
def process_service_request(req):

    # Instantiate the response message object
    res = ConvertMetersToFeetResponse()

    # Perform sanity check. Allow only positive real numbers
    # Compose the response message accordingly
    if(req.distance_meters < 0):
        res.success = False
        res.distance_feet = -np.Inf # Default error value
    else:
        res.distance_feet = _ConvFactorMeters2Feet * req.distance_meters
        res.success = True
    # Service blocks execution (10sec delay)
    for test_idx in range(0,1):
            rospy.sleep(1)

    return res

def meters_to_feet_server():
    rospy.init_node('meters_to_feet_server', anonymous = False)

    service = rospy.Service('meters_to_feet', ConvertMetersToFeet,
    process_service_request)

    rospy.loginfo('Convert meters to  feet service is available now.')
    rospy.spin()

if __name__ == "__main__":
    meters_to_feet_server()
