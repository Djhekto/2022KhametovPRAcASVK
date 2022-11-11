from itertools import tee, islice
import sys

def slide(seq, n):
    loopseq, seq = tee(seq)
    ii = 0
    for idx in loopseq:
        tmp, seq = tee(seq, 2)
        ii +=1
        yield from islice(tmp, idx, idx + n)
        #i += 1

#a, b = eval(input())
#next(slide(a,b));
#print(a,b)
exec(sys.stdin.read())