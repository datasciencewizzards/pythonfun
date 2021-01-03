########################################Lists########################################
# checkout complete list of list methods : https://www.w3schools.com/python/python_lists_methods.asp
#####################################################################################

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

fruits.insert(1, "lemon")
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
x = list(("apple", "banana", "cherry"))

print(x)

# List accessing
x = list(("Hello, World!", "banana", "cherry"))
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

x = ["apple", "banana", "cherry"]
x.insert(2, "watermelon")
print(x)

# To add an item to the end of the list, use the append() method:
x = ["apple", "banana", "cherry", "watermelon"]
x.append("watermelon")
print(x)

x = ["apple", "banana", "cherry", "watermelon"]
y = ["apple1", "banana1", "cherry1", "watermelon1"]

x.extend("watermelon")
print(x)

# Remove
x = ["apple", "banana", "cherry"]
x.remove("banana")
print(x)

# The pop() method removes the specified index.
x = ["apple", "banana", "cherry"]
x.pop(1)
print(x)
x.pop()
print (x)

# The del keyword also removes the specified index:
x = ["apple", "banana", "cherry"]
del x[0]
print(x)
# Removes the complete list too
del x

x = ["apple", "banana", "cherry"]

print (x)

# Loop Lists
x = ["apple", "banana", "cherry"]
for v in x:
    print(v)

# Loop lists with index
x = ["apple", "banana", "cherry"]
for i in range(len(x)):
    print(x[i])

# Using a while loop
x = ["apple", "banana", "cherry"]
i = 0
while i < len(x):
    print(x[i])
    i = i + 1

# Using list comprehension : Short syntax
thislist = ["apple", "banana", "cherry"]
# Python 3
# [print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Example 2
OneTo20 = [x for x in range(20)]

print (OneTo20)

OneTo20 = [x for x in range(20) if x < 5]

print (OneTo20)

# Example 3
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits if "a" in x]

print(newlist)

# Example 4 : replaces banana with orange
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]

print (newlist)

# Sorting - Asc
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits.sort()
print (fruits)

# Sorting - Desc
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits.sort(reverse=True)
print (fruits)


# Custom Sorting
def sortStrategy(n):
    return abs(n - 50)


noList = [100, 50, 65, 82, 23]
noList.sort(key=sortStrategy)
print(noList)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits.sort(key=str.lower)
print(noList)

# List Reverse
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits.reverse()
print(noList)

# Making a copy of list by reference will change all the
# instances. To make a detached copy , copy function should
# be used.
x = ["apple", "banana", "cherry", "kiwi", "mango"]
y = x
x[1] = "strawberry"
print(x)
print(y)

# Interpreter 2.x no copy method in list
x = ["apple", "banana", "cherry", "kiwi", "mango"]
# y = x.copy()
y = list(x)
x[1] = "strawberry"
print(x)
print(y)

###################Joining Lists############
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Using extend method
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
