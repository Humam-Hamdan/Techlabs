
# Chapter 1 - List vs. Array in Python
## Hey Techie,   
Welcome to the first notebook of this Numpy tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/OVD26YMkT_c. Today's video explains the differences between built-in lists in Python and Numpy arrays. In the end, please try to solve the presented tasks. In case you are interested, you find a complete walk through the tasks at: https://youtu.be/mkbgEvUkSaM. 

## Have fun! :-)   
*Video length in total*: 15 minutes   
*Self-study time*: 15 minutes   
*Total*: **30 minutes**   
## Credits
Complete Python Numpy Tutorial for Beginners, Nate at StrataScratch, https://www.youtube.com/channel/UCW8Ews7tdKKkBT6GdtQaXvQ.

# Intro to NumPy (Numerical Python)

NumPy is the fundamental package for scientific computing in Python. NumPy is used in many other packages in python even though you may not see it explicitly running in your code.

It is a python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

NumPy arrays form the core of nearly the entire ecosystem of data science tools in Python, so time spent learning to use NumPy effectively will be valuable no matter what aspect of data science interests you.

# Notes:

- 

# Lists in Python

- Natively built into python and doesn't require you to import libraries to use the functionality
- Lists are great to store values collectively and retrieve data easily

#### We can create list of integers


```python
#manual way of creating lists
A = [10, 11, 12, 13, 14]
```


```python
#create lists using functions
L = list(range(10))
L
```


```python
#find the data type of a list
type(L[0])
```

#### We can create a list of strings


```python
L2 = [str(c) for c in L]
L2
```


```python
type(L2[0])
```

#### We can create heterogeneous lists


```python
L3 = [True, "2", 3.0, 4]
[type(item) for item in L3]
```

## Arrays in Python

What is an array?

- An array is a data structure that allows you to store values...like a list

How is it different than a list?
- An array is more efficient at storing large amounts of data
- Easy and simple to perform numerical/math operations

### Creating Arrays From Python Lists

#### Use np.array to create arrays from Python lists


```python
# integer array
listA = [1,4,2,5,3]
numpyarrayA = np.array(listA)
numpyarrayA
```

#### Numpy is constrained to arrays that all contain the same type. If the types do not match, NumPy will try to change the data type


```python
np.array([3.14, 4, 2, 3])
```

#### Numpy allows you to make multidimensional arrays using lists of lists


```python
np.array([[1, 2, 3], 
          [3, 4],
          [3, 3]])
```


# Practice Tasks

#### 1. Create a list containing the values 1, 3, and 5.


```python
# START YOUR CODE HERE.

```


#### 2. Create a list containing the values from 0 to 9 using the range function and assign it to *L*.


```python
# START YOUR CODE HERE.

```


#### 3. Print the first element from *L*.


```python
# START YOUR CODE HERE.

```


#### 4. Create an array containing the values [5, 4, 3, 2, 1] and store is in *A*.


```python
# START YOUR CODE HERE.

```


#### 5. Print the datatype of array *A*.


```python
# START YOUR CODE HERE.

```


#### 6. What is the expected datatype of this array? Why? Enter the expected datatype between quotation marks


```python
A2 = np.array([3.14, 4, 2, 3])
# START YOUR CODE HERE.
A2.dtype == ''
```


#### 7. For practice reasons, create a multidimesional array from a multidimesional list. 


```python
# START YOUR CODE HERE.

```


