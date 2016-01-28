#!/usr/bin/env python
# Example : Pose with Alvar Track

import rospy
import math

from ar_track_alvar/AlvarMarkers.msg import AlvarMarkers

def AlvarCallback(odom):
	global alvarMsg
	alvarMsg = alvar


def run():
	rospy.init_node('epuck_get_alvar_pose', anonymous=True)

	rospy.Subscriber("/ar_pose_marker", AlvarMarkers, AlvarCallback)

	rate = rospy.Rate(10) # 10hz

	global alvarMsg

	while not rospy.is_shutdown():
		rate.sleep() 
		print alvarMsg


if __name__ == '__main__':
	try:
		run()
	except rospy.ROSInterruptException:
		pass