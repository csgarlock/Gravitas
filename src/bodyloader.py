from body import Body
import json
import numpy as np
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
			n_body = self.get_body(body["name"])
			pos = body["position"]
			n_body.pos = np.array([pos["x"], pos["y"]])
			vel = body["velocity"]
			n_body.vel = np.array([vel["x"], vel["y"]])
			bodies.append(n_body)
		return bodies



class BodyLoaderError(Exception):
	pass
