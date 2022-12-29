import sys


def method(foo):
    def output(*args, **kwargs):
        print(f'{foo.__name__}: {args[1:]}, {kwargs}')
        return foo(*args, **kwargs)
    return output


class dump(type):
    def __new__(metacls, name, parents, namespace, **kwargs):
        cls = super().__new__(metacls, name, parents, namespace)
        copykwargs = kwargs
        for attr, value in namespace.items():
            if callable(value):
                setattr(cls, attr, method(value)) 

        return cls                   


exec(sys.stdin.read())
