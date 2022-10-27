#числа Фибоначчи - последовательность, начинающаяся с 1, 1, 
# и продолжающаяся так, что очередной элемент равен сумме двух предшествующих элементов.
#написать генератор-функцию fib(m, n),
# возвращающую итератор по числа Фибоначчи, начинаю с m-го и заканчивая n-м (m⩽n), в нумерации с 0

from itertools import islice

def fgen():
    a, b = 1, 1
    yield a
    while 1:
        c = a + b
        a = b 
        b = c
        yield a

def fib(m, n):#https://stackoverflow.com/questions/5234090/how-to-take-the-first-n-items-from-a-generator-or-list
    nelem = islice(fgen(), n+1)
    lelem = [elem for elem in nelem if elem>=m]
    return lelem

a1, b1 = eval(input())
print (*fib (a1, b1), sep = ", ")
