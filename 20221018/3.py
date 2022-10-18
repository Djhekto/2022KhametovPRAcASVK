from collections import Counter
#Посчитать количество вхождений каждого уникального слова 
#в тексте (слова разделены пробелами) с помощью dict
s = input().split()
c = Counter(s)
print(c)
