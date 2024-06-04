a={'name':'abc','age':30,'city':'thane'}
print(a['name'])
print(a.get('name'))  #display name using method
print(a.get('age'))

a['phone']=1123456789  
a.update({'tel':234567}) #enter/insert key value pairs

a.pop('name') #delete particular key from variable
a.popitem() #delete last key values
#a.clear() "clear all keys & values from varible and reset the dictionary"
del a['age'] #delete particular key
print(a)

