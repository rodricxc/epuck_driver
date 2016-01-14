#!/usr/bin/env python
# Example 1 : Le a velocidade do robo

import rospy
import math
from sensor_msgs.msg import Image

def CameraCallback(Image):
	global ImageMsg
	ImageMsg = Image


def run():
	rospy.init_node('epuck_camera', anonymous=True)

	rospy.Subscriber("/camera", Image, CameraCallback)

	rate = rospy.Rate(10) # 10hz

	global ImageMsg

	while not rospy.is_shutdown():
		rate.sleep() 
		print ImageMsg


if __name__ == '__main__':
	try:
		run()
	except rospy.ROSInterruptException:
		pass