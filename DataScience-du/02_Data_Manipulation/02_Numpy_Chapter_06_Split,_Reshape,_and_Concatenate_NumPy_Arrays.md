# Chapter 6 - Split, Reshape, and Concatenate NumPy Arrays
## Hey Techie,   
Welcome to the sixth notebook of this Numpy tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/dWQvU9p7TdU. Today's video explains splitting and reshaping arrays as well as how to concatenate them. In the end, please try to solve the presented tasks.

## Have fun! :-)   
*Video length in total*: 21 minutes   
*Self-study time*: 21 minutes   
*Total*: **42 minutes**   
## Credits
Complete Python Numpy Tutorial for Beginners, Nate at StrataScratch, https://www.youtube.com/channel/UCW8Ews7tdKKkBT6GdtQaXvQ.

# Reshaping of Arrays

Another useful type of operation is reshaping of arrays.
The most flexible way of doing this is with the ``reshape`` method.
For example, if you want to put the numbers 1 through 9 in a $3 \times 3$ grid, you can do the following:


```python
grid = np.arange(1, 10).reshape((3, 3))
grid
```

Note that for this to work, the size of the initial array must match the size of the reshaped array. 

Another common reshaping pattern is the conversion of a one-dimensional array into a two-dimensional row or column matrix.
This can be done with the ``reshape`` method.


```python
x = np.array([1, 2, 3])

# row vector via reshape
x.reshape((1, 3))
x
```


```python
# column vector via reshape
print(x)
print(x.reshape((3, 1)))
```


```python
# column vector via newaxis
x[:, np.newaxis]
```

# Array Concatenation and Splitting

All of the preceding routines worked on single arrays. It's also possible to combine multiple arrays into one, and to conversely split a single array into multiple arrays. We'll take a look at those operations here.

## Concatenation of arrays

Concatenation, or joining of two arrays in NumPy, is primarily accomplished using the routines ``np.concatenate``, ``np.vstack``, and ``np.hstack``.
``np.concatenate`` takes a tuple or list of arrays as its first argument, as we can see here:


```python
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
np.concatenate([y,x])
```

You can also concatenate more than two arrays at once:


```python
z = [99, 99, 99]
print(np.concatenate([x, y, z]))
```

It can also be used for two-dimensional arrays:


```python
grid = np.array([[1, 2, 3],
                 [4, 5, 6]])

grid
```


```python
# concatenate along the first axis
np.concatenate([grid, grid], axis=0)
```


```python
# concatenate along the second axis
np.concatenate([grid, grid], axis=1)
```

For working with arrays of mixed dimensions, it can be clearer to use the ``np.vstack`` (vertical stack) and ``np.hstack`` (horizontal stack) functions:


```python
x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],
                 [6, 5, 4]])

# vertically stack the arrays
np.vstack([x, grid])
```


```python
# horizontally stack the arrays
y = np.array([[99],
              [99]])
np.hstack([grid, y])
```

## Splitting of arrays

The opposite of concatenation is splitting, which is implemented by the functions ``np.split``, ``np.hsplit``, and ``np.vsplit``.  For each of these, we can pass a list of indices giving the split points:


```python
x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3)
```

Notice that *N* split-points, leads to *N + 1* subarrays.
The related functions ``np.hsplit`` and ``np.vsplit`` are similar:


```python
grid = np.arange(16).reshape((4, 4))
grid
```


```python
upper, lower = np.vsplit(grid, [2])
print(upper)
print(lower)
```


```python
left, right = np.hsplit(grid, [2])
print(left)
print(right)
```


# Practice Tasks   

## 1. Create a range from 1 to 16 and reshape it into a (2, 8) array.


```python
# YOUR CODE STARTS HERE.
np.arange(0,16).reshape(2,8)
```


## 2. Reshape x1 into a 1 dimensional column using slice notation and np.newaxis.


```python
np.random.seed(1)  # seed for reproducibility
x1 = np.random.randint(10, size=9)  # One-dimensional array
# YOUR CODE STARTS HERE.
```
x1[:, np.newaxis]


## 3. Concatenate arrays *x* and *y*.


```python
x = np.array([2, 4, 6])
y = np.array([8, 10, 12])
# YOUR CODE STARTS HERE.
np.concatenate([x,y])
```


## 4. Concatenate arrays *x*, *y*, and *z*.


```python
z = [99, 99, 99]
# YOUR CODE STARTS HERE.
np.concatenate([x,y,z])
```


## 5. Concatenate *array* with itself along the second axis.


```python
array = np.array([[5, 4, 1],
                 [4, 5, 6]])
# YOUR CODE STARTS HERE.
np.concatenate([grid, grid], axis=1)
```


## 6. Concatenate x and *array* using the vstack function.


```python
# YOUR CODE STARTS HERE.
np.vstack([x,array])
```


## 7. Split *x* on element 4 and element 7.


```python
x = [1, 2, 3, 99, 99, 3, 2, 1]
# YOUR CODE STARTS HERE.
x1, x2, x3 = np.split(x, [3,6])
```


## 8. Split *array* on row 3.


```python
array = np.arange(25).reshape((5, 5))
# YOUR CODE STARTS HERE.
nvsplit = np.vsplit(array, [2])
```


## 9. Split *array* on column 4.


```python
# YOUR CODE STARTS HERE.
nhsplit = np.hsplit(array, [3])
```


