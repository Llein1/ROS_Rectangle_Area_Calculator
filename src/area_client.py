#!/usr/bin/env python

import sys
import rospy
from ros_service_assignment.srv import RectangleAreaService
from ros_service_assignment.srv import RectangleAreaServiceRequest
from ros_service_assignment.srv import RectangleAreaServiceResponse

def calc_area_client(x, y):
    rospy.wait_for_service('calc_area')
    try:
        calc_area = rospy.ServiceProxy('calc_area', RectangleAreaService)
        resp1 = calc_area(x, y)
        return resp1.area
    except rospy.ServiceException(e):
        print ("Service call failed: %s"%e)

def usage():
    return 

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print ("%s [x y]"%sys.argv[0])
        sys.exit(1)
    print ("Requesting Area")
    s = calc_area_client(x, y)
    print ("Area = %s"%(s))