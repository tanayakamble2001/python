#class is a collection of an objects.
#Class is a blueprint of an object.
#Class is a blueprint that defines some properties and behaviors. An
#object is an instance of a class that has those properties and
#behaviours attached. A class is not allocated memory when it is
#defined. An object is allocated memory when it is created. Class is a
#logical entity whereas objects are physical entities.


##a=10
##print(type(a))
##
##b=20
##print(type(b))
##
##c='abcd'
##print(type(c))

#class str   [inbuild class]
#class student  [user defined class]

##class student:
##    name='abcde'  #static variables ,class variables
##    email='abc@gmail.com'
##    roll_no=121
##s=student
##print(s.name)
##print(s.email)
##print(s.roll_no)

##class student:
##    name='abcde'
##    email='abc@gmail.com'
##    roll_no=121
##    def demo(s):
##        name='abcd'
##        print(name)
##s=student()
##s.demo()

##class student:
##    name='abcde'
##    email='abc@gmail.com'
##    roll_no=121
##
##    def demo(self):         #self is default parameter that represent instance of class
##        name='ABCD'
##        print(name)
##s=student()
###s.demo()
##k=student()
##k.demo()
##
##m=student()
##m.demo()

##class A:
##    def demo(self,department):
##        print(department)
##        print(self)
##        name='ABCDE'
##        age=21
##        roll_no=123
##        print(name,age,roll_no)
##
##    def display(self):
##        email='abc@gmail.com'
##        address='thane'
##        print(email,address)
##a=A()
###a.demo()
###print(a)
###a.display()
###A.demo('k')
##a.demo('mech')

##class student:
##    def show(self,name,roll_no):
##        print('My name is ',name)
##        print("roll number is ",roll_no)
##        print("pyhton developer")
##    def display(self):
##        print("java developer")
##s=student()
##s.show('ABCDE',123)
##s.display()

##class student:
##    name='ABCD'
##    email='abc@gmail.com'
##    def show(self):
##        print(self.name,self.email)
##        print('python developer')
##    def display(self):
##        print(self.name)
##        print('java developer')
##a=student()
##print(a.name)
##a.show()
##
##a.display()

#Local variable
##class A:
##    def show(self,roll_no,dep_name):
##        print(roll_no,dep_name)
##        name='ABCD'
##        age=31
##        print(name,age)
##
##    def display(self):
##        print(dep_name)
##        email='abc@gmail.com'
##        branch='ExTC'
##        print(name)
##        print(email,branch)
##
##a=A()
##a.show(123,'Mech')
###print(a.name)
##a.display()


#Instant Variable
##class A:
##    def show(self,name,age,salary):
##        a.name1=name
##        self.age1=age
##        self.salary1=salary
##        print(a.name1,self.age1,self.salary1)
##
##    def display(self):
##        print(a.name1,self.age1,self.salary1)
##
##a=A()
##a.show('ABCDE',31,70000)
##a.display()

#Static Variable
##class A:
##    dep_name='Mech'
##    print(dep_name)
##    def show(self,name,age,salary):
##        a.name1=name
##        self.age1=age
##        self.salary1=salary
##        print(a.name1,self.age1,self.salary1,a.dep_name)
##
##    def display(self):
##        print(a.name1,self.age1,self.salary1)
##
##a=A()
##a.show('ABCDE',31,70000)
##a.display()
##print(a.dep_name)

#User input
##class A:
##    def show(self):
##        self.name=input('Enter your name:')
##        self.age=int(input('Enter your age:'))
##        self.salary=int(input('Enter your salary:'))
##
##    def display(self):
##        print('My name is ',self.name)
##        print('My age is ',self.age)
##        print('Salary is ',self.salary)
##
##a=A()
##a.show()
##a.display()

#call one method into another
##class A:
##    def show(self,name,address):
##        print('Python Developer')
##
##    def display(self):
##        self.show('Vihan','Pune')
##        a.show('Gauri','itvedant')
##        print('Java Developer')
##
##a=A()
##a.show('rajesh','thane')
##a.display()

##class A:
##    a=10
##    b=20
##    def demo(s):
##        s.a=s.a+1
##        A.b=A.b+1   #class name effect on static variable
##        print(s.a,A.b)
##
##x=A()
##x.demo()
##
##y=A()
##y.demo()
##
##z=A()
##z.demo()
