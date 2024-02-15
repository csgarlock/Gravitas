import numpy as np
from propagator import Propagator
from graphicscontroller import GraphicsController
from body import Body
from controller import Controller
import matplotlib.pyplot as plt
def main():
	bodies = [
		Body(7.97e25, np.array([-2.5e8, 0.0]), np.array([0.0, -3500]), 6.378e6),
		Body(7.97e25, np.array([2.5e8, 0.0]), np.array([0.0, 3500]), 6.378e6),
		Body(4.97e25, np.array([0.0, 0.0]), np.array([0.0, 0.0]), 9.378e6),
		Body(7.97e25, np.array([0.0, 2.5e8]), np.array([-3500.0, 0.0]), 6.378e6),
		Body(7.97e25, np.array([0.0, -2.5e8]), np.array([3500.0, 0.0]), 6.378e6),
	]
	propagator = Propagator(bodies)
	graphics_controller = GraphicsController()
	controller = Controller(propagator, graphics_controller)
	controller.start_simulation()
	# x = []
	# y = []
	# last_y = propagator.bodies[1].pos[1]
	# orbits = 0
	# for body in propagator.bodies:
	# 	x.append([])
	# 	y.append([])
	# for i in range(1):
	# 	propagator.step()
	# 	this_y = propagator.bodies[1].pos[1]
	# 	if(last_y < 0 and this_y > 0):
	# 		orbits = orbits + 1
	# 	last_y = this_y
	# 	if(i%10 == 0):
	# 		for i in range(len(propagator.bodies)):
	# 			x[i].append(propagator.bodies[i].pos[0])
	# 			y[i].append(propagator.bodies[i].pos[1])
	# print(orbits)
	# print(propagator.bodies[1])
	# for i in range(len(propagator.bodies)):
	# 	plt.plot(x[i], y[i])
	# plt.show()

if __name__ == "__main__":
	main()