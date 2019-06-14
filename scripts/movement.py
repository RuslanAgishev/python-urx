from urx import Robot
import time
import numpy as np


robot = Robot("192.168.2.102")
acc = 0.05
vel = 0.06

trans0 = robot.get_pose()
# print "Go to drone takeoff position..."
# trans0.pos.x = 0.37846
# trans0.pos.y = -0.17486
# trans0.pos.z = 0.50439
# trans0.orient = np.array([[ 0.04920185, -0.87325427,  0.48477434],
#        					  [-0.03945265, -0.48668261, -0.87268753],
#        					  [ 0.99800935,  0.02381221, -0.05839788]])
# robot.set_pose(trans0, acc, vel)
# time.sleep(2)

print "Go to landing pad release position..."
trans_release_pad = trans0
trans_release_pad.pos.x = 0.25152
trans_release_pad.pos.y = -0.51420
trans_release_pad.pos.z = 0.50441
trans_release_pad.orient = np.array([[ 0.02487802, -0.99955103,  0.01669785],
       								 [-0.05793992, -0.01811662, -0.99815568],
       								 [ 0.99801005,  0.02386466, -0.05836461]])
robot.set_pose(trans_release_pad, acc, vel)
time.sleep(1)

print "Go a bit back..."
trans_go_back = trans0
trans_go_back.pos.x = 0.25147
trans_go_back.pos.y = -0.37025
trans_go_back.pos.z = 0.50445
trans_go_back.orient = np.array([[ 0.02489004, -0.99955202,  0.01662049],
       							 [-0.05786863, -0.01803836, -0.99816123],
       							 [ 0.99801388,  0.02388247, -0.05829169]])
robot.set_pose(trans_go_back, acc, vel)
# time.sleep(2)

print "Go to manipulate cubes..."
trans_cubes = trans0
trans_cubes.pos.x = 0.25143
trans_cubes.pos.y = -0.37026
trans_cubes.pos.z = 0.41464
trans_cubes.orient = np.array([[-0.99822647, -0.05719822,  0.01650087],
       						   [-0.01977977,  0.05724144, -0.9981644 ],
       						   [ 0.05614869, -0.99672051, -0.05827129]])
robot.set_pose(trans_cubes, acc, vel)
# time.sleep(2)

robot.close()
