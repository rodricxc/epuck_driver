#!/usr/bin/env python
# Example 10 : Le o sensor de chao

import rospy
import math
from visualization_msgs.msg import Marker

def FloorCallback(f):
	global fMsg
	fMsg = f


def run():
	rospy.init_node('epuck_floor', anonymous=True)

	rospy.Subscriber("/floor", Marker, floorCallback)

	rate = rospy.Rate(10) # 10hz

	global fMsg

	while not rospy.is_shutdown():
		rate.sleep() 
		print fMsg


if __name__ == '__main__':
	try:
		run()
	except rospy.ROSInterruptException:
		pass