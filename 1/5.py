def gen(N):
	adders=[]
	for i in range(1,N+1):
		def adder(x,a=i):
			return x+a
		adders.append(adder)
	return adders

a=gen(11)
print(a)

#def adder(f,g):
#	return lambda x: f(x) + g(x)

