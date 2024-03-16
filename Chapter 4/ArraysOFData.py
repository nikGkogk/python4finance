import array
from copy import deepcopy
from pprint import pprint

# --- Use of Lists ---
v = [0.5, 0.75, 1.0, 1.5, 2.0]
m = [v, v, v]
pprint(m)

# objects are passed as reference, so change in original object changes the m array data
v[0] = 'Python'
print('Array object changed by reference :')
pprint(m)

# by using deepcopy we get new copied objects
v = [0.5, 0.75, 1.0, 1.5, 2.0]
m = 3 * [deepcopy(v), ]
print('Deepcopy array :')
pprint(m)

# --- Use of array Class ---
v = [0.5, 0.75, 1.0, 1.5, 2.0]
# array type is specified at object creation time by using a type code, which is a single character.
a = array.array('f', v)
pprint(a)

# major methods available like List
a.append(0.5)
a.extend([1.5, 5.5])
print('After operations :')
pprint(a)

# Although “scalar multiplication” works in principle, the result is not the mathematically expected one
# rather, the elements are just repeated.
a = 2 * a
print('Multiply array :')
pprint(a)

# trying this -> a.append('string')
# would lead to an error as only float objects can be appended; other data types/type codes raise errors

# you can convert array to list
a.tolist()

# write array to file
f = open('array.apy', 'wb')
a.tofile(f)
f.close()

# alternative way to write to file
with open('array.apy', 'wb') as f:
    a.tofile(f)

# read array from file (data type declaration)
b = array.array('f')
with open('array.apy', 'rb') as f:
    b.fromfile(f, 5)
print('From file :')
pprint(b)
