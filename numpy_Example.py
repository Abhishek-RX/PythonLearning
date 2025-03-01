import numpy as np


arr = np.array([1,0,3,4,7,6,5,8],dtype = "int64")
print(arr)
print(arr.shape)
print(arr.nonzero())
print(arr.dtype)
print(arr.itemsize)
print(arr.nbytes)
print(arr.reshape(4,2))

print("********************************************************************************")
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(matrix)
print(matrix.ndim)
print(matrix.shape)
print(matrix[: , 1])  # print every element of 2nd column
print(matrix[1 , :])  # print every element of 2nd row        
#print(np.dot(matrix, matrix.T))
 
print(matrix**2) # Square of each element   
print(matrix.reshape(-1,1))  # Convert 2D matrix to 1D matrix
# Transpose of a matrix
matrix = np.transpose(matrix)
#print(matrix)

