"""
Numerical Analysis with Numpy Arrays

Numpy is a Linear Algebra Library for Python, and it’s very fast because of it’s native bindings
The most important concept in Numpy are Arrays that look a lot like lists, and Matrixes that look like tables
Many Data Science libs like pandas, sklearn and matplotlib rely on Numpy as base, and consequently take Numpy Arrays as
inputs and outputs to it’s methods.
Let’s take a look together at numpy in the CEBD-1160-code project

"""
import numpy as np

# 2. Create your first array with the elements [1,22.4,5,35,4,6.7,3,8,40] and print it.
# Experiment what the following functions do: ndim, shape, size and dtype.
first_arr = np.array([1, 22.4, 5, 35, 4, 6.7, 3, 8, 40])
print(f"This array is: {first_arr}")
print(f"This array's dimension is {first_arr.ndim}.")
print(f"This array's shape is {first_arr.shape}.")
print(f"This array has total {first_arr.size} elements.")
print(f"Type of elements in this array are all {first_arr.dtype}.")

# 3. Create your first matrix with the elements [['a', 'b'],['c', 'd'],[3, 3]] and print it.
# Experiment what the following functions do: ndim, shape, size and dtype.
first_matrix = np.array([['a', 'b'], ['c', 'd'], [3, 3]])
print(f"\nThis matrix is:\n{first_matrix}")
print(f"This matrix's dimension is {first_matrix.ndim}.")
print(f"This matrix's shape is {first_matrix.shape}.")
print(f"This matrix has total {first_matrix.size} elements.")
print(f"Tpye of elements in this matrix is {first_matrix.dtype}.\n")

# Summary of numpy array/matrix attributes:
# - ndim: Get the number of axes (dimensions/rank).
# - shape: This is a tuple of integers indicating the size of the array in each dimension.
# - size: Get total number of elements. It's equal to the product of the elements of shape.
# - dtype: Describe the type of the elements.
#  - Every ndarray has an associated data type (dtype) object, including information about :
#   -- Type of the data (integer, float, Python object etc.)
#   -- Size of the data (number of bytes)
#   -- Byte order of the data ('<': little-endian or '>': big-endian)
#      (output: <U1: unsigned ints with little-endian byte ordering)
#   -- If the data type is a sub-array, what is its shape and data type.

# Create numpy 1 dimension array using each of the functions arange and rand
print(f"Create 1 dimension array:\n{np.arange(25)}")
print(f"Create 1 dimension array:\n{np.random.rand(25)}\n")

# Create numpy 2 dimensions matrix using each of the functions zeros and rand
print(f"Create 2 dimensions matrix:\n{np.zeros((6, 4))}")
print(f"Create 2 dimensions matrix:\n{np.random.rand(3, 5)}\n")

# Create an array containing 20 times the value 7. Reshape it to a 4 x 5 Matrix
second_arr = np.array([7]).repeat(20)
print(f"An array contains twenty 7: {second_arr}")
reshape_to_matrix = second_arr.reshape(4, 5)
print(f"Reshape this array to (4,5) matrix:\n{reshape_to_matrix}\n")

# Create a 6 x 6 matrix with all numbers up to 36, then print:
# - only the first element on it
# - only the last 2 rows for it
# - only the 2 mid columns and 2 mid rows for it
# - the sum of values for each column
third_matrix = np.arange(1, 37).reshape(6, 6)

print(f"The first element is: {third_matrix[0, 0]}")
print(f"The last two rows are:\n{third_matrix[-2:, :]}")
print(f"The 2 mid columns and 2 mid rows are:\n{third_matrix[2:4, 2:4]}")
print(f"The sum value for each column are: {third_matrix.sum(axis=0)}")
