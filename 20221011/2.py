# e = sum(1/n!) ot 1..i
import math

def esum(n,one):
	i=0;
	sum=0
	while i<n:
		sum+=1/math.factorial(i)
		i+=1
	return sum

print(esum(10,1))
