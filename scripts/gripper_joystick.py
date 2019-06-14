from urx import Robot
import time
import numpy as np


robot = Robot("192.168.2.102")
acc = 0.3
vel = 0.1

trans0 = robot.get_pose()
print "Go to drone initial position..."
trans0.pos.x = 0.11875
trans0.pos.y = 0.22051
trans0.pos.z = 0.69049
trans0.orient = np.array([[-9.99999995e-01, -8.79750522e-05,  5.41215413e-05],
        				  [ 8.79727151e-05, -9.99999995e-01, -4.31829883e-05],
        				  [ 5.41253401e-05, -4.31782269e-05,  9.99999998e-01]])
robot.set_pose(trans0, acc, vel)
time.sleep(2)

print "Start manipulation..."
robot.x_t += 0.1
robot.x_t -= 0.2
robot.x_t += 0.1 # initial pose
robot.y_t += 0.1
robot.y_t -= 0.2
robot.y_t += 0.1 # initial pose

robot.close()
