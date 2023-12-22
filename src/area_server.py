#!/usr/bin/env python

from ros_service_assignment.srv import RectangleAreaService
from ros_service_assignment.srv import RectangleAreaServiceRequest
from ros_service_assignment.srv import RectangleAreaServiceResponse

import rospy

def handle_calc_area(req):
    area1 = req.width * req.height
    print ("Returning Area = %s * %s = %s"%(req.width,req.height,area1))
    return RectangleAreaServiceResponse(area1)

def calc_area_server():
    rospy.init_node('calc_area_server')
    s = rospy.Service('calc_area', RectangleAreaService, handle_calc_area)
    print ("Ready to calculate area.")
    rospy.spin()
    
if __name__ == "__main__":
    calc_area_server()