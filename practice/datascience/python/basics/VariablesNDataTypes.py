##############################################
# Variables names are camel case : printNames
##############################################
def printname(name="World!!"):
    print ("Hello "+name)


printname("Vineet")
printname("World!!")
##################################

def compare(x, y):
    if x > y:
        print ("x is greater than y")
    elif x == y:
        print ("x and y are equal")
    else:
        print ("y is greater than x")


# if else elseif
compare(10, 11)
compare(20, 12)
# How 'abc' > 1,2,3 ?
compare('abc', [1,2,3])
#########################################
def printtype(x):
    print (type(x))


# Data Types and data types
printtype("Hello")
printtype(1.3)
printtype(1)
printtype('a')
printtype('abc')
printtype([1,2,3])
printtype([[1,2],[2,3]])
#########################################
# Variables types checking.
print(isinstance(1,int)) # This returns True
#########################################
# Variables Casting

val = 3
x = str(val)    # x will be '3'
y = int(val)    # y will be 3
z = float(val)  # z will be 3.0

printtype(x)
printtype(y)
printtype(z)
#########################################
# Multi values assignments
x,y,z = 1, "One" , 1.0
printtype(x)
printtype(y)
printtype(z)
#########################################
# Un-Pack values
fruits = ["apple","banana",1]
x,y,z = fruits
printtype(x)
printtype(y)
printtype(z)
#########################################
# local vs global variable
x = "Me , global variable"

def printLocalX():
    x = "Me , local variable"
    print (x)

def printGlobalX():
    print (x)

def globalInsideFunction():
    global y
    y = "Me, global defined inside a local"

def printGlobalY():
    print(y)

printLocalX()
printGlobalX()
globalInsideFunction()
# if you comment line globalInsideFunction() , pringGlobalY() will print banana
printGlobalY()
#########################################
            # DataTypes
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview

x = "Hello World"	#str
printtype(x)
x = 20	            #int
printtype(x)
x = 20.5	        #float
x = 35e3
x = 12E4
x = -87.7e100
printtype(x)
x = 3+1j	            #complex
printtype(x)
x = ["apple", "banana", "cherry"]	#list
printtype(x)
x = ("apple", "banana", "cherry")	#tuple
printtype(x)
x = range(6)	    #range
printtype(x)
x = {"name" : "John", "age" : 36}	#dict
printtype(x)
x = {"apple", "banana", "cherry"}	#set
printtype(x)
x = frozenset({"apple", "banana", "cherry"})	#frozenset
printtype(x)
x = True	                        #bool
printtype(x)
x = b"Hello"	                    #bytes
printtype(x)
x = bytearray(5)	                #bytearray
printtype(x)
x = memoryview(bytes(5))	        #memoryview
printtype(x)

#########################################
# List vs tuple : ListOperations.py
#########################################

