import numpy as np
from propagator import Propagator
from graphicscontroller import GraphicsController
from body import Body
from multiprocessing import Process
from multiprocessing import Pipe
from multiprocessing import Queue
import time
class Controller:
	def __init__(self, propagator, graphics_controller):
		self.propagator = propagator
		self.graphics_controller = graphics_controller

	def start_simulation(self):
		prop_to_graph_queue = Queue()
		graph_to_prop_queue = Queue()
		prop_to_cont_queue = Queue()
		graph_to_cont_queue = Queue()
		graphics_process = Process(target = self.graphics_controller.run, args = (prop_to_graph_queue, graph_to_prop_queue, graph_to_cont_queue))
		propagator_process = Process(target = self.propagator.run, args = (-1, graph_to_prop_queue, prop_to_graph_queue, prop_to_cont_queue))
		propagator_process.start()
		graphics_process.start()
		graphics_process.join()
		propagator_process.terminate()

