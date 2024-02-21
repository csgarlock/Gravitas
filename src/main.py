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
	system_builder.add_system("Solar_System_Full", (0, 0), (0, 0))
	bodies = system_builder.get_bodies()
	run_to_file(bodies)
	# run_from_file("test")
	# run_live(bodies)

def run_from_file(file):
	with open("../out/" + file+ ".gravitas", "rb") as f:
		loaded_data = pickle.load(f)
		loaded_data2 = pickle.load(f)
		for data in loaded_data:
			print (data)
		print(loaded_data2)

def run_to_file(bodies):
	propagator = Propagator(bodies, time_step = Conversion.minutes(1))
	propagator.run_to_file(10000, "test")


def run_live(bodies):

	propagator = Propagator(bodies, time_step = Conversion.minutes(20), time_rate = Conversion.hours(40))
	graphics_controller = GraphicsController(False)
	controller = Controller(propagator, graphics_controller)
	controller.start_simulation()


if __name__ == "__main__":
	main()