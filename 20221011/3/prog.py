import sys
from math import ceil


s = sys.stdin.read()
k_w = s.count('~')
k_g = s.count('.')
s = list(map(list, s.split()))
w = len(s)
h = len(s[0])
twenty = 20
n_w = ceil(k_w / (w - 2))
n_g = h - 2 - n_w
hc = h
print('#' * w)
for i in range(hc - 2):
    if i < n_g:
        print('#' + '.' * (w - 2) + '#')
    elif i>= n_g:
        print('#' + '~' * (w - 2) + '#')
print('#' * w)
length = len(str(k_g + k_w) + str(max(k_g, k_w))) + 1
if k_g >= k_w:
    print(("." * twenty).ljust(twenty), f"{k_g}/{k_g + k_w}".rjust(length))
    print(("~" * round(k_w / k_g * twenty)).ljust(twenty), f"{k_w}/{k_g + k_w}".rjust(length))
elif k_g < k_w:
    print(("." * round(k_g / k_w * twenty)).ljust(twenty), f"{k_g}/{k_g + k_w}".rjust(length))
    print(("~" * twenty).ljust(twenty), f"{k_w}/{k_g + k_w}".rjust(length))
