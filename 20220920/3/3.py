#вводит целое положительное число N
#выводит таблицу умножения целых чисел от N до N+2 в виде таблицы 3x3
#при этом если сумма цифр произведения равна 6, то вместо результата печатать смайлик :=)
#(в решении должны использоваться вложенные циклы while)

n = int(input())
nc = 0;
proizv = 0;

def f1(n):#сумма цифр числа
    sum=0
    while n > 0:
        digit = n % 10
        sum = sum + digit
        n = n // 10
    return sum

ii=0
while ii<3:
    i=0
    while i<3:
        nc = n + i
        proizv = nc * n
        print(n,end=' * ')
        print(nc,end=' = ')
        if f1(proizv)==6:
            print(":=)",end=' ')
        else:
            print(proizv,end=' ')           
        i+=1
    print()#новая строка
    n+=1
    ii+=1    
 