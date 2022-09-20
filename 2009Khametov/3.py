#chet ::25 => 50*n
#nech ::25 => 25+50*n
# ::8 => 8*n

#func1   mod 50 ==0
#func2   mod 8  ==0

#func1 chisl
#  |true => A
#  |false =>-A func1 chisl-25
#		|true =>+ B
#		|False => -B
#func2 chisl  |+C
#	      |-C
