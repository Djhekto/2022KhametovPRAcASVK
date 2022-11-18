#с помощью слотов класс Alpha,
#полем любая маленькая буква латинского алфавита
#.__init__(), именные параметры которого задают эти поля
#.__str__() выводит содержимое полей объекта в алфавитном порядке

from string import ascii_lowercase

class Alpha:
    __slots__ = list(ascii_lowercase)

    def __init__(self, **kwargs):
        for c in kwargs: self.__setattr__(c, kwargs[c])

    def __str__(self):
        for c in self.__slots__:
            if hasattr(self, c):
                ahaha = ", ".join(c + ": " + str(self.__getattribute__(c)))
        return ahaha


class AlphaQ:
    def __init__(self, **kwargs):
        for c in kwargs:
            if c in ascii_lowercase:
                self.__setattr__(c, kwargs[c])
            else:
                raise AttributeError

    def __setattr__(self, key, value):
        if key in ascii_lowercase:
            self.__dict__[key] = value
        else:
            raise AttributeError

    def __str__(self):
        for c in ascii_lowercase:
            if hasattr(self, c):
                ahhaa = ", ".join(c + ": " + str(self.__getattribute__(c)))
        return ahhaa

import sys
exec(sys.stdin.read())
