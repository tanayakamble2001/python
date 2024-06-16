#import math as m
#print(m.sqrt(4))
#print(m.factorial(5))
#print(m.pow(2,3))
#print(m.floor(15.9)) #round down number 15
#print(m.ceil(15.2))  #round up number 16
#print(m.floor(-15.9))  #round down number -16
#print(m.ceil(-15.2)) #round up number -15


import random as r
#print(r.random()) #===>return float values include<--[0,1)-->exclude
#print(r.randrange(1,4)) #[a,b)
#print(r.randrange(1,6,2))
#print(r.randrange(20))
#print(r.randrange(2,8,2))
#print(r.randrange(2))
#print(r.randrange(2,6))
#print(r.randrange(6,2)) #error

#randint include upper value
#print(r.randint(2,5)) # print 2 to 5
#print(r.randint(6,2)) #error
#print(r.randint(6,6)) #6
#print(r.uniform(2,5)) # float value between range
'''
l=[11,22,33,44,'ABC']
print(r.choice(l))  #choice
'''

'''
l=['karan_arjun','Big_Boss','sholey']
r.shuffle(l)
print(l)  #shuffle in list
'''

'''
s='python_programming'
print(s[-15:-16])
print(s[2:3:-1])
'''




