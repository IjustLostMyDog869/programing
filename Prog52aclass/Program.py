class Rectangle:
	def __init__(self, length, width):
		self.length = length
		self.width = width
		
	def area(self):
		return self.length * self.width
	
	def perimeter(self):
		return 2 * self.length + 2 * self.width
	
length = int(input("Enter length: "))
wdth = int(input("Enter width: "))
r = Rectangle(length, width)
prit("Area:", r.area())
print("Perimeter:", r.perimeter())

input()