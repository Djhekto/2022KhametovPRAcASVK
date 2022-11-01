# class s lubimi polyami

class C:
	def __getattr__(self,attr):
		if attr.startswith("a"):#dobavit1 luboi esli nazvanie na a
			return attr[1:]
		else:#vivesti oshibky ili naiti v slovare
			return self.__dict__[attr]

#r1 = C(0,0,1,1) 
#r1.rect_1

#r2 = C(1,2,2,2)
#r2.rect_2

#def __setattr__(self):
