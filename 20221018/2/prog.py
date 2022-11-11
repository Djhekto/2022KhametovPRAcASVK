#in:
# - :функция переменная_1 переменная_2 … Питоновское_выражение_без_пробелов_от_этих_переменных
# -  функция константа_1 константа_2 …
# -  quit "{}:{}"

#from math import *
import math

func_dict = {}
i, ii = 1, 1
while 1:
    s = input()
    s = s.split()
    if s[0] == "quit": break;# -  quit "{}:{}"
    ii += 1
    ff = s[0]
    if ff[0] == ":":# - :функция переменная_1 переменная_2 … Питоновское_выражение_без_пробелов_от_этих_переменных
        i += 1
        args, expr = s[1:-1], s[-1]
        ff = ff[1:]
        func_dict[ff] = (args, expr)
    if ff[0] != ":":# -  функция константа_1 константа_2 …
        args = s[1:]
        for i in range(len(args)):
            if len(args): 
                ctx = {func_dict[ff][0][i]: eval(args[i])}
            else: 
                ctx = {}
        print(eval(func_dict[ff][1], vars(math), ctx))

expr = (" ".join(s)).split(maxsplit=1)[-1].strip("\"")
print(expr.format(i, ii))