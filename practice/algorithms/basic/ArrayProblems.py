# Array
arr = [1 , 2 , 3]

print(type(arr))

# Sum of the array elements
from functools import reduce

sumOfArray = reduce(lambda a , b: a + b , arr)

print(sumOfArray)

# find an element in the list
sumOfArray = reduce(lambda a , b: a + b , arr)

# find an element in the array
val = 4
for x in arr:
    if (val == x):
        print(str(x) + " exists in the list")
    else:
        print(str(x) + " does not exist in the list")
