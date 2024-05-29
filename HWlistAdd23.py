a=[1,5,105,15,10,7,8,90]
b=[]
#prime numbers
for i in a:
    for j in range(2,106,1):
        if i%j == 0:
            break
        else:
            b.append(i)
            break
print(b)
# add 2 in each number
j=[]
for i in a:
    i=i+2
    j.append(i)
print(j)
    

