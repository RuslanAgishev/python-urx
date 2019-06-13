from urx import Robot
import time
import numpy as np

def connect(robot_ip="192.168.2.102"):
	connected = False
	while not connected:
		try:
			robot = Robot(robot_ip)
			connected = True
			print "Robot", robot_ip, "is connected"
		except:
			pass
	return robot

def move_dx(robot, dx):
	try:
		robot.x_t += dx  # move robot in tool z axis [m]
	except:
		pass
	dt = 20*abs(dx)
	time.sleep(dt)
def move_dy(robot, dy):
	try:
		robot.y_t += dy  # move robot in tool z axis [m]
	except:
		pass
	dt = 20*abs(dy)
	time.sleep(dt)
def move_dz(robot, dz):
	try:
		robot.z_t += dz  # move robot in tool z axis [m]
	except:
		pass
	dt = 20*abs(dz)
	time.sleep(dt)

robot = Robot("192.168.2.102")
# print 'Position:', robot.x, robot.y, robot.z
# print 'Orientation:', robot.get_orientation()

trans = robot.get_pose()
print trans.pos

# robot.set_orientation([np.pi/2, 0, 0])
# time.sleep(5)

# move_dx(robot, -0.1)
# move_dy(robot, 0.05)
# move_dz(robot, -0.1)

# try:
# 	trans = robot.get_pose()  # get current transformation matrix (tool to base)
# 	trans.pos.z -= 0.1
# 	robot.set_pose(trans, acc=0.01, vel=0.03)  # apply the new pose
# except:
# 	pass

# try:
# 	robot.movel((0.0, 0, 0.8, 0, 0, 0), acc=0.01, vel=0.01, relative=False)  # move relative to current pose
# 	time.sleep(5.0)
# except:
# 	pass

# vx_rob = -0.05
# vy_rob = 0
# vz_rob = 0
# robot.speedl((vx_rob , vy_rob , vz_rob , 0, 0, 0), acc=0.1, min_time=1);
# time.sleep(1)


# try:
# 	speeds = [0,0,0.05, 0,0,0]
# 	robot.speedj(velocities=speeds, acc=0.01, min_time=2)
# except:
# 	print 'no vel control'

robot.close()
