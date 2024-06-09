import random
a={'aa','xyz','pqr'}
print(type(a))
a.add('tanaya')
a.update({"pravara",'anvi'})
print(a)
a.pop()
print(a)

for i in a:
    print(i)

#genrate otp
o={'1','2','3','4','5','6','7','8','9','0'}
c=""
#print(type(p))
for i in o:
    c = c+i
print(f"OTP: {c[:4:]}")#slicing

