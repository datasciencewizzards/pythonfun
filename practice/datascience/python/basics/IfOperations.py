# If syntax
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Shorthand syntax for the above

a = 200
b = 33
print("A") if a > b else print("=") if a == b else print("B")

# and operator

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# or operator
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

