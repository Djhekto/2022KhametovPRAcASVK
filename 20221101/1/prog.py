#Для любого атрибута можно написать операцию omn.атрибут = значение  значение не хранится
#выражение omn.атрибут возвращать количество экземпляров класса, для которых задано поле атрибут
# del omn.атрибут отменяет действие пункта 1 //-1

#Если атрибута нет, ничего.


class Omnibus:
    otvet = {}
    def __setattr__(self, imya, _):
        #https://www.w3schools.com/python/ref_dictionary_setdefault.asp
        self.otvet.setdefault(imya, set())
        self.otvet[imya].add(self)
        
    def __getattr__(self, ii):
        if len(self.otvet[ii]):
            haha = len(self.otvet[ii])
            return haha
        return
    
    def __delattr__(self, imya):
        if self in self.otvet.get(imya, set()):
            _ = self.otvet.pop(imya, set())
            
"""
a, b, c = Omnibus(), Omnibus(), Omnibus()
del a.random
a.i = a.j = a.k = True
b.j = b.k = b.n = False
c.k = c.n = c.m = hex
print(a.i, a.j, a.k, b.j, b.k, b.n, c.k, c.n, c.m)
del a.k, b.n, c.m
print(a.i, a.j, b.j, b.k, c.k, c.n)
del a.k, c.m
print(a.i, a.j, b.j, b.k, c.k, c.n)
a.k = b.i = c.m = 777
print(a.i, a.j, a.k, b.j, b.k, c.k, c.n, c.m) 
print(*a.otvet)
"""