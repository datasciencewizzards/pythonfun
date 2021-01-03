
# List items are ordered, changeable, and allow duplicate values.
# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#
# If you add new items to a list, the new items will be placed at the end of the list.
#
# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
#
# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:

fruits = ["apple", "banana", "cherry"]

print(fruits)

fruits.append("orange")

print(fruits)

# Replacement
fruits[1] = "chickoo"
print(fruits)

fruits.insert(1,"lemon")
print(fruits)

# Remove
fruits.remove("lemon")
print(fruits)

# Print last item in the list
print(fruits[-1])

# Print length of the list
print(len(fruits))

# List with mixed values
x = ["abc", 34, True, 40, "male"]
print(x)

# list constructor
x = list(("apple","banana","cherry"))

print(x)

# List accessing
x = list(("Hello, World!","banana","cherry"))
print(x[1])
# Negative index
print (x[-1])
# Range
print (x[0][2:5])

# All from Start and i(excluding)
print (x[:2])


# All from i(including) and till End
print (x[1:])

# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
x = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(x[-4:-1])

# Check if "apple" is present in the list:
x = ["apple", "banana", "cherry"]
if "apple" in x:
  print("Yes, 'apple' is in the fruits list")

##########################List Mutations###########
# How to replace, add , delete to a list
##########################List Mutations###########

# Replace banana with blackcurrant
x = ["apple", "banana", "cherry"]
x[1] = "blackcurrant"
print(x)
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon": Excluding 3
#       0       1           2       3           4       5
x = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(x)
x[1:3] = ["blackcurrant", "watermelon"]
print(x)

# Replace and insert
x = ["apple", "banana", "cherry"]
x[1:2] = ["blackcurrant", "watermelon"]
print(x)

# The insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# To add an item to the end of the list, use the append() method:
