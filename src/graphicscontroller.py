import pygame, sys
import queue
import numpy as np
class GraphicsController:
	def __init__(self):
		self.size = self.width, self.height = 640, 640
		self.screen = None
		self.last_gbodies = None
		self.frame_size = np.array(self.size)
		self.center = np.array([320, 320])
		self.top_left = np.array([0, 0])
		self.pix_ratio = 1


	def run(self, from_prop = None, to_prop = None, to_cont = None):
		pygame.init()
		self.size = self.width, self.height = 1000, 1000
		self.screen = pygame.display.set_mode(self.size)
		self.last_gbodies = from_prop.get()
		print("last Gbodies " + str(self.last_gbodies))
		if (len(self.last_gbodies) > 0):
			pre_av = np.array([0.0, 0.0])
			for gbody in self.last_gbodies:
				pre_av += gbody.pos
			self.center = pre_av / len(self.last_gbodies)
			max_from_av = 0
			for gbody in self.last_gbodies:
				if(abs(gbody.pos[0]) > max_from_av):
					max_from_av = gbody.pos[0]
				if(abs(gbody.pos[1]) > max_from_av):
					max_from_av = gbody.pos[1]
			self.frame_size = np.array([3 * max_from_av, 3 * max_from_av])
			self.top_left = np.array([-1.5 * max_from_av, -1.5 * max_from_av])
			self.pix_ratio = (3*max_from_av)/self.width
		to_prop.send("ready")
		while (True):
			for event in pygame.event.get():
				if (event.type == pygame.QUIT):
					sys.exit()

			self.screen.fill("black")
			self.update_last_gbodies(from_prop)
			for gbody in self.last_gbodies:
				self.draw_gbody(gbody)
			pygame.display.flip()

	def update_last_gbodies(self, q):
		while (True):
			try:
				bodies = q.get(block = False)
				self.last_gbodies = bodies
			except queue.Empty:
				break

	def draw_gbody(self, gbody):
		pygame.draw.circle(self.screen, gbody.color, (gbody.pos-self.top_left)/self.pix_ratio, gbody.radius/self.pix_ratio)

