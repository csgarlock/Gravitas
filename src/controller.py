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
		p_from_grap, g_to_prop = Pipe()
		prop_to_cont_queue = Queue()
		graph_to_cont_queue = Queue()
		graphics_process = Process(target = self.graphics_controller.run, args = (prop_to_graph_queue, g_to_prop, graph_to_cont_queue))
		propagator_process = Process(target = self.propagator.run, args = (-1, p_from_grap, prop_to_graph_queue, prop_to_cont_queue))
		propagator_process.start()
		graphics_process.start()
		graphics_process.join()
		propagator_process.join()

