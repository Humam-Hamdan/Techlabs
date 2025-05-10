```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/02_Data\ Manipulation/Part\ B\ -\ Numpy
```


```python
# ALWAYS IMPORT NUMPY FIRST.
import numpy as np
```

# Chapter 5 - NumPy Slicing and Accessing Subarrays
### Hey Techie,   
Welcome to the fifth notebook of this Numpy tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/01kOJUiiEQE. Today's video explains how to access subarrays. In the end, please try to solve the presented tasks. In case you are interested, you find a complete walk through the tasks at: https://youtu.be/STJA-D-K9Cs. 

#### Have fun! :-)   
*Video length in total*: 26 minutes   
*Self-study time*: 26 minutes   
*Total*: **52 minutes**   
#### Credits
Complete Python Numpy Tutorial for Beginners, Nate at StrataScratch, https://www.youtube.com/channel/UCW8Ews7tdKKkBT6GdtQaXvQ.
<hr style="border:2px solid gray"> </hr>   

## Array Slicing: Accessing Subarrays

Just as we can use square brackets to access individual array elements, we can also use them to access subarrays with the *slice* notation, marked by the colon (``:``) character.
The NumPy slicing syntax follows that of the standard Python list; to access a slice of an array ``x``, use this:
``` python
x[start:stop:step]
```
If any of these are unspecified, they default to the values ``start=0``, ``stop=``*``size of dimension``*, ``step=1``.
We'll take a look at accessing sub-arrays in one dimension and in multiple dimensions.

### One-dimensional subarrays


```python
x = np.arange(10,20)
x
```


```python
x[:5]  # first five elements
```


```python
x[5:10:1]  # elements after index 5
```


```python
x[4:7]  # middle sub-array
```


```python
x[::2]  # every other element
```


```python
x[1::2]  # every other element, starting at index 1
```

A potentially confusing case is when the ``step`` value is negative.
In this case, the defaults for ``start`` and ``stop`` are swapped.
This becomes a convenient way to reverse an array:


```python
x[::-1]  # all elements, reversed
```


```python
x[5::-2]  # reversed every other from index 5
```

### Multi-dimensional subarrays

Multi-dimensional slices work in the same way, with multiple slices separated by commas.
For example:


```python
x2[:2, :3]  # two rows, three columns
```


```python
x2[:3, ::2]  # all rows, every other column
```

Finally, subarray dimensions can even be reversed together:


```python
x2[::-1, ::-1]
```

#### Accessing array rows and columns

One commonly needed routine is accessing of single rows or columns of an array.
This can be done by combining indexing and slicing, using an empty slice marked by a single colon (``:``):


```python
x2[:, 0]  # first column of x2
```


```python
x2[0, :]  # first row of x2
```

In the case of row access, the empty slice can be omitted for a more compact syntax:


```python
x2[0]  # equivalent to x2[0, :]
```

<hr style="border:2px solid gray"> </hr>   

## Practice Tasks

#### For the following six tasks, refer to the arrays created below. Run this code to get started.


```python
np.random.seed(1)  # seed for reproducibility
x1 = np.random.randint(10, size=9)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 3))  # Two-dimensional array
```

#### 1. Create a slice containing the last 5 elements of x1.


```python
# START YOUR CODE HERE.

```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>x1[-5:]</code>
</p>
</details>

#### 2. Create a slice containing every third element starting at the second element  of x1.


```python
# START YOUR CODE HERE.

```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>x1[1::3]</code>
</p>
</details>

#### 3. Create a slice where x1 has been reversed.


```python
# START YOUR CODE HERE.

```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>x1[::-1]</code>
</p>
</details>

#### 4. Create a slice containing the first two rows and first column of x2.


```python
# START YOUR CODE HERE.

```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>x2[[0, 1], 0]</code>
</p>
</details>

#### 5. Create a slice where the rows have been reversed for x2.


```python
# START YOUR CODE HERE.

```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>x2[::-1,:]</code>
</p>
</details>

#### 6. Print the first column of x2.


```python
# START YOUR CODE HERE.

```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>print(x2[:, 0])</code>
</p>
</details>

#### 7. Print the first row of x2.


```python
# START YOUR CODE HERE.

```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>print(x2[0, :])</code>
</p>
</details>
