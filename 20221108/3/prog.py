class Undead(Exception): pass

class Skeleton(Undead): pass
class Ghoul(Undead): pass
class Zombie(Undead): pass

def necro(a):
    if a%3 == 0:
        raise Skeleton
    if a%3 == 1:
        raise Zombie
    if a%3 == 2:
        raise Ghoul

a = eval(input())
try:
    b1 = a[0]
    b2 = a[1]
except:
    pass

for i in range(b1,b2):
    try:
        necro(i)
    except Skeleton:
        print("Skeleton")
    except Zombie:
        print("Zombie")
    except Ghoul:
        print("Generic Undead")
