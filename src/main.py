import numpy as np
from propagator import Propagator
from graphicscontroller import GraphicsController
from body import Body
from bodyloader import BodyLoader
import json

def main():

	files = ["solar_bodies.json", "solar_systems.json"]
	body_loader = BodyLoader(files)
	bodies = body_loader.get_system("Mars_Systemiss")
	for body in bodies:
		print (body)
	# bodies = [
	# 	Body(5.98e24, np.array([-3.5e8, 0.0]), np.array([0.0, -3400]), 6.378e6),
	# 	Body(5.98e24, np.array([3.5e8, 0.0]), np.array([0.0, 3400]), 6.378e6),
	# 	Body(2.97e25, np.array([5.0e7, 0.0]), np.array([0.0, 3800.0]), 9.378e6),
	# 	Body(2.97e25, np.array([-5.0e7, 0.0]), np.array([0.0, -3800.0]), 9.378e6),
	# 	Body(5.98e24, np.array([0.0, 3.5e8]), np.array([-3900.0, 0.0]), 6.378e6),
	# 	Body(5.98e24, np.array([0.0, -3.5e8]), np.array([3900.0, 0.0]), 6.378e6)
	# ]
	# propagator = Propagator(bodies)
	# graphics_controller = GraphicsController()
	# controller = Controller(propagator, graphics_controller)
	# controller.start_simulation()

if __name__ == "__main__":
	main()