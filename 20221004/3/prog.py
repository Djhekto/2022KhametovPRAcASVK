#Написать функцию вычитания двух объектов

def f1(a, b):
    try:
        return a - b
    except TypeError as err:
        if type(a)() == type(b)() == []:
            otvet = [elem for elem in a if elem not in b]
            return otvet
        if type(a)() == type(b)() == ():
            otvet = tuple(elem for elem in a if elem not in b)
            return otvet
        raise err

print(f1(*eval(input())))