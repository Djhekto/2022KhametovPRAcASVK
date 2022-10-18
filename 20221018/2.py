#Посчитать, сколько уникальных гласных и сколько согласных в строке 

s = set(input())
gl = set("AEIOUY")
gl1= set(x[0].lower() for x in gl)
sg = set("BCDFGHJKLMNPQRSTVWXYZ")
sg1= set(x[0].lower() for x in sg)
print((s-gl)-gl1)
print((s-sg)-sg1)
