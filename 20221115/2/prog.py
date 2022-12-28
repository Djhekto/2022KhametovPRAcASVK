class Num:
    counter = 0
    def __get__(self, obj, _):
        if hasattr(obj, "_value"):
            return obj._value
        return self.counter

    def __set__(self, obj, value):
        if 'real' in dir(value):
            obj._value = value.real
        elif '__len__' in dir(value):
            obj._value = len(list(value))

    def __delete__(self, obj):
        obj._value = self.counter

import sys
exec(sys.stdin.read())
