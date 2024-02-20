from body import Body
import json
import numpy as np
import math
class BodyLoader:
	def __init__(self, files):
		self.data_folder = "../data/"
		self.bodies = {}
		self.systems = {}
		for path in files:
			try: 
				with open(self.data_folder + path, "r") as file:
					data = json.load(file)
					if (data["type"] == "body"):
						for body in data["bodies"]:
							self.bodies[body["name"]] = body
					elif (data["type"] == "system"):
						for system in data["systems"]:
							self.systems[system["name"]] = system
					else:
						raise BodyLoaderError("Invalid Format in file: " + str(path))
			except FileNotFoundError:
				raise BodyLoaderError("File not Found: " + str(path))
			except KeyError:
				raise BodyLoaderError("Error reading file: " + str(path))
			except Exception as e:
				raise BodyLoaderError("Unexpected Error Occured: " + str(e))

	def get_body(self, name):
		try:
			return (Body(self.bodies[name]["mass"], np.array([0.0, 0.0]), np.array([0.0, 0.0]), self.bodies[name]["radius"], name))
		except KeyError:
			raise BodyLoaderError("Could Not find body with name: " + str(name))

	def get_system(self, name):
		try:
			system = self.systems[name]
		except KeyError:
			raise BodyLoaderError("Could not find system with name: " + str(name))
		bodies = []
		for body in system["bodies"]:
			if (body["type"] == "body"):
				n_body = self.get_body(body["name"])
				pos = body["position"]
				n_body.pos = np.array([pos["x"], pos["y"]])
				vel = body["velocity"]
				n_body.vel = np.array([vel["x"], vel["y"]])
				bodies.append(n_body)
			if (body["type"] == "system"):
				system_bodies = self.get_system(body["name"])
				for s_body in system_bodies:
					s_body.pos = self.rotate_vector(s_body.pos, body["rotation"])
					s_body.vel = self.rotate_vector(s_body.vel, body["rotation"])
					pos = body["position"]
					s_body.pos += np.array([pos["x"], pos["y"]])
					vel = body["velocity"]
					s_body.vel += np.array([vel["x"], vel["y"]])
				bodies.extend(system_bodies)
		return bodies

	def rotate_vector(self, vector, degrees):
		x1, y1 = vector
		radians = math.radians(degrees)
		x1_prime = x1 * math.cos(radians) - y1 * math.sin(radians)
		y1_prime = x1 * math.sin(radians) + y1 * math.cos(radians)

		return np.array((x1_prime, y1_prime))



class BodyLoaderError(Exception):
	pass
