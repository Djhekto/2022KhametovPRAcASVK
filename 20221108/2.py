#
class C:
	__F = 100500
	def __init__(self, v=0):
		self.__F = v
	def __str__(self):
		return f"<self,self.__F>"

...
c._C__F

class D(C):
	__F = 42
d = D()
print (d)
