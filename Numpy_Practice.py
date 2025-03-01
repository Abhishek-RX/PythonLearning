import numpy as np 

# Broadcasting in numpy
# If you have two arrays of different shapes, numpy will broadcast the smaller one to the larger one.
# Broadcasting is the term used to describe how numpy handles element-wise arithmetic operations with arrays of different shapes.
a = np.array([[2,4,6],[8,10,12]])
b = np.array([1,2,2])

#subtract b from a 

c = a-b
print(c)
print("************************************************************************")
# 2 Vectorization
# Vectorization is the ability to organize the code in such a way 
# that the operations are performed on entire arrays rather than on individual elements.
# This is the main advantage of using numpy.

arr = np.arange(1,10**6)
res  = arr**2
print(res)
print("************************************************************************")
#3 Fancy indexing 
# Fancy indexing is the term used to describe indexing using integer arrays.
# It allows you to construct arbitrary arrays using the data from another array.
A = np.array([10,20,30,40,50,60,70,80])

res = np.array([1,3,5])
print(A[res])
print("************************************************************************")
#4 Boolean masking 
# Boolean masking is the term used to describe the use of boolean arrays to filter arrays.
# It allows you to construct arbitrary arrays using the data from another array.

A = np.array([5,12,8,21,33,45])
mask = A>10
print(A[mask])
print("************************************************************************")

# 🚀 5. Conditional Selection with np.where() 
# The np.where() function returns the indices of elements in an input array where the given condition is satisfied.
# It can be used to filter elements from an array based on a condition.

A = np.array([5,12,8,21,0,33,45])
res = np.where(A%2 == 0 , "Even", "Odd")
print(res)
print("************************************************************************")


