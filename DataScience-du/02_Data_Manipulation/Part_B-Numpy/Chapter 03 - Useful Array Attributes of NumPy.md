# Chapter 03 - Useful Array Attributes of NumPy
## Hey Techie,   
Welcome to the first notebook of this Numpy tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/aGPjAOhomY4. Today's video explains how to assess different important attributes from Numpy arrays. In the end, please try to solve the presented tasks. In case you are interested, you find a complete walk through the tasks at: https://youtu.be/Yk3H3VRDfm0 (*relevant part until 6:15 min*). 

## Have fun! :-)   
*Video length in total*: 11 minutes   
*Self-study time*: 11 minutes   
*Total*: **22 minutes**   
## Credits
Complete Python Numpy Tutorial for Beginners, Nate at StrataScratch, https://www.youtube.com/channel/UCW8Ews7tdKKkBT6GdtQaXvQ.

# The Basics of NumPy Arrays

Data manipulation in Python is nearly synonymous with NumPy array manipulation: even newer tools like Pandas are built around the NumPy array.
We'll present several examples of using NumPy array manipulation to access data and subarrays, and to split, reshape, and join the arrays.
While the types of operations shown here may seem a bit dry and pedantic, they comprise the building blocks of many other examples used in python.

We'll cover a few categories of basic array manipulations here:

- *Attributes of arrays*: Determining the size, shape, memory consumption, and data types of arrays
- *Indexing of arrays*: Getting and setting the value of individual array elements
- *Slicing of arrays*: Getting and setting smaller subarrays within a larger array
- *Reshaping of arrays*: Changing the shape of a given array
- *Joining and splitting of arrays*: Combining multiple arrays into one, and splitting one array into many

## NumPy Array Attributes

First let's discuss some useful array attributes.
We'll start by defining three random arrays, a one-dimensional, two-dimensional, and three-dimensional array.
We'll use NumPy's random number generator, which we will *seed* with a set value in order to ensure that the same random arrays are generated each time this code is run:

```python
np.random.seed(0)  # seed for reproducibility

x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array
```

Each array has attributes ``ndim`` (the number of dimensions), ``shape`` (the size of each dimension), and ``size`` (the total size of the array):


```python
print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)
```

Another useful attribute is the ``dtype``, the data type of the array


```python
print("dtype:", x3.dtype)
```

Other attributes include ``itemsize``, which lists the size (in bytes) of each array element, and ``nbytes``, which lists the total size (in bytes) of the array:


```python
print("itemsize:", x3.itemsize, "bytes")
print("nbytes:", x3.nbytes, "bytes")
```

In general, we expect that ``nbytes`` is equal to ``itemsize`` times ``size``.

<hr style="border:2px solid gray"> </hr>   

## Practice Tasks

#### For the following tasks 1, 2, and 3, refer to the array created below. Run this code to get started.


```python
np.random.seed(1)  # seed for reproducibility
x = np.random.randint(10, size=(3, 3))  # Two-dimensional array
```

#### 1. Print the *ndim*, *shape*, and *size* attributes of *x*. The print code has already been created for you.


```python
# INSERT YOUR CODE BELOW.
print("x2 ndim: ", )
print("x2 shape:", )
print("x2 size: ", )
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>print("x2 ndim: ", x.ndim)</code><br />
    <code>print("x2 shape:", x.shape)</code><br />
    <code>print("x2 size: ", x.size)</code><br />
</p>
</details>


#### 2. Print the *dtype* of x.


```python
# INSERT YOUR CODE BELOW.
print("dtype:", )
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>print("dtype:", x.dtype)</code>
</p>
</details>


#### 3. Print the *itemsize* and *nbytes* of x.


```python
# INSERT YOUR CODE BELOW.
print("itemsize:", , "bytes")
print("nbytes:", , "bytes")
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>print("itemsize:", x.itemsize , "bytes")</code><br />
    <code>print("nbytes:", x.nbytes , "bytes")</code>
</p>
</details>
