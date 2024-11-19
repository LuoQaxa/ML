# theme: numpy fundamentals
# author: QIAN LUO
# time: 01/11/2024
import numpy as np


# 1. difference from list in python, not copy, it refers to the original array.
list = [1,2,3,4,5,6]
a = np.array(list)
a[0] = 10
b = a[3:]
print(b)
b[0] = 40
print(a)

# 2.higher-dimensional arrays initialize
a_md = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# 3. attributes ndim\shape\size\\dtype
print("ndim of a_md: ", a_md.ndim)
print("shape of a_md: ", a_md.shape)
print("size of a_md: ", a_md.size) # total number of elements
print("dtype of a_md: ", a_md.dtype)

# 4. create array
print(np.arange(2,9,2)) # start, stop, step

# 5. convert 1D array into 2D array(add a new axis to an array)
a1 = np.array([1,2,3,4,5,6])
a2 = a1[np.newaxis, :]
print(f'a2 {a2}')  # -> 1 * 6 [[1 2 3 4 5 6]]

a3 = a1[:, np.newaxis]
print(f'a3 {a3}')  # -> 6 * 1

# index
print("index can use condition a[a < 5]: ",a[a < 5])

# operations sum / subtraction / multiplication / division
a_sum = np.array([[1,1],[2,2]])
print('sum over the axis of row', a_sum.sum(axis=0) )
print('sum over the axis of column', a_sum.sum(axis=1) )
print('multiply', a_sum * 2)


