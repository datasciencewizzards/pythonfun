# A set is a collection which is both unordered and unindexed.

thisset = {"apple", "banana", "cherry"}
# Every run will print a different order
print(thisset)

# Can hold mixed values
set1 = {"abc", 34, True, 40, "male"}

# Set definition with a constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Accessing set elements
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Check the presence
thisset = {"apple", "banana", "cherry"}

if("banana" in thisset):
    print("banana")

# Once a set is created , we can't change the items but we can add a new one
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Any iterable can be added
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
mylist = ["kiwi", "orange"]

thisset.update(tropical)
thisset.update(mylist)

print(thisset)

# Remove item : raises an error if the key doesn't exist
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# discard item : doesn't raise an error if the key doesn't exist
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# Removes the last item
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# clear the list
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# Looping a set
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Join 2 sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3, "a"}

set3 = set1.union(set2)
print(set3)

# insert one set to another
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3 ,"a"}

set1.update(set2)
print(set1)

# Sets intersection
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# Return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

# Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

# Return a set that contains all items from both sets, except items that are present in both:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
