#!/usr/bin/env python
# Example 3 : Le a sensores de proximidade

import rospy
import math
from sensor_msgs.msg import Range

def SensorCallback(sensor):
	global sensorMsg
	sensorMsg = sensor


def run():
	rospy.init_node('epuck_prox_sensor', anonymous=True)

	rospy.Subscriber("/proximity", Range, SensorCallback)

	rate = rospy.Rate(10) # 10hz

	global sensorMsg

	while not rospy.is_shutdown():
		rate.sleep() 
		print sensorMsg


if __name__ == '__main__':
	try:
		run()
	except rospy.ROSInterruptException:
		pass