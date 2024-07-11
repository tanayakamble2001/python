#Polymorphism
#Polymorphism means many form
#An entity can work in a multiple role, this capability is called as polymorphism.

#Types of Polymorphism:
#1)Function Overriding  2)Function overloading

#1]Function Overriding:
#In function overriding we can declare a function in a base class and derived class with the same name and same parameter
#it occures when one class is inherit from another class (inheritance)
##class A:
##    def display(self):
##        print("Python developer")
##
##class B(A):
##    def display(self):
##        print("Java developer")
##
##ob=B()
##ob.display()
##a=A()
##a.display()

#2] Function Overloading:
#More than one function  with the same name defined in same class and call with different parameter
#this process is known as method overloading.
#but Python does not support method overloading.

##class A:
##    def show(self,x):
##        print("Hii")
##    def show(self,x,y):
##        print("Bye")
##    def show(self):
##        ptint("Hello")
##
##a=A()
###a.show()
###a.show(10)
###a.show(10,30)

##class A:
##    def show(self,x,y):
##        print(x+y)
##
##a=A()
##a.show(10,30)

##class A:
##    def show(self,x=90,y=100):
##        print(x+y)
##
##a=A()
##a.show(10,30)

##class A:
##    def show(self,x=None,y=None):
##        print(x+y)
##
##a=A()
##a.show(10,30)

##class A:
##    def show(self,a=None,b=None,c=None):
##        if (a!=None and b!=None and c!=None):
##            print(a+b+c)
##        elif(a!=None and b!=None):
##            print(a+b)
##        else:
##            print(a)
##
##x=A()
###x.show(10)
###x.show(2,3)
##x.show(10,20,30)

