#Scope:

#Local Variable
'''
def display():
    a=10
    print(a)
print(a)
display()
'''

#Global Variable==> A variable is declared outside the function is called Global Variable.
'''
A=15
def display():
    a=10
    b=20
    print(a)
    print(A)
print(A)
display()
print(A)
'''

'''
A=30
def display():
    A=20
    print(A)
print(A)
display()
print(A)
'''
'''
A=30
def display():
    global A
    A=20
    print(A)
print(A)
display()
print(A)
'''


#Q1)
'''
B=30
def display(x):
    global a
    a=a+x
    return x
a=20
b=5
display(b)
print(a)
'''

#Q2)
'''
a=10
y=5
def myfun():
    a=2
    y=a
    print(y,a)
myfun()
print(y,a)
'''

#Q3)
'''
a=10
y=5
def myfun():
    y=a
    #a=2
    print(y,a)
myfun()
print(y,a)
'''

#Q4)
'''
a=10
y=5
def myfun():
    global a
    y=a
    a=2
    print(y,a)
myfun()
print(y,a)
'''

#Q5)
'''
a=10
y=5
def myfun():
    global a
    a=2
    y=a
    print(y,a)
myfun()
print(y,a)
'''

#Q6)
'''
a=1
def display():
    return a
print(a)
print(display())
print(a)
'''
