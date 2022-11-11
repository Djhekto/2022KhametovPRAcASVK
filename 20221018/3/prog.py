# вводится натуральное число W.
# Затем — многострочный текст, который оканчивается пустой строкой
# Вывести отсортированно через пробел все самые популярные в этом тексте слова длиной W

import string
import sys

d = {}
w = int(input())
text = "".join(sys.stdin.readlines())
clean = string.punctuation + string.digits
for c in clean:
    text = text.replace(c, " ")

text = text.lower()
for word in text.split():
    if len(word) == w:
        d.setdefault(word, 0)
        d[word] += 1

top = sorted(d.items(), key=lambda x: x[1], reverse=True)
ii = 0
if top:
    top_count = top[ii][1]
    i = 0
    while i < len(top) and ((cur_count := top[i][1]) == top_count):
        i += 1
    print(*sorted(_[ii] for _ in top[:i]))

