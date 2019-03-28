class Triangle():
	def __init__ (self,base,height):
		self.base = base
		self.height = height

	def calculate_area(self):
		return self.height * self.base / 2

result=Triangle(10,10)
print(result.calculate_area())
