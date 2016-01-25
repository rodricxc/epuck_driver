#!/usr/bin/env python
# Example 3 : Le a posicao do seletor

import rospy
import math
from visualization_msgs.msg import Marker

def SelectorCallback(s):
	global sMsg
	sMsg = s


def run():
	rospy.init_node('epuck_selector', anonymous=True)

	rospy.Subscriber("/selector", Marker, MarkerCallback)

	rate = rospy.Rate(10) # 10hz

	global sMsg

	while not rospy.is_shutdown():
		rate.sleep() 
		print sMsg


if __name__ == '__main__':
	try:
		run()
	except rospy.ROSInterruptException:
		pass