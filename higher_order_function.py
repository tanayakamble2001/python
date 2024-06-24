#Higher oreder Function
# A function which takes another fuunction as argument is called as higher order function.

#Built in higher order function:
##1) filter function
##2) map funciton
##3) reduce function

##1)Filter Function: filter function filter out element of iterable
##filter function return filter object.
##Syntax:
##    filter(funct_name,iterable)
##    1)funct_name: function that test every element of iterable
##    2)iterable: sequence  which need to be filtered


##number=[11,22,33,44,55,66]
##
##def even_fun(x):
##    if x%2 == 0:
##        return True
##
##filter_object=filter(even_fun,number)
##print(filter_object) #location
##print(list(filter_object))
##print(tuple(filter_object))

##number=[11,22,33,44,55,66]
##
##def even_fun(x):
##    if x%2==0:
##        return True
##filter_object=list(filter(even_fun,number))
##print(filter_object)
##print(filter_object)

#prime Number
##num=[2,55,13,15,20,97]
##def prime_num(x):
##        for j in range(2,101,1):
##            if x%j==0:
##                break;
##        if x==j:
##            return True
##prime=list(filter(prime_num,num))
##print(prime)


#map function: this is also higher order function. It apply specific function on each element of iterable and perhaps change element
##Syntax:
##map(function_name,iterable)
##n=[1,2,3,4,5,6]
##def square(x):
##    return x*x
##y=list(map(square,n))
##print(y)

num=[1,2,3,4,5,6]
def factorial(x):
    i=1
    fact=1
    while i<=x:
        fact=fact*i
        i+=1
    return fact
y=list(map(factorial,num))
print(y)
