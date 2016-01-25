#!/usr/bin/env python
# Example 5 : Le o sensor de luz

import rospy
import math
from visualization_msgs.msg import Marker

def LightCallback(l):
	global lMsg
	lMsg = l


def run():
	rospy.init_node('epuck_light', anonymous=True)

	rospy.Subscriber("/light", Marker, LightCallback)

	rate = rospy.Rate(10) # 10hz

	global lMsg

	while not rospy.is_shutdown():
		rate.sleep() 
		print lMsg


if __name__ == '__main__':
	try:
		run()
	except rospy.ROSInterruptException:
		pass