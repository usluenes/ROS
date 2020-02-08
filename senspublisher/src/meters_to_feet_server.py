#!/usr/bin/env python

import rospy
import numpy as np
from senspublisher.srv import ConvertMetresToFeet, ConvertMetresToFeetRequest, ConvertMetresToFeetResponse

_ConvFactorMetres2Feet = 3.28

# Service callback function.
def process_service_request(req):

    # Instantiate the response message object
    res = ConvertMetresToFeetResponse()

    # Perform sanity check. Allow only positive real numbers
    # Compose the response message accordingly
    if(req.distance_metres < 0):
        res.success = False
        res.distance_feet = -np.Inf # Default error value
    else:
        res.distance_feet = _ConvFactorMetres2Feet * req.distance_metres
        res.success = True
    # Service blocks execution (10sec delay)
    for test_idx in range(0,1):
            rospy.sleep(1)

    return res

def metres_to_feet_server():
    rospy.init_node('metres_to_feet_server', anonymous = False)

    service = rospy.Service('metres_to_feet', ConvertMetresToFeet,
    process_service_request)

    rospy.loginfo('Convert metres to  feet service is available now.')
    rospy.spin()

if __name__ == "__main__":
    metres_to_feet_server()
