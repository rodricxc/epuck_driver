#!/usr/bin/env python
# Example 6 : Le a velocidade do motor

import rospy
import math
from visualization_msgs.msg import Marker

def MotorCallback(m):
	global mMsg
	mMsg = m


def run():
	rospy.init_node('epuck_motor_vel', anonymous=True)

	rospy.Subscriber("/motor_speed", Marker, MotorCallback)

	rate = rospy.Rate(10) # 10hz

	global mMsg

	while not rospy.is_shutdown():
		rate.sleep() 
		print mMsg


if __name__ == '__main__':
	try:
		run()
	except rospy.ROSInterruptException:
		pass