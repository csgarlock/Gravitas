import numpy as np
from propagator import Propagator
from graphicscontroller import GraphicsController
from controller import Controller
from body import Body
from bodyloader import BodyLoader
from systembuilder import SystemBuilder
from conversion import Conversion
import json

def main():

	files = ["solar_bodies.json", "solar_systems.json"]
	body_loader = BodyLoader(files)
	system_builder = SystemBuilder(body_loader)
	system_builder.add_system("Mars_System", (0, 0), (0, 0))
	bodies = system_builder.get_bodies()
	propagator = Propagator(bodies, time_step = 1, time_rate = Conversion.minutes(20))
	graphics_controller = GraphicsController(False)
	controller = Controller(propagator, graphics_controller)
	controller.start_simulation()

if __name__ == "__main__":
	main()