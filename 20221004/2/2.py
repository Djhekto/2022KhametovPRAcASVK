# (x,y) доминируется парой (a,b), если x<=a, y<=b, и верно хотя бы одно из: x<a, y<b 
#  Pareto(набор пар чисел,), 
#return (каждая из которых НЕ доминируется НИКАКОЙ парой из заданного набора)

def ff (a, b):#a b  et pari
    if a[0] <= b[0] and a[1] <= b[1] and (a[0] < b[0] or a[1] < b[1]):
        return 1
    return 0

def Pareto(*hahah):
    otvet = []
    for pair in hahah:
        for other in hahah:
            if ff(pair, other)==1:      break
        else:                           otvet.append(pair)
    return tuple(otvet)

print(Pareto(*eval(input())))