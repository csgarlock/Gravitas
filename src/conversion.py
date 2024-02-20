class Conversion:
	@staticmethod
	def minutes(minutes):
		return minutes * 60
	
	@staticmethod
	def hours(hours):
		return hours * 3600

	@staticmethod
	def days(days):
		return days * 86400

	@staticmethod
	def years(years):
		return years * 31536000

	@staticmethod
	def kilometers(kilometers):
		return kilometers * 1000

	@staticmethod
	def miles(miles):
		return miles * 1609.34

	@staticmethod
	def feet(feet):
		return feet / 3.281 
