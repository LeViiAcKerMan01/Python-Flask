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




    