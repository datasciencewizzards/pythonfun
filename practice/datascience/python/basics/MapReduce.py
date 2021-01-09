# List filter
myList = [1,2,3,4,5,6]
newList = list(filter(lambda a:a%2==1,myList))
print(newList)

# map(func, iterables)

myList = [1,2,3,4,5,6]

# List Constructor
p = list(map(lambda a:a%2==0,myList))
print(p)

# reduce(func, sequence)
# import is required for the reduce

from functools import reduce

myList = [1,2,3,4,5,6]
result = reduce(lambda a,b:a+b,myList)
print(result)

####################### Solve Algeraic Expressions ###

# Lambda for Algebraic Expression

squared = lambda a: a**2

print(squared(10))

 

