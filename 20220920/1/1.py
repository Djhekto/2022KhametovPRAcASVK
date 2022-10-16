#func1 chisl
#  |true => A
#  |false =>-A func1 chisl-25
#		|true =>+ B
#		|False => -B
#func2 chisl  |+C
#	      |-C
#-----------------------=>----------------------
#func1   mod 50 ==0
#func2   mod 8  ==0

#        print(elem,end=', ')

#четн %25 => %50
#else нечетн %25 => %25
#%8

ch = int(input())
if ch % 50 == 0:#четн%25
    print("A + B - ",end='')
else:
    if ch % 25 == 0:#нечетн%25
        print("A - B + ",end='')
    else:#не %25
        print("A - B - ",end='')

if ch % 8 == 0:
    print("C + ",end='')
else:
    print("C - ",end='')
