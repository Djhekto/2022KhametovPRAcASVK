#дескриптор Num, который хранит только числа
#послед -> длинна

class Num:
    otvet = 0
    def __get__(self, instance, _):
        if hasattr(instance, "_val") == False:
            instance.otvet = 0
        return instance._val
    def __set__(self, instance, value):
        if hasattr(value, "real"):
            instance._val = value.real
        else:
            if hasattr(value, "__len__"):
                instance._val = len(value)

import sys
exec(sys.stdin.read())