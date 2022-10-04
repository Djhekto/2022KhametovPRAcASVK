def f1(x):
	def f2(y,a=x):
		return y+a
	return f2

print(f1(1))
