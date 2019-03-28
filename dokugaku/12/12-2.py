import math


class Circle():
	def __init__ (self,radius):
		self.radius=radius

	def calculate_area(self):
		return self.radius ** 2 * math.pi

result=Circle(4)
print(result.calculate_area())
