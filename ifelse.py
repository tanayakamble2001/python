if 1==1:
    print(True)
else:
    print(False)

a=12
b=1
c=15
if a>b and a>c:
    print(a,"is greater")
elif b>a and b>c:
    print(b,"is greater")
else:
    print(c,"is greater")


#datatype OR User input

#a=input("Enter Your name:")
#b=int(input("Enter Your Age:"))
#print(type(a),type(b))

a=1.2
print(type(int(a)))
print(int(a))
c= 2+3j
print(type(c))
ab= 11
print(float(ab))

ac={1,2,3,4,5}
print(type(ac))
print(list(ac))

#addition of two numbers

n1=int(input("Enter a number1:"))
n2=int(input("Enter a number2:"))
print("Addition of n1 and n2=",n1+n2)

