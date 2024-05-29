a=['Robert','Anuj','Mishraji','Saud','Jadhav','Nair','More']
b=[]

for i in a:
    for j in i.lower():
        if j == 'r':
            b.append(i)
            break
print(b)
'''
c=""      
for i in a:
    if 'r' in i.lower():
        c=a[i]
        print(list(c))
'''  
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i][j]=='r':
            b=list(a[i])
            print(b,end=" ")
            break
        j+=1
    i+=1

