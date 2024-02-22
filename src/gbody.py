class GBody:
	def __init__(self, mass, pos, radius, id_num, name = "Object", color = "white"):
		self.mass = mass
		self.pos = pos
		self.radius = radius
		self.name = name
		self.color = color
		self.id = id_num

	def __str__(self):
		return self.name + " At " + str(self.pos)