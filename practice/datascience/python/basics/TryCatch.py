# The try block lets you test a block of code for errors.
#
# The except block lets you handle the error.
#
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

try:
    print(x)
except:
    print("An exception occurred")

# Catch specific Exception
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# Legitimate Error : try to open a file for writing which doesn't exist
try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    pass
    # f.close()


# Throwing an Exception from the program
x = -1

# Compile time Exception
if x < 0:
  raise Exception("Sorry, no numbers below zero")

# Custom Exception
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

