#Inheritance
#One class can inherit the properties and method of another class this process is know as inheritace.
##class A:
##    a=10
##    def show(s):
##        print("python developer")
##
##class B(A):
##    b=20
##
##    def display(s):
##        print(s.b,c.b,c.a,B.a,B.b)
##
##        print('java developer')
###a=A()
###a.show()
##
##c=B()
##c.display()
###c.show()


#Types of inheritance:
#1) Single level inheritance
#2) Multilevel inheritance
#3) Hirarchical inheritance
#4) Multiple inheritance
#5) Hybrid inheritance

#2) The inheritance in which a class can be derived from another class is known as multilevel inheritance.
##class A:
##    a=10
##    def show(s):
##        print('Grand parent method called.')
##
##class B(A):
##    b=20
##    def display(s):
##        print("Parent method called.")
##
##class C(B):
##    c=30
##    def data(s):
##        print(s.a+s.b+s.c)
##        print("Childe method called.")
##
##x=C()
###print(x.c)
##x.data()
##x.display()
##x.show()

class Engineer:
    def study(s):
        print("Engineer study method called.")

    def show(s):
        print("Engineer show method called.")

class Doctor:
    def study(s):
        print("Doctor study method called.")

    def display(s):
        print("Doctor display method called.")

class student(Engineer,Doctor):
    def demo(s):
        print("Pharmacis")

s=student()
s.demo()
s.display()
