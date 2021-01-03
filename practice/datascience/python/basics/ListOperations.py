# List is Mutable
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