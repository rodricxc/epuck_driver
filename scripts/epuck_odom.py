#!/usr/bin/env python
# Example 3 : Le a odometria

import rospy
import math
from nav_msgs.msg import Odometry

def OdomCallback(odom):
	global odomMsg
	odomMsg = odom


def run():
	rospy.init_node('epuck_odom', anonymous=True)

	rospy.Subscriber("/odom", Odometry, OdomCallback)

	rate = rospy.Rate(10) # 10hz

	global odomMsg

	while not rospy.is_shutdown():
		rate.sleep() 
		print odomMsg


if __name__ == '__main__':
	try:
		run()
	except rospy.ROSInterruptException:
		pass