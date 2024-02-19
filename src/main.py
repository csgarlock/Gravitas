import numpy as np
from propagator import Propagator
from graphicscontroller import GraphicsController
from controller import Controller
from body import Body
from bodyloader import BodyLoader
from systembuilder import SystemBuilder
import json

def main():

	files = ["solar_bodies.json", "solar_systems.json"]
	body_loader = BodyLoader(files)
	system_builder = SystemBuilder(body_loader)
	system_builder.add_body("Earth", (-9.1e8, 0.0), (0.0, -391340.0))
	system_builder.add_body("Earth", (9.1e8, 0.0), (0.0, 391340.0))
	system_builder.add_body("Sun", (0.0, 0.0), (0.0, 0.0))
	bodies = system_builder.get_bodies()
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
	propagator = Propagator(bodies)
	graphics_controller = GraphicsController(False)
	controller = Controller(propagator, graphics_controller)
	controller.start_simulation()

if __name__ == "__main__":
	main()