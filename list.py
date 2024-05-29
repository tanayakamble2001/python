#Creating list with Constructor method

a=list((1,2,'abc','xyz'))
print(a)
print(type(a))
print(len(a))


b=['xyz','abc',123,44,55]
print(b)
print(type(b))
print(len(b))

'''
c=['Robert','Anuj','Mishraji','Saud','Jadhav','Nair']
for i in c:
    if i[-1]=='i':
        print(i)

for i in c:
    if 'r' in i:
        print(i)

for i in c:
    for j in i:
        if j == 'r':
            print(i)
            break

i=0
while i<len(c):
    j=0
    while j<len(c[i]):
        if c[i][j]=='r':
            print(c[i])
            break
        j+=1
    i+=1
'''

c=['Robert','Anuj','Mishraji','Saud','Jadhav','Nair']
#Count Vowels in the list
for i in c:
    count=0
    for j in i.lower():
        
        if j in 'aeiou':
            count=count+1
            
    print(i,'=',count)

for i in c:
    count=""
    for j in i.lower():
        if j in 'aeiou':
            count=count+j
    print(i," this name contain ",len(count),'vowels',count)

i=0
while i<len(c):
    j=0
    count=0
    while j<len(c[i]):
        if c[i][j] in 'aeiou':
            count=count+1
        j+=1
    print(f"{c[i]} this name contains {count} vowels")
    i+=1
#Print the name whose length is 4
i=0
while i<len(c):
    j=0
    while j<len(c[i]):
        if len(c[i])==4:
            print(c[i])
            break
        j+=1
    i+=1

for i in c:
    for j in c:
        if len(i) == 4:
            print(i)
            break

for i in c:
    if len(i) == 4:
        print(i)
        
