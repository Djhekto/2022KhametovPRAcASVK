#Ввести построчно две квадратные матрицы с размерностью 100 ⩾ N ⩾ 2. 
#Рассчитать и вывести произведение матриц (вывод строго через запятую без пробелов)

input1 = list(eval(input()))
hehe = len(input1)# N print(hehe)
sp1=[]
sp1.append(input1)
#----ввкли первую строку и знаем размеры все----------

ii=0
while ii<hehe-1:
    input1 = list(eval(input()))
    sp1.append(input1)
    ii+=1
#print(sp1)
sp2=[]
ii=0
while ii<hehe:
    input1 = list(eval(input()))
    sp2.append(input1)
    ii+=1
#print(sp2)

ahha=0
input1=[]
otvet = []
for i in range(len(sp1)):#k-vo strok sp1
    for j in range(len(sp2[0])):#k-vo stolb sp2
        for ii in range(len(sp2)):
            ahha = sp1[i][ii] * sp2[ii][j]
            input1.append(ahha)
            #print(input1)
        otvet.append(sum(input1))
        input1=[]

#print(otvet,hehe)
for ii,elem in enumerate(otvet[:-1]):
    if (ii+1)%hehe ==0:
        print(elem,end="\n")
    else:
        print(elem,end=",")
print(otvet[-1],end="")
