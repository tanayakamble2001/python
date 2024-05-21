n= 93084
num = n
l=len(str(n))
sum=0
while n!=0:
    r=n%10
    sum=sum+r**l
    n=n//10
if num == sum:
    print(num,"This is an Armstrong Number")
else:
    print(num,"This is not an Armstrong Number")
