# Numpy :   Memory efficient
#           Fast
# Complete list of functions

import numpy as np

a = np.array([1 , 3 , 2] , dtype='int8')  # One integer is one byte
b = np.array([[1 , 3 , 2] , [1 , 5 , 7]])  # Default is int64

# dimensions
print("Dim(a) {}, Dim(b) {}".format(a.ndim , b.ndim))

# Shape
print("Shape(a) {}, Shape(b) {}".format(a.shape , b.shape))

# DataType
print("Type(a) {}, Type(b) {}".format(a.dtype , b.dtype))

# No of bytes per item
print("Per item Size(a) {} bytes,Per item Size(b) {}".format(a.itemsize , b.itemsize))

# Total No of bytes
print("Total item size(a) {} bytes,Total item Size(b) {} bytes".format(a.nbytes , b.nbytes))

# Change, Accessing array
a = np.array([[1 , 2 , 3 , 4 , 5 , 6 , 7]
                 , [8 , 9 , 10 , 11 , 12 , 13 , 14]])
print(a)

# Get a specific element , 2nd row 4th column
print("Specific element {}".format(a[1 , 5]))

# Get specific row , 1th row
r = -1
print("Backwards Specific row {} is {}".format(r , a[r , :]))
# Get specific row backwards, -1 first row from last(end)

# Get specific column , 1nd col
c = 2
print("Specific column {} is {}".format(c , a[: , c]))
# Get specific column , -1th col
c = -1
print("Backwards Specific column {} is {}".format(c , a[: , c]))

##############Fancy Operations############

# [startIdx:endIdx:stepSize]
# We want to get every other element in row 0 starting from 2 ending 6
print("Fancy printing {}".format(a[0 , 1:6:2]))
# Same with backwards, 6 is at -2 but use -1 as endIdx is exclusive
print("Fancy printing {}".format(a[0 , 1:-1:2]))

##############Modification Operations############
a[1 , 5] = 20
print("Modified array {}".format(a))

# Modifying multi values : Change all the values in the 5th column
a[: , 5] = 20
print("Modified array {}".format(a))

# Scale up the dimension , move from 2 to 3 dimension :: Open challenge


##############Different Matrix Initializations############

allZeros = np.zeros((2 , 3))
print("All zeros matrix {}".format(allZeros))

allOnes = np.ones((2 , 3))
print("All zeros matrix {}".format(allOnes))

allX = np.full((2 , 3) , 100)
print("All zeros matrix {}".format(allX))

b = np.array([[1 , 3 , 2] , [1 , 5 , 7]])  # Default is int64
sameAsBButDiffVal = np.full_like(b , 10)
print("All 10 and dim same as b matrix {}".format(sameAsBButDiffVal))

##############Random Samples############
randBet0to1 = np.random.random_sample(b.shape)
print("Random sample matrix between 0 to 1 of size {}".format(randBet0to1 , b.shape))

# Integer matrix with random values
# Excluding -2 inclusive 7 exclusive
randIntMatrix = np.random.randint(-2 , 7 , size=(3 , 3 , 3))
print("Random integer matrix with values from {} to {} is {}".format(0 , 7 , randIntMatrix))

# Identity Matrix
i5 = np.identity(5)
print("Identity integer matrix {}".format(i5))

# Repetitions
arr = np.array([[1 , 2 , 3]])
# Row repetitions
print("Array with repeated row items {}".format(np.repeat(arr , 3 , axis=0)))
print("Array with repeated column items {}".format(np.repeat(arr , 3 , axis=1)))

# Exercise
# 1,1,1,1,1
# 1,0,0,0,1
# 1,0,9,0,1
# 1,0,0,0,1
# 1,1,1,1,1

fiveXfiveOnes = np.ones((5 , 5))
threeXthreeZeros = np.zeros((3 , 3))
threeXthreeZeros[1 , 1] = 9
# Super Impose 9x9 onto 5x5
fiveXfiveOnes[1:4 , 1:4] = threeXthreeZeros
print("Final outcome {}".format(fiveXfiveOnes))

# Copy by values
a = np.ones((3 , 2))
b = a  # b and a points to the same matrix , unsafe to b
b = a.copy()  # b has copied values , safe to change b
b[1 , 1] = 100

print("b {} after copying from a {}".format(b , a))

# ---------------Mathematical operations--------------
a = np.array([1,2,3])
print("Matrix multiplied by {} is {}".format(2,a*2))
print("Matrix sine values {}".format(np.sin(a)))

# ---------------Linear Algebra--------------
# Matrix multiplication
a = np.ones((2,3))
b = np.full((3,2),2)

result = np.matmul(a,b)
print("Multiply matrix 1 {} with Matrix 2 {} results {}".format(a,b,result))


