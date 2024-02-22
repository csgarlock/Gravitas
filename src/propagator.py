import numpy as np
import math
import time
import os
import pickle
from gbody import GBody
class Propagator:
	def __init__(self, bodies, G = 6.6743e-11, time_step = 60, time_rate = 86400):
		self.bodies = bodies
		self.G = G
		self.time_rate = time_rate
		self.time_step = float(time_step)
		self.loop_times = 1/(self.time_rate/self.time_step)
		print(self.loop_times)

	def step(self):
		for i in range(len(self.bodies)):
			for j in range(i + 1, len(self.bodies)):
				b_1, b_2 = self.bodies[i], self.bodies[j]
				force_s = self.G * ((b_1.mass * b_2.mass) / ((b_2.pos[0] - b_1.pos[0])**2 + (b_2.pos[1] - b_1.pos[1])**2))
				diff = b_2.pos - b_1.pos
				diff_length = math.sqrt(diff[0]**2 + diff[1]**2)
				scale_factor = force_s / diff_length
				force_v = diff * scale_factor
				b_1.add_force(force_v)
				b_2.add_force(force_v * -1)
		for body in self.bodies:
			b_acc = body.force/body.mass
			body.vel += (b_acc * self.time_step)
			body.pos += (body.vel * self.time_step)
			body.zero_force()

	def run(self, steps = -1, from_grap = None, to_grap = None, to_cont = None):
		if (to_grap is not None):
			g_bodies = self.get_gbodies()
			to_grap.put(g_bodies)
		current_steps = 0
		g_message = from_grap.recv()
		if (g_message != "ready"):
			print("This Definitly should not happen")
			return
		while (current_steps != steps):
			loop_start = time.perf_counter()
			self.step()
			to_grap.put(self.get_gbodies())
			current_steps += 1
			remaining_time = self.loop_times - (time.perf_counter() - loop_start)
			if (remaining_time > 0):
				while(time.perf_counter() - loop_start < self.loop_times):
					pass
			else:
				print("Time Rate overrun")

	def run_to_file(self, steps, name, freq = 10, overwrite = False):
		out_path = "../out/"
		file_path = out_path + name + ".gravitas"
		if (overwrite == False):
			if (os.path.exists(file_path)):
				print("File with that name already exists")
				return
		file = open(file_path, "wb")
		pickle.dump(self.bodies, file, protocol = pickle.DEFAULT_PROTOCOL)
		steps_ran = 0
		start_time = time.perf_counter()
		last_second = 0
		last_second_steps = 0
		while (steps_ran < steps):
			self.step()
			if (time.perf_counter() - start_time > last_second + 1):
				time_r = self.convert_seconds_to_hms((time.perf_counter() - start_time)/(steps_ran/steps) - (time.perf_counter() - start_time))
				print(f"{steps_ran/steps:.2%} complete. ETA {time_r[0]} hours {time_r[1]} minutes {time_r[2]} seconds. Steps per second {last_second_steps}")
				last_second = last_second + 1
				last_second_steps = 0
			if (steps_ran % freq == 0):
				pickle.dump(self.bodies, file, protocol = pickle.DEFAULT_PROTOCOL)
			steps_ran += 1
			last_second_steps += 1
		file.close()

	def convert_seconds_to_hms(self, seconds):
		hours = seconds // 3600
		minutes = (seconds % 3600) // 60
		seconds = seconds % 60
		return hours, minutes, seconds

	def get_gbodies(self):
		g_bodies = []
		for body in self.bodies:
			g_body = GBody(body.mass, body.pos, body.radius, body.id, body.name, body.color)
			g_bodies.append(g_body)
		return g_bodies

