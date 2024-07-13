#Exceptional Handeling: An Exception is an event , which occurs during the
#execution of a program, that interrupt the normal flow of the program's instructions.
#The try block which is used to test a block of code for errors.
#The except block used to handle the errors.

##print('Python Developer.')
##a=int(input('Enter the first number:'))
##b=int(input('Enter the second number:'))
##try:
##    print(a/b)
##
##except:
##    print('Exception Handled')
##print('Java Developer')

##print('Hiiii')
##a=[11,22,33,44,55]
##try:
##    print(a[len(a)])
##except:
##    print('list index out of range')
##print('Hello')

##print('Hiii')
##a=[11,22,33,44,55]
##try:
##    print(a[len(a)])
##except Exception as e:
##    print(e)
##print('Hello')


##try:
##    print('Thane')
##    print(2/0)
##    print(int('demo'))
##    print('Dadar')
##
##except ZeroDivisionError as e:
##    print(e)
##
##except ValueError as v:
##    print('Value Error:',v)
##
##except Exception as e:
##    print('Exception Handeled:',e)
##
##except:
##    print('Exception Handeled.')  #Default except must be last.

k=[]
try:
    print(k[2])
    print('Thane')
    try:
        print(9/0)
    except Exception as e:
        print(e)
    print('Mumbai')
    try:
        print(abc)
    except Exception as e:
        print(e)

except:
    print('Outer exception handeled')

else:
    print('It will execute only when exception is not occured')

finally:
    print('It always be executd')
