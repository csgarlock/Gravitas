import pygame, sys
import queue
import math
import time
import numpy as np
from gbody import GBody
import pickle

#Modes:
# 0 Recieve from propagator
# 1 Read from File
class GraphicsController:
	def __init__(self, true_size = True, mode = 0, file = None, rate = 600, file_rate = 10):
		self.true_size = true_size
		self.size = self.width, self.height = 1000, 1000
		self.screen = None
		self.last_gbodies = None
		self.center = np.array([320.0, 320.0])
		self.top_left = np.array([0, 0])
		self.frame_size = 0
		self.pix_ratio = 1
		self.last_mouse = (0, 0)
		self.mode = mode
		self.file = file
		self.bodies = []
		self.rate = rate
		self.file_rate = file_rate
		self.time_pos = 0

		self.out_path = "../out/"
		self.frame_rate = 60
		self.loop_times = 1.0/self.frame_rate

		self.pos_per_frame = (rate/self.frame_rate)/file_rate


	def run(self, from_prop = None, to_prop = None, to_cont = None):
		pygame.init()
		self.screen = pygame.display.set_mode(self.size)
		if(self.mode == 0):
			self.last_gbodies = from_prop.get()
			print("last Gbodies " + str(self.last_gbodies))
			if (len(self.last_gbodies) > 1):
				self.center_screen()
			to_prop.send("ready")
		if (self.mode == 1):
			with open("../out/" + self.file + ".gravitas", "rb") as f:
				while (True):
					try:
						self.bodies.append(pickle.load(f))
					except EOFError:
						break 
			gbodies = []
			for body in self.bodies[0]:
				gbodies.append(GBody(body.mass, body.pos, body.radius, body.name, body.color))
			self.last_gbodies = gbodies
			self.center_screen()

		while (True):
			loop_start = time.perf_counter()
			for event in pygame.event.get():
				if (event.type == pygame.QUIT):
					pygame.quit()
					sys.exit()
				elif (event.type == pygame.KEYDOWN):
					if (event.key == pygame.K_c):
						self.center_screen()
				elif (event.type == pygame.MOUSEWHEEL):
					self.zoom(event.y)
				elif (event.type == pygame.MOUSEMOTION):
					if (event.buttons[0] == 1):
						self.pan(event.rel)

			self.screen.fill("black")
			self.update_last_gbodies(from_prop)
			for gbody in self.last_gbodies:
				self.draw_gbody(gbody)
			pygame.display.flip()
			remaining_time = self.loop_times - (time.perf_counter() - loop_start)
			if (remaining_time > 0):
				while(time.perf_counter() - loop_start < self.loop_times):
					pass
			else:
				print("Time Rate overrun")

	def update_last_gbodies(self, q):
		if (self.mode == 0):
			while (True):
				try:
					bodies = q.get(block = False)
					self.last_gbodies = bodies
				except queue.Empty:
					break
		if (self.mode == 1):
			self.time_pos += self.pos_per_frame
			gbodies = []
			try:
				for body in self.bodies[math.floor(self.time_pos)]:
					gbodies.append(GBody(body.mass, body.pos, body.radius, body.name, body.color))
			except IndexError:
				pygame.quit()
				sys.exit()
			self.last_gbodies = gbodies


	def pan(self, vector):
		self.center += (-vector[0] * self.pix_ratio, -vector[1] * self.pix_ratio)
		self.top_left = np.array([-self.frame_size/2.0, -self.frame_size/2.0]) + self.center

	def zoom(self, direction):
		zoom_ratio = 1.1
		zoom_amount = zoom_ratio
		if (direction > 0):
			zoom_amount = 1/zoom_ratio
		self.frame_size *= zoom_amount
		self.top_left = np.array([-self.frame_size/2.0, -self.frame_size/2.0]) + self.center
		self.pix_ratio = self.frame_size/self.width



	def center_screen(self):
		pre_av = np.array([0.0, 0.0])
		total_mass = 0
		for gbody in self.last_gbodies:
			pre_av += gbody.pos * gbody.mass
			total_mass += gbody.mass
		self.center = pre_av / total_mass
		max_from_av = 0
		for gbody in self.last_gbodies:
			if(abs(gbody.pos[0] - self.center[0]) > max_from_av):
				max_from_av = abs(gbody.pos[0] - self.center[0])
			if(abs(gbody.pos[1] - self.center[1]) > max_from_av):
				max_from_av = abs(gbody.pos[1] - self.center[1])
		self.top_left = np.array([-1.5 * max_from_av, -1.5 * max_from_av]) + self.center
		self.frame_size = 3 * max_from_av
		self.pix_ratio = self.frame_size/self.width


	def draw_gbody(self, gbody):
		pygame.draw.circle(self.screen, gbody.color, (gbody.pos-self.top_left)/self.pix_ratio, self.inflate_size(gbody.radius/self.pix_ratio))


	def inflate_size(self, radius):
		if (not self.true_size):
			return max(radius, 1)
		else:
			return radius


