from math import *

def func_s(x,s):
    return eval(s, globals(), {"x": x})

def func_t(x,t):
    return eval(t, globals(), {"x": x})

def Calc(s, t, u):
    def func(x):
        xx = func_s(x,s)
        yy = func_t(x,t)
        return eval(u, globals(), {"x": xx, "y": yy})
    return func

l = eval(input())
x = eval(input())
print(Calc(*l)(x))
