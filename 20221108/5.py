#

class B(Exception):
	pass

class C(B):
	pass

class D(C):
	pass

for cl in [B,C,D]:
	try:
		raise cl()
	except D:
		print("d")
	except C:
		print("c")
	except B:
		print("b")





#
