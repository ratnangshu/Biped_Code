#!/usr/bin/env python
import roslib
roslib.load_manifest('my_dynamixel_tutorial')

import rospy
import actionlib
from std_msgs.msg import Float64
import trajectory_msgs.msg 
import control_msgs.msg  
from trajectory_msgs.msg import JointTrajectoryPoint
from control_msgs.msg import JointTrajectoryAction, JointTrajectoryGoal, FollowJointTrajectoryAction, FollowJointTrajectoryGoal



class Joint:
        def __init__(self, motor_name):
            #arm_name should be b_arm or f_arm
            	self.name = motor_name   
		print(motor_name)        
		self.jta = actionlib.SimpleActionClient('/'+self.name+'_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
		rospy.loginfo('Waiting for joint trajectory action')
		self.jta.wait_for_server()
		rospy.loginfo('Found joint trajectory action!')

            
        def move_joint(self, angles):
            goal = FollowJointTrajectoryGoal()                  
            char = self.name[0] #either 'f' or 'b'
            goal.trajectory.joint_names = ['motor8', 'motor9','motor10','motor11','motor12','motor13','motor14','motor15','motor16','motor17']
            point = JointTrajectoryPoint()
            point.positions = angles
            point.time_from_start = rospy.Duration(0.5)              
            goal.trajectory.points.append(point)
            self.jta.send_goal_and_wait(goal)
              

def main():
	arm = Joint('f_arm')
	#arm.move_joint([0])
        # motor no.      8   9    10   11    12   13   14   15   16   17
	arm.move_joint([3.10,2.49,3.41,0.22,-2.36,2.88,0.30,3.67,2.60,3.01])
	arm.move_joint([3.30,2.49,3.41,0.22,-2.36,2.88,0.30,3.67,2.60,3.34])
	arm.move_joint([3.30,2.60,3.95,0.03,-1.52,2.88,0.32,3.67,2.60,3.34])
	
	##arm.move_joint([3.20,2.60,3.95,0.22,-2.40,2.88,0.35,3.67,2.60,3.24]).36
	
	arm.move_joint([3.20,2.64,3.90,0.03,-1.58,2.79,0.08,3.78,2.56,3.25])
	arm.move_joint([3.09,2.64,3.85,0.21,-1.46,2.80,0.25,3.85,2.58,3.14])
	arm.move_joint([2.90,2.64,3.85,0.21,-1.46,2.80,0.25,3.85,2.58,3.14])

	#abhay
	arm.move_joint([2.80,2.64,3.85,0.21,-1.46,2.50,0.45,3.85,2.58,3.14])
	arm.move_joint([2.70,2.64,3.85,0.21,-1.46,2.50,0.65,3.85,2.88,2.78])
	arm.move_joint([2.70,2.64,3.85,0.21,-1.46,2.30,0.65,3.85,2.88,2.78])


	#arm.move_joint([2.82,2.66,3.6,0.19,-2.61,2.80,0.35,3.85,2.58,3.14])
	#arm.move_joint([2.82,2.66,3.6,0.19,-2.61,2.80,0.25,3.85,2.58,3.14])
	#arm.move_joint([2.90,2.64,3.79,0.29,-2.51,2.80,0.47,3.65,2.39,3.01])
	#arm.move_joint([2.90,2.64,3.79,0.29,-2.49,2.37,0.38,2.93,2.42,3.01])
	###arm.move_joint([2.91,2.69,3.82,0.16,2.53,2.81,0.28,3.61,2.54,3.10])
	
	#arm.move_joint([3.1,2.90,3.75,0.22,-3.14,2.28,0.30,3.25,2.60,3.01])
	#arm.move_joint([3.1,2.90,3.75,0.22,-3.14,2.28,0.30,3.25,2.60,3.05])
        
	
	
print("Hello1")

                        
if __name__ == '__main__':
	rospy.init_node('trajectory_client')
	main()
	print("Hello")
		
