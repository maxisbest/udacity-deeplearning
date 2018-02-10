# numpy

## Import
```
import numpy as np
```

## Arrays 
Arrays are usaually created form list of lists
```
a = np.array(['a', 'c', 'd'])
```

Arrays have homogenous types:
- `a.dtype`: is more fine grained then types in python: `ìnt32`, `int64`, etc.
- `a.shape`: shape of the array


## Scalars
```
s = np.array(5)
```
scalars have shape `()`

## Vectors
1- dimensional arrays, such as:
```
a = np.array([5, 8, 1])
```

they have `a.shape`: `(3,)`

## Matrices

Example:
```
m = np.array([[1,2,3], [4,5,6], [7,8,9]])
```
The shape is `m.shape`: `(3,3)`: 3 rows and 3 columns

