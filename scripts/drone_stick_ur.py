#!/usr/bin/env python

import numpy as np
import time
from swarmlib import Mocap_object
import rospy

from urx import Robot


rospy.init_node('CrazyflieAPI', anonymous=False)

JOYSTICK_TAKEOFF_HEIGHT = 0.8
initialized    = False
vel_koef       = 0.3
yaw_koef       = 1.0
put_limits       = 0
limits           = np.array([ 1.7, 1.7, 2.5 ]) # limits desining safety flight area in the room
limits_negative  = np.array([-1.7, -1.7, -0.1 ])
rate = rospy.Rate(1.0)

# UR robot-arm
class UR(Robot):
    def __init__(self, ip="192.168.2.102"):
        Robot.__init__(self, ip)
        self.ip = ip
        self.ee_pose = np.zeros(3)
        self.ee_orient = np.zeros(3)

    def move_dx(self, dx):
        try:
            self.x_t += dx  # move robot in tool z axis [m]
        except:
            pass
    def move_dy(self, dy):
        try:
            self.y_t += dy  # move robot in tool z axis [m]
        except:
            pass
    def move_dz(self, dz):
        try:
            self.z_t += dz  # move robot in tool z axis [m]
        except:
            pass

    def move_dp(self, dp):
        try:
            trans = self.get_pose()  # get current transformation matrix (tool to base)
            # print trans.orient
            trans.pos.x += dp[0]
            trans.pos.y += dp[1]
            # trans.pos.z += dp[2]
            self.set_pose(trans, acc=0.01, vel=0.01)  # apply the new pose
        except:
            pass

ur = UR("192.168.2.102")
print 'UR ee-position:', ur.x, ur.y, ur.z

# joystick
drone_joystick_name = 'cf3' # 'cf3'
drone_joystick = Mocap_object(drone_joystick_name)

if __name__ == "__main__":
    # setpoint estimation
    print 'Joystick mean orientation estimation...\n' 
    time_to_eval = 2.0
    a = drone_joystick.orientation()
    for i in range(int(time_to_eval*100)):
        a = np.vstack([a, drone_joystick.orientation()])
        time.sleep(0.01)
    mean_angles = np.array([np.mean(a[:,0]), np.mean(a[:,1]), np.mean(a[:,2])])

    print 'start DroneStick \n'
    while not rospy.is_shutdown():
        drone_joystick.orient = drone_joystick.orientation()
        drone_joystick.position()
        roll = drone_joystick.orient[0] - mean_angles[0]
        pitch = drone_joystick.orient[1] - mean_angles[1]
        yaw = drone_joystick.orient[2] - mean_angles[2]
        dz = drone_joystick.pose[2] - JOYSTICK_TAKEOFF_HEIGHT

        if not initialized:
            ur_init_pose = np.array([ur.x, ur.y, ur.z])
            time_prev = time.time()
            initialized = True

        pitch_thresh = [0.05, 0.15]
        roll_thresh = [0.05, 0.15]
        yaw_thresh = [0.05, 0.50]
        dz_thresh = [0.04, 0.15]
        if abs(pitch)<pitch_thresh[0]:
            x_input = 0
        elif abs(pitch)>pitch_thresh[1]:
            x_input = - np.sign(pitch) * pitch_thresh[1]
        else:
            x_input = - pitch

        if abs(roll)<roll_thresh[0]:
            y_input = 0
        elif abs(roll)>roll_thresh[1]:
            y_input = np.sign(roll) * roll_thresh[1]
        else:
            y_input = roll

        if abs(yaw)<yaw_thresh[0]:
            yaw_input = 0
        elif abs(yaw)>roll_thresh[1]:
            yaw_input = np.sign(yaw) * yaw_thresh[1]
        else:
            yaw_input = yaw

        if abs(dz)<dz_thresh[0]:
            z_input = 0
        elif abs(dz)>dz_thresh[1]:
            z_input = np.sign(dz) * dz_thresh[1]
        else:
            z_input = dz

        cmd_vel = vel_koef*(np.array([x_input, y_input, z_input]))
        yaw_input = yaw_koef * yaw_input
        time_now = time.time()
        print 'Sending velocities:', cmd_vel
        time_prev = time_now

        ur.move_dp(cmd_vel)

        # terminate controller if drone-joystick is landed
        Z = JOYSTICK_TAKEOFF_HEIGHT
        if (Z - drone_joystick.pose[2]) > 0.15:
            break
        rate.sleep()
    ur.close()

