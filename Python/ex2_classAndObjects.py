class MyComplexNumber:
    # constructor methods
    def __init__(self, real=0,imag=0):
        print("My computer constructor executing...")
        self.real_part = real
        self.imag_part = imag

        def displayComplex(self):
            print("{0} + {1}j".format(self.real_part,self.imag_part))


        # Create a new object against MyComplexNumber class 
            cmp1x1 = MyComplexNumber(40,50)

            # Calling displayComplex() function
            # Output: 40+50j
            cmp1x1.displayComplex()

            # Create another object against MyComplexNumber class 
            # and create a new attribute 'new_attribute'
            cmp1x2 = MyComplexNumber(60, 70)
            cmp1x2.new_attribute = 80
            cmp1x2.displayComplex()
            # Output: (60, 70, 80)
            print((cmp1x2.real_part, cmp1x2.imag_part, cmp1x2.new_attribute))

            # but cmp1x1 object doesn't have attribute 'new_attribute'
            # AttributeError: 'MyComplexNumber' object has no attribute 'new_attribute'
            cmp1x1.new_attribute


            # Deleting object attributes and the object
            print(cmp1x1)
            del cmp1x1.real_part
            del cmp1x1

            print(cmp1x1)