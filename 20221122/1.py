with open('newfile.txt', 'w', encoding='utf-8') as g:
    d = int(input())
    print('1 / {} = {}'.format(d, 1 / d), file=g)


class CM:
    def __init__(self, val = None):
        self.val = val

    def __enter__(self):
        print(">>>")

    def __exit__(self, *args):
        print("<<<",*(c for c in args if c), sep="/", end=">>>\n")
        return self.val

with CM(True) as f:
    print("Working")
    raise SyntaxError("шhат?")

print("Done")

"""  ASCII -> Unicode
>>> sys.getsizeof("qwer")
53
>>> sys.getsizeof("qwert")
54
>>> sys.getsizeof("qwertЫ")
86
"""
import sys
txt = "Вопрос"
print(*map(hex, map(ord, txt)))
#0x412 0x43e 0x43f 0x440 0x43e 0x441
t1 = txt.encode()
#b'\xd0\x92\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81'
t2 = sys.getdefaultencoding()
#'utf-8'
t3 = txt.encode('utf-8')
#b'\xd0\x92\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81'
t4 = txt.encode('WINDOWS-1251')
#b'\xc2\xee\xef\xf0\xee\xf1'
t5 = txt.encode('KOI8-R')
#b'\xf7\xcf\xd0\xd2\xcf\xd3'
t6 = txt.encode('WINDOWS-1251').decode('KOI8-R')
#'бНОПНЯ'
print(txt,t1,t2,t3,t4,t5,t6)

#print("Вопрос".encode("koi8-r").decode("latin3"))

