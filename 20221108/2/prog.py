from math import sqrt

def triangleSquare(s):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(s)
    except:
        return -1

    a = sqrt((x1 - x2)**2 + ((y1 - y2)**2))
    b = sqrt((x2 - x3)**2 + ((y2 - y3)**2))
    c = sqrt((x3 - x1)**2 + ((y3 - y1)**2))
    maxstorona = max([a,b,c])
    summast = min([a + b, b + c, c + a])
    if maxstorona >= summast:
        return -2
    
    return 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))

while 1:
    s = triangleSquare(input())
    if s == -1:
        print("Invalid input")
    if s == -2:
        print("Not a triangle")
    if s >= 0:
        print(s)
        break
