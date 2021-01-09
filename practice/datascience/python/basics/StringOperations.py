#########################################
# String operations
# String operations complete reference : https://www.w3schools.com/python/python_ref_string.asp
x = "Hello World!!"
print (x[1])

# Looping String
def printAllchars(x):
    for c in x:
        print (c)


printAllchars("banana")

# String length
print("banana length "+str(len("banana")))

# Presence of text in a string. bool
x = "The best things in life are free!"
print("free" in x)
# No Presence of text in a string. bool : not in
print("expensive" not in x)

########################################
# Slicing Strings
# Get the characters from position 2 to position 5 (not included):
x = "Hello, World!"
print(x[5:2])

# Get the characters from the start to position 5 (not included):
print(x[:5])

# Get the characters from position 2, and all the way to the end:
print(x[2:])

# Use negative indexes to start the slice from the end of the string:
# -5 inclusive -2 exclusive
print(x[-5:-2])

# UpperCase
x = "Hello, World!"
print(x.upper())

# LowerCase
print(x.upper().lower())

# Remove whitespaces
x = "   Hello, World!  "
print (x.strip())

# Replace
print (x.replace("Hello","JXXX"))

# Split returns ['Hello', ' World!']
x = "Hello, World!"
print (x.split(","))

# String and int can't be added
# String formatting
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
# More sophosticated formatting
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Formatting with named indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

# Escape characters : https://www.w3schools.com/python/python_strings_escape.asp
# Print with quotes
txt = "We are the so-called \"Vikings\" from the north."
print(txt)