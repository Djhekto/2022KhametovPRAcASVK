#class C:
#	f = 11111
#c = C()
#c.f  #11111
# et odin id
#c.f = 2132132
# raznie id

# cheychik cozdani1 ob1ectov classa
#
#class C:
#	r = 124
#
#b = C()
#b.__class__.r = 12
#b.r = 12
#
#type(b).r = -1
#a = C()
#a.r #-1

class C:
	def __init__(self,x1,y1,x2,y2):
		self.A1 = (x1,y1)
		self.A2 = (x1,y2)
		self.A3 = (x2,y2)
		self.A4 = (x2,y1)
	def __str__(self):
		return f"{self.A1},{self.A2},{self.A3},{self.A4}"
	def rectcnt(self)

r1 = C(0,0,1,1)
r1.rectcnt

r2 = C(1,2,3,4)
r2.rectcnt

#setattr (r1,f"a{r1.rectcnt}",42)
# => r1.ai -> r1.a2 = 42









