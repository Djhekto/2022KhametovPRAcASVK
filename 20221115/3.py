#
#https://www.tutorialsteacher.com/python/property-decorator



class Student:
    def __init__(self, name):	self.__name = name
    @property
    def name(self):			return self.__name
#    @property
    def hahaha(self):			return self.__name

s = Student('Steve')
print(s.name) 
s = Student('Steve')
print(s.hahaha) 

#-----------------------------------------
class Student:
    def __init__(self, name):	self.__name = name
    @property
    def name(self):				return self.__name
    @name.setter
    def name(self, value):		self.__name=value
    @name.deleter   #property-name.deleter decorator
    def name(self):
        print('Deleting..')
        del self.__name

s = Student('Steve')
s.name = 'Bill'
print(s.name)
del s.name 
#print(s.name)

