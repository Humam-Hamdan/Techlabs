
```python
# ALWAYS IMPORT NUMPY FIRST.
import numpy as np
# LIBRARIES NEEDED FOR THE EXAMPLE.
import pandas as pd
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
```

# Chapter 9 - A Boolean Mask on NumPy Arrays
## Hey Techie,   
Welcome to the final notebook of this Numpy tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/LL7dnUymOvo. Today's video explains how to use boolean masks in Numpy arrays. In the end, please try to solve the presented tasks. In case you are interested, you find a complete walk through the tasks at: https://youtu.be/e6C1Z-o1fyQ. 

## Have fun! :-)   
*Video length in total*: 28 minutes   
*Self-study time*: 28 minutes   
*Total*: **56 minutes**   
## Credits
Complete Python Numpy Tutorial for Beginners, Nate at StrataScratch, https://www.youtube.com/channel/UCW8Ews7tdKKkBT6GdtQaXvQ.

# Comparisons, Masks, and Boolean Logic

This section covers the use of Boolean masks to examine and manipulate values within NumPy arrays.
Masking comes up when you want to extract, modify, count, or otherwise manipulate values in an array based on some criterion: for example, you might wish to count all values greater than a certain value, or perhaps remove all outliers that are above some threshold.
In NumPy, Boolean masking is often the most efficient way to accomplish these types of tasks.

## Example: Counting Rainy Days

Imagine you have a series of data that represents the amount of precipitation each day for a year in a given city.
For example, here we'll load the daily rainfall statistics for the city of Seattle in 2014 using pandas.

### Import data from the Strata Scratch platform


```python
rainfall = pd.read_csv('data/seattle_2014.csv')
```


```python
inches = rainfall['prcp'] / 254.0  # 1/10mm -> inches
inches.shape
```

The array contains 365 values, giving daily rainfall in inches from January 1 to December 31, 2014.

As a first quick visualization, let's look at the histogram of rainy days, which was generated using Matplotlib.

```python
plt.hist(inches, 40);
```

This histogram gives us a general idea of what the data looks like: despite its reputation, the vast majority of days in Seattle saw near zero measured rainfall in 2014.
But this doesn't do a good job of conveying some information we'd like to see: for example, how many rainy days were there in the year? What is the average precipitation on those rainy days? How many days were there with more than half an inch of rain?

## Comparison Operators as ufuncs

We introduced ufuncs, and focused in particular on arithmetic operators. We saw that using ``+``, ``-``, ``*``, ``/``, and others on arrays leads to element-wise operations.
NumPy also implements comparison operators such as ``<`` (less than) and ``>`` (greater than) as element-wise ufuncs.
The result of these comparison operators is always an array with a Boolean data type.
All six of the standard comparison operations are available:

```python
x = np.array([1, 2, 3, 4, 5])
x < 3  # less than
x > 3  # greater than
x <= 3  # less than or equal
x >= 3  # greater than or equal
x != 3  # not equal
x == 3  # equal
```

It is also possible to do an element-wise comparison of two arrays, and to include compound expressions:

```python
(2 * x) == (x ** 2)
```

As in the case of arithmetic operators, the comparison operators are implemented as ufuncs in NumPy; for example, when you write ``x < 3``, internally NumPy uses ``np.less(x, 3)``.

A summary of the comparison operators and their equivalent ufunc is shown here:

| Operator	    | Equivalent ufunc    || Operator	   | Equivalent ufunc    |
|---------------|---------------------||---------------|---------------------|
|``==``         |``np.equal``         ||``!=``         |``np.not_equal``     |
|``<``          |``np.less``          ||``<=``         |``np.less_equal``    |
|``>``          |``np.greater``       ||``>=``         |``np.greater_equal`` |


Just as in the case of arithmetic ufuncs, these will work on arrays of any size and shape.
Here is a two-dimensional example:

```python
rng = np.random.RandomState(0)
x = rng.randint(10, size=(3, 4))
x
x < 6
```

In each case, the result is a Boolean array, and NumPy provides a number of straightforward patterns for working with these Boolean results.

## Boolean Arrays as Masks

In the preceding section we looked at aggregates computed directly on Boolean arrays.
A more powerful pattern is to use Boolean arrays as masks, to select particular subsets of the data themselves.
Returning to our ``x`` array from before, suppose we want an array of all values in the array that are less than, say, 5:

```python
x
```

We can obtain a Boolean array for this condition easily, as we've already seen:

```python
x < 5
```

Now to *select* these values from the array, we can simply index on this Boolean array; this is known as a *masking* operation:

```python
x[x < 5]
```

What is returned is a one-dimensional array filled with all the values that meet this condition; in other words, all the values in positions at which the mask array is ``True``.

We are then free to operate on these values as we wish.
For example, we can compute some relevant statistics on our Seattle rain data:

```python
# construct a mask of all rainy days
rainy = (inches > 0)

# construct a mask of all summer days (June 21st is the 172nd day)
days = np.arange(365)
summer = (days > 172) & (days < 262)

print("Median precip on rainy days in 2014 (inches):   ", np.median(inches[rainy]))
print("Median precip on summer days in 2014 (inches):  ", np.median(inches[summer]))
print("Maximum precip on summer days in 2014 (inches): ", np.max(inches[summer]))
print("Median precip on non-summer rainy days (inches):", np.median(inches[rainy & ~summer]))
```

By combining Boolean operations, masking operations, and aggregates, we can very quickly answer these sorts of questions for our dataset.


# Practice Tasks
## 1. Create a boolean mask of x for values less than or equal to 2.

```python
x = np.arange(-3, 5)
# START YOUR CODE HERE.
x[x<=2]
```

## 2. Create a boolean mask of x for values equal to -1.

```python
# START YOUR CODE HERE.
x==-1
```

## 3. Create a boolean mask of x for all positive values.

```python
# START YOUR CODE HERE.
x>0
```

## 4. Create a boolean mask of x for all even values. (Hint:  Modulo)

```python
# START YOUR CODE HERE.
x % 2 == 0
```

## 5. Create a boolean mask 'greater' of x for values greater than 4. Create an array of x for values greater than four using a masking operation.

```python
np.random.seed(1)  # seed for reproducibility
x = np.random.randint(10, size=(3, 4))
# START YOUR CODE HERE.
greater = x > 4
x[greater]
```

## 6. Create a boolean mask 'odd' of x for all odd values. Create an array of x for those odd values using a masking operation.

```python
# START YOUR CODE HERE.
odd = x%2 !=0
x[odd]
```

## 7. Create an array of x containing all values that are greater than 4 and are not odd using boolean operators and a masking operation.

```python
# START YOUR CODE HERE.
greater = x>4
odd = x%2 != 0
x[greater & ~odd]
```

