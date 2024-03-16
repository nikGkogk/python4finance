# Chapter 4 Notes

## NumPy ndarray
The use of NumPy for array-based operations and algorithms generally results in compact, 
easily readable code and significant performance improvements over pure plain Python code.

 - The ndarray object has built-in dimensions (axes).
 - The ndarray object is immutable; its length (size) is fixed.
 - It only allows for a single data type (np.dtype) for the whole array.

During a reshaping operation, the total number of elements in the ndarray object is
unchanged. During a resizing operation, this number changes—it either decreases
(“down-sizing”) or increases (“up-sizing”)

## Structured NumPy Arrays
Objects that allow you to have a different dtype per column that allow the description and handling of table-like
data structures. They bring SQL table–like data structures to Python, with
most of the benefits of regular ndarray objects (syntax, methods,
performance).
 - structured ndarray
 - record ndarray

## NumPy Arrays Memory Layout

```python
import numpy as np
## C is Contiguous layout. Mathematically speaking, row major.
C = np.array([...], order='C')
## F is Fortran contiguous layout. Mathematically speaking, column major.
F = np.array([...], order='F')
```

 -  When calculating the sum of all elements, the memory layout does not really matter. 
 - The summing up over the C-ordered ndarray objects is faster both over rows and over columns (an absolute speed advantage). 
 - With the C-ordered (row-major) ndarray object, summing up over rows is relatively faster compared to summing up over columns. 
 - With the F-ordered (column-major) ndarray object, summing up over columns is relatively faster compared to summing up over rows.