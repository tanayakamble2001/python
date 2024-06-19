##Recursion: when a function call itself, then that function is called
##as recursive function and the process is called as recursion

##def demo():
##    print("ABCD")
##    demo()
##demo()

#import sys

#print(sys.getrecursionlimit())
##sys.setrecursionlimit(200)
##print(sys.getrecursionlimit())
##
##i=0
##def demo():
##    global i
##    i=i+1
##    print("ABCD",i)
##    demo()
##demo()

#Advantage:
##1)clean code/less number of code
##2) complex problem can be solved

#Disadvantage:
##1) hard to debug
##2) not memory efficient

#WAP for fibbonacci series using recursion
#0,1,1,2,3,5,.......

##fibo(1)=0
##fibo(2)=1
##fibo(3)=fibbo(1)+fibbo(2)
##fibo(4)=fibbo(3-2)+fibbo(3-1)
##fibo(n)=fibbo(n-2)+fibbo(n-1)

##def fibo(n):
##    if n==1:
##        return 0
##    if n==2:
##        return 1
##    return fibo(n-2)+fibo(n-1)
##n=int(input("Enter the number of terms:"))
##print(fibo(n))
