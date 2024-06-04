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

print(a.keys()) #print all keys in variable
print(a.values()) #print all values in variable
print(a.items()) #print all key values pairs in variable
for k,v in a.items():
    print(k,v)
