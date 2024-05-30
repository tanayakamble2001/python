a={'name':'ABC',0:'Kuch bhi','age':78,'name':'pqrs'}
print(a)
print(len(a))
print(type(a))

a['age']=20
a['city']='thane'
#a['name']='tanaya'
print(a)

for i in a:
    print(f"{i}={a[i]}")
for i in a:
    print(i)
