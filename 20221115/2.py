"""
from functools import chktype
@chktype(float)
def afafa(a,s,d):
	return a
"""
from functools import partial#https://habr.com/ru/company/otus/blog/504102/
 
def multiply(x, y):
       return x * y
 
doubleNum = partial(multiply, 2)
tripleNum = partial(multiply, 3)
 
print(doubleNum(10)) #20
#------------------
from functools import partial
def orderFunc(a,b,c,d):
#	print(a,b,c,d)
	return a*1000 + b*100 + c*10 + d*1

result = partial(orderFunc,5,6,7)# *a -> orderFunc; b,c,d-> orderFunc
print(result(8)) # ->*a
#5,6,7,8 -> f
result = partial(orderFunc,6,7)
print(result(8,5))
#66 => 6,7,8,5 -> f
result = partial(orderFunc,c=6,d=7)
print(result(8,5))#8 5 6 7 ->f

#-------------------------------------









