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
	system_builder.add_system("Solar_System_Full", (0, 0), (0, 0))
	bodies = system_builder.get_bodies()
	propagator = Propagator(bodies, time_step = Conversion.minutes(20), time_rate = Conversion.hours(6))
	graphics_controller = GraphicsController(False)
	controller = Controller(propagator, graphics_controller)
	controller.start_simulation()

if __name__ == "__main__":
	main()