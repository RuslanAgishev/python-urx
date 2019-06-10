from urx import Robot
import time

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
print 'Position:', robot.x, robot.y, robot.z
# print 'Orientation:', robot.get_orientation()

move_dx(robot, -0.1)
move_dy(robot, 0.05)
move_dz(robot, 0.05)

# print robot.x  # returns current x
# robot.rx  # returns 0 (could return x component of axis vector, but it is not very usefull
# robot.rx -= 0.1  # rotate tool around X axis



robot.close()
