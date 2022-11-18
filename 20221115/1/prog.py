#декоратор_класса objcount добавляет в класс поле counter
# del -> c-=1

def objcount(class_):
    class_.counter = 0
    initcopy = class_.__init__
    def __init__(self,*args, **kwargs):
        class_.counter += 1
        initcopy
    
    class_.__init__ = __init__
    if "__del__" in class_.__dict__:
        delcopy = class_.__del__
    else:
        delcopy = None
    def __del__(self):
        class_.counter -= 1
        if delcopy!=None:
            return delcopy
    
    class_.__del__ = __del__
    
    return class_

import sys
exec(sys.stdin.read())