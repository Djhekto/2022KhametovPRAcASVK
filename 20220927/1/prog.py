#Ввести натуральные M и N, вывести список простых чисел в диапазоне от M до N

spisok=[]

(m,n) = eval(input())
for ch in range(m,n):
    for i in range(2,ch):
        if ch%i==0:     break;
    else:#for else (none)
        spisok.append(ch)
print(spisok)