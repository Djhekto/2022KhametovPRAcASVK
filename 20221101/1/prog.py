from collections import defaultdict


class Omnibus:
    attribs = defaultdict(int)
    counter = 1

    def __init__(self):
        pass

    def __setattr__(self, key, value):

        if key not in self.__dict__:
            self.__dict__[key] = value
            Omnibus.attribs[key] += self.counter

    def __getattribute__(self, key):
        if key in Omnibus.attribs:
            return Omnibus.attribs[key]

        return object.__getattribute__(self, key)

    def __delattr__(self, key):
        if key in self.__dict__:
            Omnibus.attribs[key] -= self.counter

            self.__dict__.pop(key)

    def __del__(self):
        for key in self.__dict__:
            Omnibus.attribs[key] -= self.counter 
            
import sys
try:
    exec(sys.stdin.read())
except:
    pass