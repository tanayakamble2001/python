#append
a=[1,2,3,'abc','xyz']
a.append("Added")
print(a)

#extend
a=[1,2]
b=[3,4]
a.extend(b)
b.extend(a)
print(b)

#insert
a=[1,2,3,4]
a.insert(0,100) #insert(index,value)
a.insert(0,100)
a.insert(2,300)
a.insert(2,400)
print(a)

#replace value using index
a=['abc',100,200]
a[1]='tanaya'
print(a)

#delete values using pop and remove
a=[1,2,3,4,'abc','yyyyy',4]
a.pop() #delete last value from list
a.remove('abc') #delete particular value
print(a)

#delete
a=[1,2,3,4,4]
#del a # delete whole list
del a[0] #delete particular value using index
print(a)

#clear
a=[1,2,3,4,5,6,7,8]
a.clear() #delete all element and reset the list
print(a)

#count
ab=[1,2,3,3,3]
print(ab.count(3)) #count duplicate values

#index
print(ab.index(3)) #display index number
ab.reverse()  # reverse the list
print(ab)
