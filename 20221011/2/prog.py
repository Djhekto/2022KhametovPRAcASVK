from math import *

width, hight, a, b, func = input().split()
width = int(width)
hight = int(hight)
a = int(a)
b = int(b)

def f(x):
    return eval(func)

canvas = []
for i in range(hight + 1):
    stroka = [' '] * (width + 1)
    canvas.append(stroka)

xs = []
for i in range(width + 1):
    ch = i * (b - a) / width + a
    xs.append(ch)

ys = []
for znach in xs:
    znachf = f(znach)
    ys.append(znachf)

xc = xs
xs = []
for x in xc:
    xs.append((x-a))

yc = ys
ys = []
for y in yc:
    ys.append((y - min(yc)))

ys = [round(y * hight / max(ys)) for y in ys]

for i in range(1, width + 1):
    canvas[hight - ys[i]][i]= '*'
    if ys[i - 1] <= ys[i]:
        step = 1 
    else:
        step = -1
    for j in range(ys[i - 1], ys[i], step):
        canvas[hight - j][i - 1] = '*'

for line in canvas:
    print(*line,sep='')