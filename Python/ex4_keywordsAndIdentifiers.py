# True False
print(5 == 5)
print(5 > 5)
print("\n")

# None 
print(None == 0)
print(None == False)
print(None == [])
print(None == None)
print("\n")

def a_void_function():
    a = 1
    b = 2
    c = a + b
    # return(c)
x=a_void_function()
print(x)
print("\n")

# and, or, not
print(True and False)
print(True or False)
print(not False)
print(True and True)
print(True or True)
print(not True)
print("\n")

# as
import math as myMath  
# math module has been renamed to myMath and myMath will be used for the operations
print(myMath.cos(myMath.pi))
print("\n")


# assert
assert 5 > 4
assert 5 == 5

# break
for i in range(1, 11):
    if(i==5):
        break
    print(i)
    print("\n")

# continue
    for i in range(1, 8):
        if(i == 5):
            continue
        print(i)
    print("\n")
    
# class 
class ExampleClass:
    def function1(parameters):
        print("function1() executing...")
    def function2(parameters):
        print("function2() executing...")
ob1 = ExampleClass()
ob1.function1()
ob1.function2()
print("\n")

# def 
def function_name(parameters):
    pass
function_name(10)
print("\n")

# del
a = 10
print(a)
del a
# print(a) 
# as it is not defined now so it won't print and therefore gives a traceback error 
# that is the only reason why i made it into a comment
print("\n")

# if..elif..else
# note : if-elif-else must have same indentation!!
num = 2
if num == 1:
    print("One")
elif num == 2:
    print("Two")
else :
    print("Something else")
print("\n")

# try...except...raise...catch...finally
try:
    x=9
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Division cannot be performed")
finally:
# finally block will be executed forever irrespective of any error is raised or not
    print("Executed Successfully")
print("\n")

# for
for i in range(1, 10):
    print(i)
print("\n")

# from..import
import math
from math import cos
print(cos(10))

# global
globvar = 10
def read1():
    print(globvar)
def write1():
    global globvar
# globvar becomes global variable and is assigned to value 5
    globvar = 5
def write2():
    globvar = 15 
# globvar is a local variable as we have not used "global" before it! 
read1()
write1()
read1()
write2()
read1()
print("\n")


# in
a = [1, 2, 3, 4]
print(4 in a)
print(44 in a)
print(44 not in a)
# checks weather 4 is in a or not!
# checks membership 
print("\n")

# lambda
a = lambda x: x*2
for i in range(1, 6):
# i ranges from 1 to 5 only , 6 is excluded
    print(i, a(i))
print("\n")

# nonlocal
def outer_function():
    a = 5
    def inner_function():
        nonlocal a
        a = 10
        print("Inner Function:", a)
    inner_function()
    print("Outer function", a)

outer_function()
print("\n")


# pass
def function(args):
    pass
# Have no outcomes
# Its a placeHolder

# return 
def func_return():
    a=10
    return a
print(func_return())
print("\n")

# while
i = 5
while(i > 0):
    print(i)
    i -= 1

# with 
with open('example.txt', 'w') as my_file:
    my_file.write('Hello World!')
print("\n")


# yield
def generator():
    for i in range(6):
         yield i*i


g=generator()
for i in g:
    print(i)

    