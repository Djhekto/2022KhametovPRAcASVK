class C:
	def __init__(self,x1,y1,x2,y2):
		self.A1 = (x1,y1)
		self.A2 = (x1,y2)
		self.A3 = (x2,y2)
		self.A4 = (x2,y1)
	def __str__(self):
		return f"{self.A1},{self.A2},{self.A3},{self.A4}"
#__getitem__ <- cherez iter   | __getattr__
	def __getitem__(self,ii):
		return ((self.A1),(self.A2),(self.A3),(self.A4))[ii]
