import numpy as np
class Body:
	def __init__(self, mass, pos, vel, radius = 10, name = "Object", color = "white"):
		self.mass = mass
		self.pos = pos
		self.vel = vel
		self.radius = radius
		self.name = name
		self.color = color
		self.force = np.zeros((2))

	def __str__(self):
		return self.name + " At " + str(self.pos) + " With Velocity " + str(self.vel) 

	def add_force(self, force):
		self.force += force

	def zero_force(self):
		self.force = np.zeros((2))