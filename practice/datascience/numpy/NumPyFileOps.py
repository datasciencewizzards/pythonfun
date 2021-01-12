# File operations : Numpy
import numpy as np

fileData = np.genfromtxt("data/data.txt" , delimiter=",")
fileData = fileData.astype("int32")
print(fileData)

# Filtering data
print(fileData[fileData > 50])

# 1 ,2 ,3 ,4 , 5
# 6, 7, 8, 9, 10
# 11,12,13,14,15
# 16,17,18,19,20
# 21,22,23,24,25
# 26,27,28,29,30
# Print 11,12, 16,17
arr = np.array([[1  , 2  , 3  , 4  , 5] ,
               [6  , 7  , 8  , 9  , 10] ,
               [11 , 12 , 13 , 14 , 15] ,
               [16 , 17 , 18 , 19 , 20] ,
               [21 , 22 , 23 , 24 , 25] ,
               [26 , 27 , 28 , 29 , 30]])

# First Setting is the col span and then row span
# print : 11,12 ; 16,17
print(arr[2:4,0:2])

# print : 2,8,14,20
print(arr[[0,1,2,3],[1,2,3,4]])

# print : 4,5,24,25,29,30
print(arr[[0,4,5],3:])


