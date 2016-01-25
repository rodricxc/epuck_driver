#!/usr/bin/env python
# Example 2 : Le os dados do acelerometro

import rospy
import math
from sensor_msgs.msg import Imu

def AccCallback(acc):
	global accMsg
	accMsg = acc


def run():
	rospy.init_node('epuck_velocity', anonymous=True)

	rospy.Subscriber("/accel", Imu, AccCallback)

	rate = rospy.Rate(10) # 10hz

	global accMsg

	while not rospy.is_shutdown():
		rate.sleep() 
		print accMsg


if __name__ == '__main__':
	try:
		run()
	except rospy.ROSInterruptException:
		pass