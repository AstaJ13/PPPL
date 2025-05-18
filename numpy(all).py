import numpy as np  

# 1D Arrays
a = [1, 2, 3, 4]
b = [1, 3, 5, 7, 9]
arr = np.array(a)

print(arr)
print("Type of a:", type(a))
print("Type of arr:", type(arr))
print("Type of b:", type(b))

# Creating arrays of zeros and ones
z = np.zeros((3, 3))
print("Zeros inside array:\n", z)

z1 = np.ones((4, 4), dtype=int)
print("Ones inside array:\n", z1)

# 2D Array
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr1)
print("Datatype of arr1:", arr1.dtype)
print("Dimension of arr1:", arr1.ndim)

# 3D Array
arr2 = np.array([[[1, 2, 3], [1, 2, 3], [1, 2, 3]]])
print("3D Array:\n", arr2)
print("Data Type of arr2:", arr2.dtype)
print("Dimension of arr2:", arr2.ndim)
print("Total no. of elements:", arr2.size)
print("Max element:", arr2.max())
print("Min element:", arr2.min())
print("Sum of elements:", arr2.sum())

# Identity Matrices
m = np.eye(3)
n = np.eye(4)
print("Identity Matrix 3x3:\n", m)
print("Identity Matrix 4x4:\n", n)

# 1D Array of Zeros
a1 = np.zeros(10)
print("1D array of zeros:\n", a1)

# 1D Array of Vowels
a2 = np.array(['a', 'e', 'i', 'o', 'u'])
print("Vowels:\n", a2)

# 2D Array of Ones
a3 = np.ones((2, 5), dtype=int)
print("2D array of ones:\n", a3)
print("Datatype of a3:", a3.dtype)

# Sum of columns and rows
print("Column-wise sum:\n", a3.sum(axis=0))
print("Row-wise sum:\n", a3.sum(axis=1))

# Example 2D array sum operations
eg = np.ones((4, 3), dtype=int)
print("Example 2D Array:\n", eg)
print("Column-wise sum:\n", eg.sum(axis=0))
print("Row-wise sum:\n", eg.sum(axis=1))
