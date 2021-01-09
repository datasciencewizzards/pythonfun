# A lambda function is a small anonymous function.
#
# A lambda function can take any number of arguments, but can only have one expression.

# No argument lambda

x = lambda : print ("Hello lambda World!")
x()

# Single argument Lamda
x = lambda a : a + 10
print(x(5))

# Multi argument lambda

x = lambda a,b,c : print (a+"$$$",b+"$$$",c+"$$$")

x(5,10,15)

# lambda with list as argument

x = lambda list : print(list)

# map with lambda

myList = [10, 25, 17, 9, 30, -5]
# Double the value of each element
myList2 = map(lambda n : n*2, myList)

print (myList2)

myList = [10, 25, 17, 9, 30, -5]
# Filters the elements which are not multiples of 5
myList2 = filter(lambda n : n%5 == 0, myList)
print (myList2)

