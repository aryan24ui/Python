#Write a program to find the maximum of the numbers in a list using the reduce function
from functools import reduce
l = [1, 63865, 2, 585, 5785, 323, 789, 2135, 45, 55]

def greater(a, b):
    if(a>b):
        return a
    return b

print(reduce(greater, l))