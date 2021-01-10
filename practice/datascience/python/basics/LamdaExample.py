# definition less functions
# Syntax
# lambda arguments : expression

x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 6))

# A lambda function is a small anonymous function.
#
# A lambda function can take any number of arguments, but can only have one expression.

# No argument lambda

x = lambda: print("Hello lambda World!")
x()

# Single argument Lamda
x = lambda a: a + 10
print(x(5))

# Multi argument lambda

x = lambda a, b, c: print(str(a) + "$$$", str(b) + "$$$", str(c) + "$$$")

x(5, 10, 15)

# lambda with list as argument

x = lambda list: print(list)

# map with lambda

myList = [10, 25, 17, 9, 30, -5]
# Double the value of each element
myList2 = map(lambda n: n * 2, myList)

print(myList2)

myList = [10, 25, 17, 9, 30, -5]
# Filters the elements which are not multiples of 5
myList2 = filter(lambda n: n % 5 == 0, myList)
print(myList2)


# Function returning lambda

def power(n):
    return lambda a: a ** n


print("{%d}th Power of {%d} is :: {%d}" %(2,5, power(2)(5)))

print("{}th Power of {} is :: {}".format(2,5, power(2)(5)))

