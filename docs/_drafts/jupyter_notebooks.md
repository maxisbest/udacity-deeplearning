# Jupyter Notebooks

## Magic Cells
### Debugging
- with `%pdb`

### Timeit
- `%timeit ...` : measures the time of one statement
- `%%timeit` measures and prints the time of a whole cell

### Matplotlib as inline
```
%matplotlib inline
%config InlineBackend.figure_format = 'retina'

import matplotlib as plt
```

### More Magic
- [->More on Magic](http://ipython.readthedocs.io/en/stable/interactive/magics.html)

## Converting them into html, slideshows, etc 
This can be done with the command **nbconvert**:
```
jupyter nbconvert notebook.ipynb --to slides
```

serve it immediately with **--post serve**:
```
jupyter nbconvert notebook.ipynb --to slides --post serve
```
