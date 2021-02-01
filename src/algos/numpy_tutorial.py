
# numpy is the core library for scientific computing in python
# it provides a high performance multidimentional array object and tools for
# working with these arrays
import numpy as np

# the number of dimensions is the rank of the array
# this is a rank 1 array
a = np.array([1, 2, 3])
print(type(a), a.shape, a[0], a[1])

# rank 2 array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b.shape, b[0, 0], b[0, 1], b[1, 0])

# create an array of all zeros
c = np.zeros((2, 2))
print('array of zeros', c)

# create an array of all ones
d = np.ones((1, 2))
print('array of ones', d)

# array of consts
e = np.full((2, 2), 7)
print('array of consts', e)

f = np.eye(2)
print('identity matrix', f)

g = np.random.random((2, 2))
print('array of randoms', g)

# slicing arrays
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# b is a view into a so changing it will change a
b = a[:2, 1:3]
#  [ 2  3]
#  [ 6  7]]

print('sliced array', b)

# we can also use integet indexes but that will yeald an array of a lower rank
second_row_rank_1 = a[1, :]
print('second row rank 1', second_row_rank_1)

second_row_rank_2 = a[1:2, :]
print('second row rank 2', second_row_rank_2)

second_row_rank_2_2 = a[[1], :]
print('second row rank 2_2', second_row_rank_2_2)

# or same with columns
second_col_rank_1 = a[:, 1]
print('second column rank 1', second_col_rank_1)

second_col_rank_2 = a[:, [1]]
print('second column rank 2', second_col_rank_2)

# we can also access arrays using integer array indexing
a = np.array([[1, 2], [3, 4], [5, 6]])
print('array integer index', a[[0, 1, 2], [0, 1, 0]])
# same as
print('array integer index2', np.array([a[0, 0], a[1, 1], a[2, 0]]))

# we can easily access one elemens from each row
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# array of col indices
b = np.array([0, 2, 0, 1])
print(a[np.arange(4), b])

# or mutate
a[np.arange(4), b] += 10
print(a)

# boolean array indexing - select elements of the array whihc satisfy a condition
