#Подсчитать количество различных пар букв в тексте
#На вход строка,
#буква: isalpha() возвращает True
#Требуется подсчитать количество различных пар букв в тексте

otvet = input()
otvet = otvet.lower()
pari = set()
count = 0
for i in range(1, len(otvet)):
    para = otvet[i-1: i+1]
    if para.isalpha():
        if para not in pari:
            pari.add(para)
            count += 1

print(count)
