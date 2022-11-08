class A:
	v = 1

class B(A):
	v=2
	#v0 = 2

	def __init__(self):
		self.v = 3


class A:
	def __init__(self,v):
		self.v = v
	def __add__(self,o):
		return A(self.v+o.v)

class B(A):
	pass

c = B(10) + B(11)
print(c.v,type(c))#21 class A
#21 B   <--??

class A:
	def __init__(self,v):
		self.v = v
#	def __add__(self,o):
#		return A(self.v+o.v)

class B(A):
	pass
	def __add__(self,o):
		return B(self.v+o.v)

c = B(10) + B(11)
print(c.v,type(c))#21 B

class A:
	def __init__(self,v):
		self.v = v
	def __add__(self,o):
		return self.__class__(self.v+o.v)


c = B(10) + B(11)
print(c.v,type(c))#21 B



