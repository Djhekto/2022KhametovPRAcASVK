import math

fd=dict()
count2=0
count1=0
while (s:=input().split())[0]!="quit":
    if s[0][0]==":":
        count1+=1
        fd[s[0][1:]]=(s[1:-1],s[-1])
    if s[0][0]!=":":
        fdd={fd[s[0]][0][i]: eval(s[1:][i]) for i in range(len(s[1:]))} if len(s[1:]) else {}
        try:
            print(eval(fd[s[0]][1], vars(math),fdd))
        except:
            pass
    count2+=1
ss=" ".join(s[1:]).replace('"','')
print(ss.format(count1+1,count2+1))
