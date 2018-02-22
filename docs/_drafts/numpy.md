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
2 dimensional numpy arrays

Example:
```
m = np.array([[1,2,3], [4,5,6], [7,8,9]])
```
The shape is `m.shape`: `(3,3)`: 3 rows and 3 columns

## Tensors
numpy arrays with a higher dimension:

Example
```
t = np.array([[[[1],[2]],[[3],[4]],[[5],[6]]],[[[7],[8]],\
    [[9],[10]],[[11],[12]]],[[[13],[14]],[[15],[16]],[[17],[17]]]])
```
The shape `t.shape` is `(3,3,2,1)`

In Machine Learning we are oftne dealing with higher dimensional tensors.

