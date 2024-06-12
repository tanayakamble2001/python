# Types of Argument
# 1) Positional argument
# Ans.: During a function call , values passed through arguments should be in the order of parameters in the function definition.
##def simple_int(p,r,t):
##    print('Principle is:',p)
##    print('rate is:',r)
##    print('time is:',t)
##    si=p*r*t/100
##    print('Simple Interset is:',si)
##p=5000
##r=10
##t=5
##simple_int(p,r,t)

def simple_int(r,p,t):
    print('Principle is:',p)
    print('rate is:',r)
    print('time is:',t)
    si=p*r*t/100
    print('Simple Interset is:',si)
p=5000
r=10
t=5
simple_int(p,r,t) #value changed

# 2)Default argument
# 3) Keyword argument
# 4) Vaiable length argument
