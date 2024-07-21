from pprint import pprint

import numpy as np
import pandas as pd

data = np.random.standard_normal((10, 2))  # ndarray object with standard normally distributed random numbers
df = pd.DataFrame(data, columns=['x', 'y'])  # DataFrame object with the same random numbers.
df.info()

print('Comparison operators and logical operators on values in the two columns:')
pprint(df['x'] > 0.5)  # Check whether value in column x is greater than 0.5.
# similarly
(df['x'] > 0) & (df['y'] < 0)  # Check whether value in column x is positive and value in column y is negative
(df['x'] > 0) | (df['y'] < 0)  # Check whether value in column x is positive or value in column y is negative

print('All rows for which the value in column x is greater than 0')
xGrtZero = df[df['x'] > 0]
xGrtZero = df.query('x > 0')
pprint(xGrtZero)

print('All rows for which the value in column x is positive and the value in column y is negative.')
xyGrtZero = df[(df['x'] > 0) & (df['y'] < 0)]
xyGrtZero = df.query('x > 0 & y < 0')
xyGrtZero = df[(df.x > 0) & (df.y < 0)]
pprint(xyGrtZero)

print('Comparison operators can also be applied to complete DataFrame objects at once:')
pprint(df > 0)
pprint(df[df > 0])

# Concatenation, Joining and Merging
df1 = pd.DataFrame(data=['100', '200', '300', '400'],
                   index=['a', 'b', 'c', 'd'],
                   columns=['A'])
df2 = pd.DataFrame(data=['200', '150', '50'],
                   index=['f', 'b', 'd'],
                   columns=['B'])
print('Concat data frames')
pprint(pd.concat((df1, df2), sort=False, ignore_index=False))

print('There are a total of four different join methods available, each leading to a different behavior'
      ' with regard to how index values and the corresponding data rows are handled:')
df1.join(df2, how='left')  # Left join is the default operation.
df1.join(df2, how='right')  # Right join is the same as reversing the sequence of the DataFrame objects.
df1.join(df2, how='inner')  # Inner join only preserves those index values found in both indices.
pprint(df1.join(df2, how='outer'))  # Outer join preserves all index values from both indices.

print('Merging data frames')
c = pd.Series([250, 150, 50], index=['b', 'd', 'c'])
df1['C'] = c
df2['C'] = c

print('Merge based on column C')
pprint(pd.merge(df1, df2, on='C'))

print('An outer merge is also possible, preserving all data rows.')
pprint(pd.merge(df1, df2, how='outer'))

