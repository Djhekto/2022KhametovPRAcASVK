#Реализовать рекурсивную функцию бинарного поиска 
#(проверки наличия) элемента в упорядоченной по 
#неубыванию индексируемой хранимой последовательности.

def f1(ch, string):
    opti1 = len(string)
    if opti1 == 0:		return False
    if (opti1 % 2 ==0):	center = (opti1 // 2)
    else:						center = ((opti1 // 2) - 1)
    if ch == string[center]:    return  True
    else:
        if ch > string[center]:     return f1(ch, string[center + 1:])#levaya
        else:                       return f1(ch, string[:center])#pravaya

ch, string = eval(input())#"a", "abcdfghklmoprsyz"
print(f1(ch, string))