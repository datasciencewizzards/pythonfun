# Sum of all the element of a list

l = [1,2,3,4]


from functools import reduce

result = reduce(lambda a,b:a+b,l)
print(result)

# find largest in a list
l = [1,20,3,4]


def max1(a, b):
    if(a>b) :
        return a
    else :
        return b


result = reduce(lambda a,b:max1(a,b),l)
print(result)

# rotate list
l = [1,20,3,4]

# left rotation
def rotateList(list,steps):
    return l[2:]+l[:2]

print(rotateList(l,2))

# implement right and left rotation

# Swap first and the last element of the array
l = [1,20,3,4]

l[0],l[-1] = l[-1],l[0]

print(l)

#