from fractions import Fraction

def ff (args, i, s):
    fr = args[i]
    for iii in range(int(args[i - 1])):
        fr *= s
        fr += args[iii + i + 1]
    return fr

def f1 (args):
    s = args[0]#znachenie s chekaem
    sprava = args[1]
    stepv = int(args[2])

    ii = 3
    chislitel1 = ff(args, ii, s)
    ii = ii + stepv + 2
    znamenatel1 = ff(args, ii, s)
    return chislitel1 / znamenatel1 == sprava


args = input()# s, sprava, stepen1 verx, {koefi verx}, stepen1 niz, {koefi niz}
args = args.split(", ")# in 1, -1/8, 2, 1, -5/2, 1, 1, 1, 3
nargs = []
for elem in args:
    nargs.append(Fraction(str(elem))) #https://docs.python.org/3/library/fractions.html
#print(nargs) konvertit v tip drobi poka ne razvernem

print(f1(nargs))