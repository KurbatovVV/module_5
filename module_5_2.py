class Point():
	def __init__(self, x, y):
		self.x=x
		self.y=y

	
	def Sum (self):
		return(self.x+self.y)


	def Sub (self):
		return(self.x-self.y)

p1=Point(2,3)
print (p1.Sum())
print (p1.Sub())