from pprint import pprint

import numpy as np

# compose a complex dtype
dt = np.dtype([('Name', 'S10'), ('Age', 'i4'),('Height', 'f'), ('Children/Pets', 'i4', 2)])
pprint(dt)

# create an array based on the previously created dt
s = np.array([
            ('Smith', 45, 1.83, (0, 1)),
            ('Jones', 53, 1.72, (2, 2))
        ],
        dtype=dt
    )
pprint(s)

# array is still ndarray
print(type(s))

# access data with index of row and name of column
print(s[1]['Age'])
