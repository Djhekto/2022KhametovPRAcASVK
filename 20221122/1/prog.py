import sys


file = sys.stdin.buffer.read()
length = file[0]
txt = file[1:]
tail = len(file[1:])
ii=1
sections = sorted([txt[int(i*tail/length):int((i+ii)*(tail/length))] \
                   for i in range(length)])

sys.stdout.buffer.write(bytes([length]) + b''.join(sections))
