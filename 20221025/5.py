from itertools import *

def flt(n, seq):
	yield from filterfalse(lambda x: x % n, seq)
