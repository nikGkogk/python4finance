from pprint import pprint

import numpy as np

a = np.array([[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8],
              [9, 10, 11]])

b = np.array([[0., 0.5, 1.],
              [1.5, 2., 2.5],
              [3., 3.5, 4.],
              [4.5, 5., 5.5]])

print('Add vectors :')
pprint(a + b)

print('Operations on vectors like 2*a+3 :')
pprint(2 * a + 3)

c = np.array([0., 0.5, 1.])

print('The c (matrix) and a (vector) objects :')
pprint(a + c)


def f(x):
    return 3 * x + 5


print('Function applied to an ndarray object, resulting in a vectorized and element-wise evaluation of the function')
pprint(f(a))
