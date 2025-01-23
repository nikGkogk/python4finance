# Chapter 8 Notes

Reading csv data into panda uses 0 as default index.
In any other case, you can define the index like this :
```python
# make sure to define index column
data = pd.read_csv(filename, index_col='Date')
```

Indexes are loaded as strings, but for any function than needs dateObjects (ex. resample),
you will need to convert the strings to dates like this:
```python
# convert the index to actual date objects
data.index = pd.to_datetime(data.index) 
```

When resampling, pandas take by default the left label (index value) of the interval.
To be financially consistent, make sure to use the right label (index value).
Something like week-end, month-end.. for which the week-end, month-end date (right value of interval)
should be used and not the start date (left time of interval)
```python
rets.cumsum().apply(np.exp).resample('1ME', label='right').last().plot(figsize=(10, 6));
```