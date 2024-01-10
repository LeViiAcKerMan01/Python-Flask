# Defining and declaring an array 
arr = [10, 20, 30, 40, 50]
print(arr)

# Accessing Array elements
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[-1]) # Negative indexing
print(arr[-2]) # Negative indexing
# Negative indexing means indexing from the end element of an array
# -1 represents arr[4] 
# -2 represents arr[3]

brands = ["Coke", "Apple", "Google", "Microsoft", "Amazon"]
print(brands)

# Adding an element to the array using append()
brands.append("NetFlix")
print(brands)
print("\n")

# Removing elements from an array by different ways
colors = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"]
print(colors)
print("\n")

del colors[4]
print(colors)
print("\n")

colors.remove("Blue")
print(colors)
print("\n")

colors.pop(3)
print(colors)
print("\n")

# Modifying elements of an array using indexing
fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
print(fruits)
print("\n")

fruits[1] = "Pineapple"
print(fruits)
print("\n")

fruits[-1] = "Guava"
print(fruits)
print("\n")

# Concatenating two arrays using the '+' operator
concat = [1, 2, 3]
print(concat)
print("\n")

concat + [4, 5, 6]
print(concat)
print("\n")

concat = concat + [4, 5, 6]
print(concat)
print("\n")


# Repeating elements in an array
repeat = ["a"]
print(repeat)

repeat = repeat * 5
print(repeat)
print("\n")


# Slicing elements in an array 
fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
print(fruits)

print(fruits[1:4]) # also written as : [fruits[1] , fruits[4])
print(fruits[ :3]) # also written as : [fruits[0] , fruits[3])
print(fruits[-4: ]) # also written as : [fruits[-4] , fruits[4]]
print(fruits[-3:-1]) # also written as : [fruits[-3] , fruits[-1])
# Use of intervals is made in the above slicing of elements
# (a, b) , (a, b] , [a, b) , [a, b]
# where (a, b) means a < x < b
# where [a, b] means a <= x <= b

# Declaring and defining multi-dimensional arrays

multd = [[2,3], [4,5], [6,7], [8, 9]]
print(multd)
print("\n")

print(multd[0])
print(multd[3])
print(multd[2][1])
print(multd[3][0])
print(multd[2][0])





