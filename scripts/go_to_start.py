from urx import Robot
import time
import numpy as np


robot = Robot("192.168.2.102")
acc = 0.05
vel = 0.06

print "Go to drone takeoff position..."
trans0 = robot.get_pose()
trans0.pos.x = 0.37846
trans0.pos.y = -0.17486
trans0.pos.z = 0.50439
trans0.orient = np.array([[ 0.04920185, -0.87325427,  0.48477434],
       					  [-0.03945265, -0.48668261, -0.87268753],
       					  [ 0.99800935,  0.02381221, -0.05839788]])
robot.set_pose(trans0, acc, vel)
time.sleep(2)

robot.close()
