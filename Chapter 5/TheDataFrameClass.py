from pprint import pprint

import pandas as pd

df = pd.DataFrame(
    [10, 20, 30, 40],      # Define the data as a list object
    columns=['numbers'],        # Specify the column label
    index=['a', 'b', 'c', 'd']  # Specify the index values/labels
)

pprint(df)

print('The index attribute and Index object:')
pprint(df.index)
print('The columns attribute and Index object:')
pprint(df.columns)
print('Selects the value corresponding to index c:')
pprint(df.loc['c'])
print('Selects the two values corresponding to indices a and d:')
pprint(df.loc[['a', 'd']])
print('Selects the second and third rows via the index positions:')
pprint(df.iloc[1:3])
print('Calculates the sum of the single column:')
pprint(df.sum())
print('Uses the apply() method to calculate squares in vectorized fashion:')
pprint(df.apply(lambda x: x ** 2))
print('Applies vectorization directly as with ndarray objects:')
pprint(df ** 2)

print('Enlarge the DataFrame with a list:')
df['floats'] = (1.5, 2.5, 3.5, 4.5)
pprint(df)

# A whole DataFrame object can also be taken to define a new column.
# In such a case, indexes are aligned automatically
print('Enlarge the DataFrame with an other DataFrame:')
df['names'] = pd.DataFrame(
    ['Yves', 'Sandra', 'Lilli', 'Henry'],
    index=['d', 'a', 'b', 'c']
)
pprint(df)

print('Enlarge the DataFrame with an other DataFrame by appending data:')
df = df._append(pd.DataFrame({'numbers': 100, 'floats': 5.75, 'names': 'Jil'}, index=['y',]))
pprint(df)

print('Enlarge the DataFrame with an other DataFrame by appending incomplete data:')
df = df._append(pd.DataFrame({'names': 'Liz'}, index=['z',]))
pprint(df)

# Although there are now missing values, the majority of method calls will still work
print('Column Mean:')
pprint(df[['numbers', 'floats']].mean())
print('Column Standard Deviation:')
pprint(df[['numbers', 'floats']].std())
