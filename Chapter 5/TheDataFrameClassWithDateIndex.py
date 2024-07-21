from pprint import pprint
from pylab import plt, mpl

import numpy as np
import pandas as pd

np.random.seed(100)
a = np.random.standard_normal((9, 4))  # A ndarray with standard normally distributed random numbers

dates = pd.date_range('2019-1-1', periods=9, freq='ME')  # Create a DatetimeIndex

df = pd.DataFrame(a, index=dates, columns=['No1', 'No2', 'No3', 'No4'])  # Create a DataFrame from the ndarray

print('A Dataframe with DateTimeIndex:')
pprint(df)

# Basic Analytics
pprint(df.info())
pprint(df.describe())

print('Column-wise sum:')
pprint(df.sum())

print('Column-wise mean:')
pprint(df.mean(axis=0))

print('Row-wise mean:')
pprint(df.mean(axis=1))

print('Column-wise cumulative sum:')
pprint(df.cumsum())

# DataFrame objects also understand NumPy universal functions, as expected:
print('NumPy Column-wise mean:')
pprint(np.mean(df))

print('NumPy log:')
pprint(np.log(df))

# Basic Visualisation
pprint(plt.style.available)  # see available styles
plt.style.use('seaborn-v0_8')
mpl.rcParams['font.family'] = 'serif'

df.cumsum().plot(lw=2.0, figsize=(10, 6))
plt.show()

df.plot(kind='bar', figsize=(10, 6))
plt.show()

# Series Class
# A Series object is obtained when a single column is selected from a multicolumn DataFrame object:
s = df['No1']
print('Series example:')
pprint(s)
pprint(type(s))

# GroupBy Operations
df['Quarter'] = ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3', 'Q3']
groups = df.groupby('Quarter')  # Groups according to the Quarter column.
print('Grouped data operations:')
pprint(groups.size())
print('Gives the mean per column:')
pprint(groups.mean())
print('Gives the maximum value per column:')
pprint(groups.max())
print('Gives both the minimum and maximum values per column:')
pprint(groups.aggregate([min, max]).round(2))

# Grouping can also be done with multiple columns.
df['Odd_Even'] = ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']
groups = df.groupby(['Quarter', 'Odd_Even'])
print('Multiple columns grouped data operations:')
pprint(groups.size())
pprint(groups[['No1', 'No4']].aggregate([np.sum, np.mean]))
