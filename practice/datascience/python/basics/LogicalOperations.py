# Operator	Description	Example	Try it
# and 	Returns True if both statements are true	x < 5 and  x < 10
# or	Returns True if one of the statements is true	x < 5 or x < 4
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

x = 100
print (not(x < 5 and x < 10))

# Operator	Description	Example	Try it
# is 	Returns True if both variables are the same object	x is y
# is not	Returns True if both variables are not the same object	x is not y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference between "is" and "==": this comparison returns True because x is equal to y

##########################################################
# Membership operators
# Operator	Description	Example	Try it
# in 	Returns True if a sequence with the specified value is present in the object	x in y
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y
##########################################################
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

print("banana" not in x)

# returns False because a sequence with the value "banana" is in the list

####################### BitWise Operators ###################################
# Operator	Name	Description
# & 	AND	Sets each bit to 1 if both bits are 1
# |	OR	Sets each bit to 1 if one of two bits is 1
#  ^	XOR	Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT	Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left,
#       and let the rightmost bits fall off
####################### BitWise Operators ###################################

