# A tuple is a collection which is ordered ,unchangeable and allows duplicates.
t = ("apple", "banana", "cherry")
print(t)

print(len(t))

# Mixed values
t = ("abc", 34, True, 40, "male")

print(t)

# Constructor

t = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(t)

# Accessing elements
t = ("apple", "banana", "cherry")
print(t[1])

# Negative index -1 : Last element, -2: Second Last element
t = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(t[-1])
# Guess the output ?
print(t[-4:-1])

# Range of elements
t = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(t[2:5])

# Wild Card indexing
# (1) From the beginning
t = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(t[:4])
# (2) From the End
t = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(t[2:])

# If an item exists "in"
t = ("apple", "banana", "cherry")
if "apple" in t:
  print("Yes, 'apple' is in the fruits tuple")

# Tuples are un-changeable but can be converted to list
x = ("apple", "banana", "cherry")
# Tuple to list conversion
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Tuples are immutable ; Can't add an item to tuple
thistuple = ("apple", "banana", "cherry")
# thistuple[1] = ("orange") # This will raise an error
print(thistuple)

# Tuples are immutable ; Can't remove an item to tuple
t = ("apple", "banana", "cherry")
# t.remove("apple") : Raises and error
y = list(thistuple)
y.remove("apple")
t = tuple(y)

print(t)

# The del keyword can delete the tuple completely:
t = ("apple", "banana", "cherry")
del t
# print(t) #this will raise an error because the tuple no longer exists

# Unpack Tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Wild card unpacking
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
# red will have cherry, strawberry , raspberry
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")


(green, *tropic, red) = fruits

print(green)
# tropic will have mango, papaya , pineapple
print(tropic)
print(red)

# Confused wildcard
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# Gives syntax error
# (green, *tropic, *red) = fruits

######################Loop###############
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

for x in fruits:
  print (x)

# While loop
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

i = 0
while (i<len(fruits)):
  print(fruits[i])
  i+=1

# Join tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply tuple
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# appends same tuple , same as fruits + fruits
mytuple = fruits * 2
print(mytuple)


