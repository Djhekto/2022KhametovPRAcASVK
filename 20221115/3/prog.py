#с помощью слотов класс Alpha,
#полем любая маленькая буква латинского алфавита
#.__init__(), именные параметры которого задают эти поля
#.__str__() выводит содержимое полей объекта в алфавитном порядке

class Alpha:
    __slots__ = [x for x in 'abcdefghijklmnopqrstuvwxyz']

    def __init__(self, **kwargs):
        for x in kwargs:
            self.__setattr__(x, kwargs[x])

    def __str__(self):
        s = ""
        counter = 2
        for x in self.__slots__:
            if hasattr(self, x):
                s += f"{x}: " + str(self.__getattribute__(x)) + ", "
        if s:
            return s[:-counter]


class AlphaQ:
    _letters = [x for x in 'abcdefghijklmnopqrstuvwxyz']

    def __init__(self, **kwargs):
        for i,(k, v) in enumerate(kwargs.items()):
            setattr(self, k, v)

    def __setattr__(self, k, v):
        if k in self._letters:
            self.__dict__[k] = v
        else:
            raise AttributeError

    def __str__(self):
        s_dict = sorted(self.__dict__.items())
        return ", ".join(f"{k}: {v}" for (k, v) in s_dict)

import sys
exec(sys.stdin.read())
