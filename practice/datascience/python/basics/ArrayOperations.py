# Define Array
cars = ["Ford", "Volvo", "BMW"]

print("Length of the array {}".format(len(cars)))

# Iterating an Array
cars = ["Ford", "Volvo", "BMW"]

for car in cars:
    print("Car is cars :: {}".format(car))

# Addition of the elements append()
cars = ["Ford", "Volvo", "BMW"]
cars.append("Merce")

print("Cars after append :: {}".format(cars))

# Remove element from Array , pop() : Removal by index ,remove() : Removal by "name"
cars = ["Ford", "Volvo", "BMW"]
print("Cars before removal :: {}", cars)
cars.remove("Volvo")
print("Cars after removal :: {}", cars)


cars = ["Ford", "Volvo", "BMW"]
print("Cars before pop :: {}", cars)

# Removes the second element
cars.pop(1)
print("Cars after pop :: {}", cars)

# Sort the array
cars = ["Ford", "Volvo", "BMW"]
print("Cars before sort :: {}", cars)
cars.sort()
print("Cars after sort :: {}", cars)

# Reverse the list
cars = ["Ford", "Volvo", "BMW"]
print("Cars before reverse :: {}", cars)
cars.reverse()
print("Cars after reverse :: {}", cars)





