#получает через стандартный вход (stdin) последовательность целых чисел в виде списка, например
#выводит результат в стандартный выход (stdout) через пробел и запятую

def f1():
    spisok = eval(input())
    spisok.sort()
#   print(spisok)   
    for ii,elem in enumerate(spisok[:-1]):
        print(elem,end=', ')
    a = spisok[-1:]
    print(a[0])

f1()