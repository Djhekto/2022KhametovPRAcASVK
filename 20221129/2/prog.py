import types
import inspect
import sys

def uncallable(attr):
    if callable(attr):
        return False
    return True

class check(type):
    def __new__(metacls, clsname, bases, namespace, **kwds):
        def sub_check(cls, attr, origin):
            if isinstance(origin, types.GenericAlias):
                origin = origin.__origin__
            return hasattr(cls, attr) and isinstance(getattr(cls, attr), origin)
        def check_annotations(self):
            annotation = inspect.get_annotations(self.__class__)
            return all(sub_check(self, attr, value) for attr, value in annotation.items()\
                                               if uncallable(attr))

        namespace['check_annotations'] = check_annotations
        return super().__new__(metacls, clsname, bases, namespace)


exec(sys.stdin.read())
