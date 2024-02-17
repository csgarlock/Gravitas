import numpy as np
import math
class SystemBuilder:
	def __init__(self, body_loader):
		self.body_loader = body_loader
		self.bodies = []

	def add_body(self, name, pos, vel):
		body = self.body_loader.get_body(name)
		body.pos = np.array(pos)
		body.vel = np.array(vel)
		self.bodies.append(body)

	def add_system(self, name, pos, vel, rot = 0):
		system = self.body_loader.get_system(name)
		for body in system:
			body.pos = self.rotate_vector(body.pos, rot) + pos
			body.vel = self.rotate_vector(body.vel, rot) + vel

		self.bodies.extend(system)

	def get_bodies(self):
		return self.bodies

	def rotate_vector(self, vector, degrees):
		x1, y1 = vector
		radians = math.radians(degrees)
		x1_prime = x1 * math.cos(radians) - y1 * math.sin(radians)
		y1_prime = x1 * math.sin(radians) + y1 * math.cos(radians)

		return np.array((x1_prime, y1_prime))