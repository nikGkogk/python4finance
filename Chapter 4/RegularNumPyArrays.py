from pprint import pprint
import time
import numpy as np
import math

# -- Creating arrays --
a = np.array([0, 0.5, 1.0, 1.5, 2.0])
a = np.array(['a', 'b', 'c'])
a = np.arange(2, 20, 2)  # start at 2, till 20, step of 2
a = np.arange(8, dtype=np.float_)  # can also pass the type of objects in range
a[5:]  # element 5 till end
a[:2]  # from start till element 2

print('Array functions')
print("===============")
arraySum = a.sum()
std = a.std()
cumsum = a.cumsum()
print(arraySum)
print(std)
print(cumsum)

print('Vectorised Operations')
print("=====================")
pprint(a)
pprint(2*a)
pprint(a**2)

print('Universal NumPy Functions')
print("=========================")
pprint(np.exp(a))
pprint(np.sqrt(a))

# even though math package also has same universal functions
# math.exp(a)
# math.sqrt(a)
# these will result in :
# "TypeError: only length-1 arrays can be converted to Python scalars"
# as math.sqrt() function cannot be applied to the ndarray object directly.

# math module universal functions are expected to be faster than numPy
start_time = time.time()
np.sqrt(2.5)
end_time = time.time()
elapsed_time = (end_time - start_time) * 1000  # in milliseconds
print("NumPy sqrt time: ", elapsed_time)

start_time = time.time()
math.sqrt(2.5)
end_time = time.time()
elapsed_time = (end_time - start_time) * 1000  # in milliseconds
print("Math sqrt time: ", elapsed_time)

print("Multiple Dimension Vectors")
print("==========================")
b = np.array([a, a * 2])
pprint(b)
b[0]     # select first row
b[0, 2]  # select first row, second column
b[:,1]   # select second column
print(b.sum())  # Calculates the sum of all values
print(b.sum(axis=0))   # Calculates the sum along the first axis; i.e., column-wise.
print(b.sum(axis=1))   # Calculates the sum along the second axis; i.e., row-wise.

# -- Vector initialization --
c = np.zeros((2, 3), dtype='i')  # Creates a ndarray object prepopulated with zeros.
c = np.ones((2, 3, 4), dtype='i')  # Creates a ndarray object prepopulated with ones.
d = np.zeros_like(c, dtype='f16')  # Creates a ndarray object but takes another ndarray object to infer the shape
d = np.ones_like(c, dtype='f16')  # Creates a ndarray object but takes another ndarray object to infer the shape
e = np.empty((2, 3, 2)) # Creates an ndarray object not prepopulated with anything (numbers depend on the bits present in the memory!!!)
f = np.empty_like(c)  # Creates an ndarray object not prepopulated with anything but takes another ndarray object to infer the shape
diagonal = np.eye(5)  # Creates a square matrix as a ndarray object with the diagonal populated by ones.
g = np.linspace(5, 15, 12)  # Creates a one-dimensional ndarray object with evenly spaced intervals between numbers
                                            # parameters used are start, end, and num (number of elements).

print("ndarray MetaInformation")
print("=======================")
c = np.zeros((2, 3), dtype='f16')
pprint(c)
print("The number of elements : ", c.size)
print("The number of bytes used to represent one element :", c.itemsize)
print("The number of dimensions : ", c.ndim)
print("The shape of the ndarray object : ", c.shape)
print("The dtype of the elements : ", c.dtype)
print("The total number of bytes used in memory : ", c.nbytes)

print("Reshaping ndarray")
print("=================")
g = np.arange(15)
pprint(g)
print("The shape of the ndarray object : ", g.shape)
g = g.reshape((3, 5))
pprint(g)
print("The shape of the ndarray object : ", g.shape)
print("Flatten an ndarray object : ")
pprint(g.flatten())


# In linear algebra, the transpose of a matrix is an operator which flips a matrix over its diagonal.
# That is, it switches the row and column indices of the matrix.
print("The transpose of the new ndarray object. : ")
pprint(g.transpose())  # or g.T

print("Resizing ndarray")
print("================")
g = np.arange(15)
pprint(np.resize(g, (3, 1)))  # downsize
pprint(np.resize(g, (1, 5)))  # downsize
pprint(np.resize(g, (2, 5)))  # downsize
pprint(np.resize(g, (5, 4)))  # upsize

print("Stacking ndarray")
print("================")
g = np.arange(15).reshape(5, 3)
pprint(g)
hg = np.hstack((g, g * 2))  # Horizontal stacking of two ndarray objects.
pprint(hg)
vg = np.vstack((g, g * 2))  # Vertical stacking of two ndarray objects.
pprint(vg)

print("Boolean ndarray")
print("================")
g = np.arange(15).reshape(5, 3)
pprint(g > 8)     # is the element value greater than 8
pprint(g[g > 8])  # give me the elements with value greater than 8
pprint(np.where(g % 2 == 0, 'even', 'odd'))  # conditional value to the result