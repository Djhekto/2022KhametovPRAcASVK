# pereryzka 
class C:
	def __init__(self,x1,y1,x2,y2):
		self.A1 = (x1,y1)
		self.A2 = (x1,y2)
		self.A3 = (x2,y2)
		self.A4 = (x2,y1)
	def __str__(self):
		return f"{self.A1},{self.A2},{self.A3},{self.A4}"
#https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
	def __lt__(self,drugoi):#<
		return pass#abs(A2-A1)*abs(A3-A2) < abs(b2-b1)*abs(b3-b2)  -> t|f
