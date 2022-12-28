import sys
txt = sys.stdin.buffer.read()
print(txt.decode('utf-8', errors='replace').encode('latin1', errors='replace')\
      .decode('cp1251', errors='replace'),end="\n")
