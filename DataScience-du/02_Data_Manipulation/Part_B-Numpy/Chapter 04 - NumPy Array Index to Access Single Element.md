# Chapter 04 - NumPy Array Index to Access Single Element 
### Hey Techie,   
Welcome to the fourth notebook of this Numpy tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://www.youtube.com/watch?v=sKMuioo7Xf8. Today's video explains the fundamentals of indexing arrays. In the end, please try to solve the presented tasks. In case you are interested, you find a complete walk through the tasks at: https://youtu.be/Yk3H3VRDfm0 (*relevant part starting at 6:15 min*). 

## Have fun! :-)   
*Video length in total*: 13 minutes   
*Self-study time*: 13 minutes   
*Total*: **26 minutes**   
## Credits
Complete Python Numpy Tutorial for Beginners, Nate at StrataScratch, https://www.youtube.com/channel/UCW8Ews7tdKKkBT6GdtQaXvQ.

## Array Indexing: Accessing Single Elements

If you are familiar with Python's standard list indexing, indexing in NumPy will feel quite familiar.
In a one-dimensional array, the $i^{th}$ value (counting from zero) can be accessed by specifying the desired index in square brackets, just as with Python lists:


```python
x1
```


```python
x1[0]
```

To index from the end of the array, you can use negative indices:


```python
x1
```


```python
x1[-1]
```

In a multi-dimensional array, items can be accessed using a comma-separated tuple of indices:


```python
x2 #size = (3,4) (rows,columns)
```


```python
x2[0, 0]
```


```python
x2[2, 0]
```


```python
x2[2, -1]
```

Values can also be modified using any of the above index notation:


```python
x2
```


```python
x2[0, 0] = 12
```


```python
x2[2,-1] = 0
x2
```

Keep in mind that, unlike Python lists, NumPy arrays have a fixed type.
This means, for example, that if you attempt to insert a floating-point value to an integer array, the value will be silently truncated. Don't be caught unaware by this behavior!


```python
x1[0] = 3.14159  # this will be truncated!
x1
```


```python
x1.dtype
```


# Practice Tasks   

## For the following six tasks, refer to the arrays created below. Run this code to get started.


```python
np.random.seed(1)  # seed for reproducibility
x1 = np.random.randint(10, size=9)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 3))  # Two-dimensional array
```

## 1. Print the first element of x1.


```python
# START YOUR CODE HERE.
x1[0]
```


## 2. Print the fifth element of x1.


```python
# START YOUR CODE HERE.
x1[4]
```


## 3. Print the second to last element of x1 using negative indicies.


```python
# START YOUR CODE HERE.
x1[-2]
```


## 4. Print the element at position (0,2) of x2.


```python
# START YOUR CODE HERE.
x2[0,2]
```


## 5. Print the second element of the last row of x2 using positive and negative indicies.


```python
# START YOUR CODE HERE.
x2[-1, 1]
```


## 6. Assign a value of 25 to the first element of the last row of x2.


```python
# START YOUR CODE HERE.
x2[-1, 0] = 25
```


