#
"""
class 0: pass
class B(0): pass
class F(0, B): pass # <--er
"""
class o: pass
class B(o): pass
class F(B, o): pass 


class A: pass
class B: pass

class C(A,B): pass
class D(B,A): pass

#class E(A,C):pass  #<--ER
#class E(B,D):pass  #<--ER
#class E(C,D):pass  #<--ER


from itertools import permutations
class A: pass
class B: pass

class C(A,B): pass
class D(B,A): pass

for k in range(2,5):
	for R in permutations((A,B,C,D),k):
		try:
			class N(*R): pass
		except Exception as E:
			print(R,E)




