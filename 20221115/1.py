#
"""
def gff(f1):
	def nf(*a):
		print(a,end=' ')
		res = f1(*a)
		print(f"->{res}")
		return res
	return f1

@gff
def f1(a,b):
    return a*2+b

print(f1(2,3))
"""
def genf(f):
    def newfun(*args):
        print(">", *args)
        res = f(*args)
        print("<", res)
        return res
    return newfun

@genf
def fun(a,b):
    return a*2+b

print(fun(2,3))
#----------------------------------------
def multicall(times):
    def decorator(fun):
        def newfun(*args):
            return [fun(*args) for i in range(times)]
        return newfun
    return decorator

@multicall(5)
def simplefun(N):
    return N*2+1

print(*simplefun(4))

#---------------------------------------------------

from functools import wraps

def inter(f):
	@wraps (f)
	def nf(*a):
		if all(map(lambda x: isinstance(x, int), args)):
			return f(*a)
		else:
			raise TypeError("Args must be int")
	return nf


def multer(ii):
	def dec(f):
		def nf(*a, **aa):
			return [f(*a,**aa) for i in range (ii)]
		return nf
	return dec


#@multer(5)
#def ff()






















