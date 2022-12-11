#Написать класс DivStr (унаследованный от collections.UserString), в котором:

# возможность заведения пустой строки без параметров — DivStr()

# операция a // n — возвращается итератор из n подстрок
#    одинакового наибольшего размера, на которые можно разбить исходную строку

# операция a % n — возвращается «остаток от деления»,
#     хвостик, который надо приписать к a // n, чтобы получилась вся строка (возможно, пустой)


from collections import UserString
import sys


class DivStr(UserString):
    dlina = 0
    def __init__(self, sstr=""):
        try:
            self.dlina = len(sstr)
        except:
            self.dlina = 0
        super().__init__(sstr)

    def __floordiv__(self, n):#//
        dlina1 = int(self.dlina / n)
        otvet = []
        for i in range(0, n * dlina1, dlina1):
            #print(self[i:i+dlina1])
            otvet.append(self[i:i + dlina1])
        return iter(otvet)
    
    def __mod__(self, n):#%
        return self[-(self.dlina%n):]
    
#exec(sys.stdin.read())

#a = DivStr("XcDfQWEasdERTdfgRTY")
#print(* a // 4)
#print(a % 4)
#print(* a % 10 // 3)
#print(a.lower() % 3)
#print(* a[1:7] // 3)
#print(a % 5 + DivStr() + a % 6)