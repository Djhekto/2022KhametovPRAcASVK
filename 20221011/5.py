from math import sin

screen=[['.']*80 for i in range(20)]
for l in screen:
    print(''.join(l))

def put_y(y):
    print(" "*int((y+1)*20)+"*")

#for i in range (-30,30):
#    put_y(sin(i/10))
