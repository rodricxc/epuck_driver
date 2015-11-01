#!/usr/bin/env python
# PID controller to navigate the robot

import rospy
import math
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseStamped

odomMsg = 'Null'
goalMsg = 'Null'

threshold = 0.025
M_PI_8 = 0.392699082

def OdomCallback(odom):
	global odomMsg
	odomMsg = odom


def GoalCallback(goal):
	global goalMsg
	goalMsg = goal	


def run():
	rospy.init_node('epuck_move_base', anonymous=True)

	pub = rospy.Publisher('/mobile_base/cmd_vel', Twist, queue_size=10)
	#pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

	rospy.Subscriber("/odom", Odometry, OdomCallback)

	rospy.Subscriber("/move_base_simple/goal", PoseStamped, GoalCallback)

	rate = rospy.Rate(10) # 10hz

	global odomMsg
	global goalMsg

	cmd_vel = Twist()

	while not rospy.is_shutdown():
		if goalMsg == 'Null':
			rate.sleep()
			continue

		dx = goalMsg.pose.position.x - odomMsg.pose.pose.position.x
		dy = goalMsg.pose.position.y - odomMsg.pose.pose.position.y

		if abs(dx) <= threshold and abs(dy) <= threshold:
			cmd_vel.linear.x = 0.0
			cmd_vel.angular.z = 0.0
			pub.publish(cmd_vel)
			rate.sleep()
			continue

		theta = math.atan2(dy, dx)
		w = (odomMsg.pose.pose.orientation.x, odomMsg.pose.pose.orientation.y,
			 odomMsg.pose.pose.orientation.z, odomMsg.pose.pose.orientation.w)
		euler = tf.transformations.euler_from_quaternion(w)
		yaw = euler[2]
		ang = (theta - yaw)

		if ang > math.pi:
			ang -= 2*math.pi

		cmd_vel.angular.z = ang
		cmd_vel.linear.x = 0.2
		#cmd_vel.linear.x = 0.5 * (1 - abs(ang)/2*math.pi)
		pub.publish(cmd_vel)
		rate.sleep()


if __name__ == '__main__':
	try:
		run()
	except rospy.ROSInterruptException:
		pass

