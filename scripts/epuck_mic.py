#!/usr/bin/env python
# Example 7 : Le os dados do microfone

import rospy
import math
from visualization_msgs.msg import Marker

def MicCallback(m):
	global mMsg
	mMsg = m


def run():
	rospy.init_node('epuck_microphone', anonymous=True)

	rospy.Subscriber("/microphone", Marker, MicCallback)

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