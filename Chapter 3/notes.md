# Chapter 3 Notes

### There is a saying that “everything in Python is an object.”
Which means that even basic data types have built-in functions

```python
a = 10
a.bit_length()
Out: 4
```

### Data structures
`tuple` : An immutable collection of arbitrary objects; only a few methods available

`list` : A mutable collection of arbitrary objects; many methods available

![list-operations.png](img%2Flist-operations.png)

`dict` : A key-value store object

![dict-operations.png](img%2Fdict-operations.png)

`set` : An unordered collection object for other unique objects

### List Comprehensions, Functional Programming, Anonymous Functions
It can be considered good practice to avoid loops on the Python
level as far as possible. List comprehensions and functional pro‐
gramming tools like filter(), map(), and reduce() provide
means to write code without (explicit) loops that is both compact
and in general more readable. lambda or anonymous functions are
also powerful tools in this context.