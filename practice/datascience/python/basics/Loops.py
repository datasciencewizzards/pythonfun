# While loop
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# Loop through a string
for x in "banana":
  print(x)

# Looping on range : 0 - 5

for x in range(6):
  print(x)

# Looping on range : 2 - 6 excluding 6

for x in range(2, 6):
  print(x)

# Looping on range : 0 - 30 excluding 30 with a jump of 3
for x in range(0, 30, 3):
  print(x)

# The else keyword in a for loop specifies a block of code to be executed
# when the loop is finished:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

