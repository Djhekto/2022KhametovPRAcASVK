#chet ::25 => 50*n
#nech ::25 => 25+50*n
# ::8 => 8*n

#func1   mod 50 ==0
#func2   mod 8  ==0
def func1(a,otve,bykva):
	if (a%50 == 0): otve=otve+bykva
	else	      :{ otve=otve+"-"+bykva
			func1(a-25,otve,"B") }

def func2(a,otve):
	if (a%8 == 0): otve=otve+"+C"
	else	     : otve=otve+"-C":
#func1 chisl
#  |true => A
#  |false =>-A func1 chisl-25
#		|true =>+ B
#		|False => -B
#func2 chisl  |+C
#	      |-C
otvet=""
b=input("vvedi chislo")
func1(b,otvet,"A")
func2(b,otvet)

print(otvet)

