#itertools
#list(combinations("sdad",3)) #d считаются разными

#=========
from itertools import *
## product('ABCD', 'xy')
#a=product("abcdefgh","12345678")
#print(a)

#for elem in product("abcdefgh","12345678"):
#	print(elem)

#list(product("abcdefgh","12345678"))

for a in map("".join , product("abcdefgh","12345678")):
	print(a, end=" ")
