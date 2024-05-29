a=[1,2,3,4,5,6,7,8,9,10]
e=[]
o=[]
for i in a:
    if i%2 == 0:
        e.append(i)        
    elif i%2!=0:
        o.append(i)
print(e)
print(o)


#count duplicate value
b=[1,2,3,4,5,6,7,7,6,6,6,4]
count=0
'''for i in b:
    c1=0
    for j in range(i+1,len(b),1):
        if i == j:
            c1=c1+1
    if c1:
        print(f"{i} duplicate are {c1}")
'''
c=[]
d=[]
for i in b:
    if i not in c:
        c.append(i)
    else:
        d.append(i)

for i in c:
    c2=0
    for j in d:
        if j == i:
            c2=c2+1
    if c2:
        print(f"{i} duplicate are {c2}")

'''
i=0
while i<len(b):
    j=i+1
    while j<len(b):
        if b[i]== b[j]:
            count+=1
            print(a[i])
        j+=1
    i+=1
    '''
