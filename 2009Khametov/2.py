a=int(input("storona a"))
b=int(input("storona b"))
c=int(input("storona c"))
check=0
if(a<0):	check = check+1
if(b<0):	check=check+1
if(c<0):	check=check+1
#print (check)
#a<b+c b<a+c c<b+a
if(a>=b+c):        check=check+1
if(b>=a+c):        check=check+1
if(c>=a+b):        check=check+1
#
#print(check)
if(check==0):	print("treugolnik")
else:		print("ne treugolnik")

