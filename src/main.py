import numpy as np
from propagator import Propagator
from graphicscontroller import GraphicsController
from controller import Controller
from body import Body
from bodyloader import BodyLoader
from systembuilder import SystemBuilder
from conversion import Conversion
import json
import pickle

def main():

	files = ["solar_bodies.json", "solar_systems.json"]
	body_loader = BodyLoader(files)
	system_builder = SystemBuilder(body_loader)
	system_builder.add_system("Earth_System", (0, 0), (0, 0))
	bodies = system_builder.get_bodies()
	# run_to_file(bodies, 10000, "test", True)
	run_from_file("full_solar_sim")
	# run_live(bodies)

def run_from_file(file):
	graphics_controller = GraphicsController(False, 1, file, 600)
	graphics_controller.run()

def run_to_file(bodies, steps, name, overwrite = True):
	propagator = Propagator(bodies, time_step = Conversion.minutes(1))
	propagator.run_to_file(steps, name, overwrite = overwrite)


def run_live(bodies):

	propagator = Propagator(bodies, time_step = Conversion.minutes(20), time_rate = Conversion.hours(40))
	graphics_controller = GraphicsController(False)
	controller = Controller(propagator, graphics_controller)
	controller.start_simulation()


if __name__ == "__main__":
	main()