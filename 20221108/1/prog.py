import collections

class DivStr(collections.UserString):
    dlina = 0
    def __init__(self, s = ''):
        try:
            self.dlina = len(s)
        except:
            self.dlina = 0
        super().__init__(s)        
            
    def __floordiv__(self, other):
        a = int(self.dlina/other)
        s = []
        for i in range(other):
            s.append(self[a * i: a * (i+1)])
        return s
        
    def __mod__(self,other):
        return self[self.dlina-self.dlina%other:]


import sys
exec(sys.stdin.read())
