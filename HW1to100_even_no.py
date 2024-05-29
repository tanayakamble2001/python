'''a=0
i=1
while i<=100:
    num=i%2
    if num==0:
        a=list(i)
        print(a)
    i+=1
'''
b=[]
for i in range(1,101,1):
    num=i%2
    if num==0:
        b.append(i)
print(b)
