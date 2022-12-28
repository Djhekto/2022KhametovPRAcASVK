def fib(m,n):
    x = 0
    y = 1
    for _ in range(m):
        try:
            x,y=y,x+y
        except:
            pass
        
    for _ in range(m,m+n):
        yield y
        x,y=y,x+y

import sys
exec(sys.stdin.read())
