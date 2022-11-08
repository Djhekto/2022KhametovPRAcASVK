#super()

#    {OK} Например, дёрнуть «родительский» __init__()

#Линейно унаследовать A → B → C, так, чтобы объект.__str__() 
#выводил путь по дереву наследования, например "A:B" для print(B())

class C:pass
C.__name__
##
class A:
	def __str__(self):
		return "A"

class B(A):
	def __str__(self):
		return super().__str__()+":"+"B"

class C(B):
	def __str__(self):
		return super().__str__()+":"+"C"

a= A
b= B
c= C
print(*c)



