
```python
# ALWAYS IMPORT NUMPY FIRST.
import numpy as np
```

# Chapter 8 - Summary Statistics in NumPy
## Hey Techie,   
Welcome to the eigth notebook of this Numpy tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/gZGGexOyL9M (*until 7:16 min*). Today's video explains how to calculate different statistical measures for Numpy arrays. In the end, please try to solve the presented tasks. In case you are interested, you find a complete walk through the tasks at: https://youtu.be/ceJ4lVXN0T8 (*until 6:49 min*). 

## Have fun! :-)   
*Video length in total*: 8 minutes   
*Self-study time*: 8 minutes   
*Total*: **16 minutes**   
## Credits
Complete Python Numpy Tutorial for Beginners, Nate at StrataScratch, https://www.youtube.com/channel/UCW8Ews7tdKKkBT6GdtQaXvQ.

# Aggregations: Min, Max, and Everything In Between

Often when faced with a large amount of data, a first step is to compute summary statistics for the data in question.
Perhaps the most common summary statistics are the mean and standard deviation, which allow you to summarize the "typical" values in a dataset, but other aggregates are useful as well (the sum, product, median, minimum and maximum, quantiles, etc.).

NumPy has fast built-in aggregation functions for working on arrays; we'll discuss and demonstrate some of them here.

# Minimum and Maximum

Similarly, Python has built-in ``min`` and ``max`` functions, used to find the minimum value and maximum value of any given array:

```python
big_array = np.random.rand(1000000)
```

NumPy's corresponding functions have similar syntax, and again operate much more quickly:

```python
np.min(big_array), np.max(big_array)
```

For ``min``, ``max``, ``sum``, and several other NumPy aggregates, a shorter syntax is to use methods of the array object itself:

```python
print(big_array.min(), big_array.max(), big_array.sum())
```

## Multi dimensional aggregates

One common type of aggregation operation is an aggregate along a row or column.
Say you have some data stored in a two-dimensional array:

```python
M = np.random.random((3, 4))
print(M)
```

By default, each NumPy aggregation function will return the aggregate over the entire array:

```python
M.sum()
```

Aggregation functions take an additional argument specifying the *axis* along which the aggregate is computed. For example, we can find the minimum value within each column by specifying ``axis=0``:

```python
M.min(axis=0)
```

The function returns four values, corresponding to the four columns of numbers.

Similarly, we can find the maximum value within each row:

```python
M.max(axis=1)
```

The way the axis is specified here can be confusing to users coming from other languages.
The ``axis`` keyword specifies the *dimension of the array that will be collapsed*, rather than the dimension that will be returned.
So specifying ``axis=0`` means that the first axis will be collapsed: for two-dimensional arrays, this means that values within each column will be aggregated.

## Other aggregation functions

NumPy provides many other aggregation functions, but we won't discuss them in detail here.
Additionally, most aggregates have a ``NaN``-safe counterpart that computes the result while ignoring missing values, which are marked by the special IEEE floating-point ``NaN`` value.
Some of these ``NaN``-safe functions were not added until NumPy 1.8, so they will not be available in older NumPy versions.

The following table provides a list of useful aggregation functions available in NumPy:


|Function Name      |   NaN-safe Version  | Description                                   |
|-------------------|---------------------|-----------------------------------------------|
| ``np.sum``        | ``np.nansum``       | Compute sum of elements                       |
| ``np.prod``       | ``np.nanprod``      | Compute product of elements                   |
| ``np.mean``       | ``np.nanmean``      | Compute mean of elements                      |
| ``np.std``        | ``np.nanstd``       | Compute standard deviation                    |
| ``np.var``        | ``np.nanvar``       | Compute variance                              |
| ``np.min``        | ``np.nanmin``       | Find minimum value                            |
| ``np.max``        | ``np.nanmax``       | Find maximum value                            |
| ``np.argmin``     | ``np.nanargmin``    | Find index of minimum value                   |
| ``np.argmax``     | ``np.nanargmax``    | Find index of maximum value                   |
| ``np.median``     | ``np.nanmedian``    | Compute median of elements                    |
| ``np.percentile`` | ``np.nanpercentile``| Compute rank-based statistics of elements     |
| ``np.any``        | N/A                 | Evaluate whether any elements are true        |
| ``np.all``        | N/A                 | Evaluate whether all elements are true        |


We will see these aggregates often throughout the rest of the book.

# Practice Tasks
## 1. Print the min and max values of big_data.

```python
np.random.seed(1)  # seed for reproducibility
big_data = np.random.rand(1000000)
# INSERT CODE BELOW.
print("Max value:", np.max(big_data))
print("Max value:", big_data.max())
print("Min value:", np.min(big_data))
print("Min value:", big_data.min())
```

## 2. Print the sum of the elements of big_data.

```python
# INSERT CODE BELOW.
print("Sum:", big_data.sum())
```

## 3. Print the minimum value of each column of x.

```python
np.random.seed(1)  # seed for reproducibility
x = np.random.random((3, 4))
# YOUR CODE GOES HERE.
x.min(axis=0)
```

## 4. Print the maximum value of each row of x.

```python
# YOUR CODE GOES HERE.
x.max(axis=1)
```

