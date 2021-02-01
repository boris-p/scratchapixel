
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

# we can easily access one element from each row
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# array of col indices
b = np.array([0, 2, 0, 1])
print(a[np.arange(4), b])

# or mutate
a[np.arange(4), b] += 10
print(a)

# boolean array indexing - select elements of the array which satisfy a condition
a = np.array([[1, 2], [3, 4], [5, 6]])
bool_idx = (a > 2)
print(bool_idx)

# from that we can also construct a rank 1 array of all the elements that were true
print(a[bool_idx])

# we can be even more concise
print(a[a > 2])

# np arrays are typed, numpy tries to guess the type but we can also specify it
x = np.array([1, 2], dtype=np.int64)
print(x.dtype)

# --------------------------------------------------------
# -------------------  array math ------------------------
# --------------------------------------------------------
print('array math')

# exist both as operator overloads and as np functions
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a + b)
print(np.add(a, b))

print(a - b)
print(np.subtract(a, b))

print(a * b)
print(np.multiply(a, b))

# also divide, sqrt and probably others

# computing products
v = np.array([9, 10])
w = np.array([11, 12])

print(v.dot(w))
print(np.dot(v, w))
# using @ is the same
print(v @ w)

# ways to calculate the matrix / vector product
# these are all the same
print(a.dot(v))
print(np.dot(a, v))
print(a @ v)

# matrix / matrix product
print(a.dot(b))
print(np.dot(a, b))
print(a @ b)

# coimputations on arrays

# sum
x = np.array([[1, 2], [3, 4]])
print(np.sum(x))
print(np.sum(x, axis=0))  # compute the su of each column
print(np.sum(x, axis=1))  # compute the su of each row

# transpose
print(x)
print('transposed:\n', x.T)

# --------------------------------------------------------
# -------------------  broadcasting ----------------------
# --------------------------------------------------------
print('broadcasting\n')

# perform action on arrays of different sizes

# for instance add a constant vector to each row of a matrix

# the standard way would be to do it like this:
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)   # Create an empty matrix with the same shape as x

for i in range(4):
    y[i, :] = x[i, :] + v

print(y)
# this works but for very large arrays can be slow
# we can also create another 4X4 matrix from the vactor and then just add the two matrixes

vv = np.tile(v, (4, 1))
print(vv)
print(x + vv)

# with broadcasting we don't even need to do that and can just do
print(x + v)

# because broadcasitng works on arrays with different lengths
# there are some rules for how they work so if it's relevant might be worth
# reading a more detailed description

# a few examples

print("Compute outer product of vectors")
v = np.array([1, 2, 3])  # v has shape (3,)
w = np.array([4, 5])    # w has shape (2,)
# To compute an outer product, we first reshape v to be a column
# vector of shape (3, 1); we can then broadcast it against w to yield
# an output of shape (3, 2), which is the outer product of v and w:

print(np.reshape(v, (3, 1)) * w)

print("Add a vector to each column of a matrix")
x = np.array([[1, 2, 3], [4, 5, 6]])
# x has shape (2, 3) and w has shape (2,).
# If we transpose x then it has shape (3, 2) and can be broadcast
# against w to yield a result of shape (3, 2); transposing this result
# yields the final result of shape (2, 3) which is the matrix x with
# the vector w added to each column. Gives the following matrix:

print((x.T + w).T)

# Another solution is to reshape w to be a row vector of shape (2, 1);
# we can then broadcast it directly against x to produce the same
# output.
print(x + np.reshape(w, (2, 1)))

print("Multiply a matrix by a constant")
# x has shape (2, 3). Numpy treats scalars as arrays of shape ();
# these can be broadcast together to shape (2, 3), producing the
# following array:
print(x * 2)

# Broadcasting typically makes your code more concise and faster, so you should strive to use it where possible

# this is a very partial overview of numpy!

