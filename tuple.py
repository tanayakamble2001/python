a=(1,2,3,'abc','xyz')
print(a)
print(type(a))
print(len(a))
print(a[-1])

#a[0]="pqrs"
#print(a)

b=(1,2)
print(type(a+b))
s=(1,)
print(type(s))

data=('abcd',54,'Thane',11,222,33,44,55,66,77)
print(data)
(name,age,city,*a)=data
print(name)
print(age)
print(city)
print(a)
print(a[2])

#example
a=[1,2,3,([33,88,'abc',('yes','No','yes')])]
b=list(a[3][3])
print(a)
#b[3][3][1]='yes'
b[1]='yes'
a[3][3]=tuple(b)
print(a)
#a[3][0][0][3][1]='yes'
'''a[3][3][1]="yes"
print(a[3][3][1])
'''


#tuple sclicing
a=(1,2,3,3,4,3)
#reverse tuple
print(a[::-1])
#inbuild methods
#count the  duplicate value
print(a.count(3))
#index value display
print(a.index(1))
#iteration
a=(1,2,3,3,4,3)
#for in loop
for i in a:
    print(i)
    
#while loop
i=0
while i<len(a):
    print(a[i])
    i+=1
    
#for in range
for i in range(len(a)):
    print(a[i])
