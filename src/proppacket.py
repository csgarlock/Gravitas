class PropPacket:
	def __init__(self, gbodies, time_rate, time_step, collisions):
		self.gbodies = gbodies
		self.time_rate = time_rate
		self.time_step = time_step
		self.collisions = collisions