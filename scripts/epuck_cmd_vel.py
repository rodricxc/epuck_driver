#!/usr/bin/env python
# Example 10 : Envia comando de velocidade para o robo andar em circulos

import rospy
import math
from geometry_msgs.msg import Twist

def run():
	rospy.init_node('epuck_floor', anonymous=True)

	pub = rospy.Publisher('/mobile_base/cmd_vel', Twist, queue_size=10)

	rate = rospy.Rate(10) # 10hz

	cmd_vel = Twist()

	while not rospy.is_shutdown():
		cmd_vel.linear.x = 1.0
		cmd_vel.angular.z = 2.0
		pub.publish(cmd_vel)
		rate.sleep() 


if __name__ == '__main__':
	try:
		run()
	except rospy.ROSInterruptException:
		pass