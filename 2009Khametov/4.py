#input v cikle
#sum tex chto >0
#input <=0 => end
#sum > 21 =>end

summa = 0
while True:
	a=input("chislo")
	summa = summa + a
	if (a<=0): break
	if (summa>21): break
print (summa)
