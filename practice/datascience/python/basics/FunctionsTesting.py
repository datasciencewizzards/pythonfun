# Arbitrary number of arguments

def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# You can also send arguments with the key = value syntax.
#
# This way the order of the arguments does not matter.

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


# If you do not know how many keyword arguments that will be passed
# into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments,
# and can access the items accordingly:

def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:

def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# To let a function return a value, use the return statement:
def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))