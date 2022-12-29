import sys


file = sys.stdin.buffer.read()
length = file[0]
txt = file[1:]
tail = len(file[1:])
ii=1
sections = sorted([txt[int(i*tail/length):int((i+ii)*tail/length)] \
                   for i in range(length)])

#lsections = list(sections)#.remove(b"\n")
#print("\n",lsections)
#print("\n",sections,"\n")
sys.stdout.buffer.write((bytes([length]) + b''.join(sections))[:1] +
                        (bytes([length]) + b''.join(sections))[3:])
#sys.stdout.buffer.write(bytes(length) + b"".join(sorted(sections)))
