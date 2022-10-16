#Написать программу, которая вводит два числа через запятую и выводит наибольшее из них

#a = eval(input())
#print(a)
#ch1 = a[0]
#ch2 = a[1]
#print(ch1)

def f1():
    (a,b) = eval(input())
    if a>b: return a
    return b

print(f1())