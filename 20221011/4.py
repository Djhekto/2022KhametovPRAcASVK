from math import sin


def put_y(y):
#	for i in range(-30,30):
	print(" "*int((y+1)*20)+"*")

for i in range (-30,30):
	put_y(sin(i/10))
