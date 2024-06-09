#positional argument function
def data(name,age,city):
    return f"My name is {name} My age is {age} and I live in {city}"
#print(data('ABC',20,'Thane'))
#print(data('PQR',12,'Thane'))


#Key word Argument Function
def data(name,age,city):
    return f"My name is {name} My age is {age} and I live in {city}"
print(data(age=25,city='Thane',name='TUV'))
