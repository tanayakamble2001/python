#Constructor: __init__ method runs automatically when object is created
#Which is used to initialize the instance object

##class A:
##    def __init__(s):
##        print("Rudra")
##        s.id=10
##        s.name='Rajesh'
##        s.salary=70000
##
##    def display(s):
##        print('Id is ',s.id)
##        print('Name is ',s.name)
##        print('Salary is ',s.salary)
##
##a=A()
##a.display()

#User input
##class A:
##    def __init__(s):
##        s.id=int(input("Enter id:"))
##        s.name=input("Enter Your name:")
##        s.salary=int(input("Enter Salary:"))
##
##    def display(s):
##        print(f"Id is {s.id}, Name is {s.name}, Salary is {s.salary}.")
##        print("Name is ",s.name)
##        print("Salary is ",s.salary)
##
##a=A()
##a.display()

#Passsing argument to parameter
##class A:
##    def __init__(s,name,age,salary):
##        s.name=name
##        s.age=age
##        s.salary=salary
##
##    def display(s):
##        print(s.name,s.age,s.salary)
##
##a=A('ABCDE',21,50000)
##a.display()

##class A:
##    def __init__(s,name,age,salary):
##        s.name=name
##        s.age=age
##        s.salary=salary
##    def display(s):
##        print(s.name,s.age,s.salary)
##
##    def __str__(s):  #str runs when object is printed
##        return s.name+' '+str(s.age)+' '+str(s.salary)
##
##a=A('rajesh',21,70000)
##a.display()
##print(a)

#Call one method into another
##class A:
##    def display(s,name,age):
##        s.email='r@gmail.com'
##        print(name,age,s.email)
##        print("Python Developer")
##
##    def show(s):
##        print(s.email)
##        s.display('Raj',31)
##        print("Java Developer")
##
##    def demo(k):
##        print(k.email)
##        print(a.email)
##a=A()
##a.display('Janvi',21)
##a.show()
##a.demo()

#Destructor
#Destructor is a member method of a class
#It delete the memory of object
#It can be call with the object
#Name is __del__
#Garbage Collector:
#A program to delete reference
#It runs automatically
#It does memory management

##class A:
##    def __init__(self):
##        self.name='rajesh'
##        print('Python Developer')
##
##    def show(self):
##        print('Java Developer')
##
##    def __del__(self):
##        print('Object Deleted')
##
##a=A()
##a.show()
##del a
##c=A()
##c.show()
