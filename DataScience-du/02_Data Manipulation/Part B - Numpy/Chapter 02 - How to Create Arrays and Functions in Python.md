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

# Chapter 2 - How to Create Arrays and Functions in Python
### Hey Techie,   
Welcome to the second notebook of this Numpy tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/F5sKh-3V3KA. Today's video explains multiple options on how to create Numpy arrays. In the end, please try to solve the presented tasks. In case you are interested, you find a complete walk through the tasks at: https://youtu.be/yLn52ppKO80. 

#### Have fun! :-)   
*Video length in total*: 15 minutes   
*Self-study time*: 15 minutes   
*Total*: **30 minutes**   
#### Credits
Complete Python Numpy Tutorial for Beginners, Nate at StrataScratch, https://www.youtube.com/channel/UCW8Ews7tdKKkBT6GdtQaXvQ.
<hr style="border:2px solid gray"> </hr>   

### Creating Arrays from Scratch

#### Especially for larger arrays, it's more efficient to create arrays from scratch using functions built into NumPy


```python
# create an integer array with 10 zeros
np.zeros(10, dtype=int)
```


```python
# create a 3x5 float-ing point array filled with 1s
np.ones((3,5), dtype=float)
```


```python
# create a 3x5 array filled with 3.14
np.full((3,5), 3.14)
```


```python
# create an array filled with a linear sequence
# starting at 0, ending at 20, stepping by 2
np.arange(0, 20, 2)
```


```python
# create an array of five values evenly spaced between 0 and 1
np.linspace(0, 1, 5)
```


```python
# create a 3x3 array of uniformly distributed random values between 0 and 1
np.random.random((3,3))
```


```python
# create a 3x3 array of normally distributed random values
# with mean 0 and standard deviation 1
# np.random.normal(mean,std,array size)

np.random.normal(0, 1, (3, 3))
```


```python
# create a 3x3 array of random integers in the interval [0, 10)
# np.random.randint(start value, stop value, array size)
np.random.randint(0, 10, (3,3))
```


```python
# create a 3x3 identity matrix
np.eye(5)
```


```python
# create an uninitialized array of three integers
# the values will be whatever happens to already exist at that memory location
np.empty(5)
```

## NumPy Standard Data Types

NumPy arrays contain values of a single type, so it is important to have detailed knowledge of those types and their limitations.
Because NumPy is built in C, the types will be familiar to users of C, Fortran, and other related languages.

The standard NumPy data types are listed in the following table.
Note that when constructing an array, they can be specified using a string:

```python
np.zeros(10, dtype='int16')
```

Or using the associated NumPy object:

```python
np.zeros(10, dtype=np.int16)
```


```python
a = np.zeros(10, dtype='int16')
a
```


```python
a.dtype
```

| Data type	    | Description |
|---------------|-------------|
| ``bool_``     | Boolean (True or False) stored as a byte |
| ``int_``      | Default integer type (same as C ``long``; normally either ``int64`` or ``int32``)| 
| ``intc``      | Identical to C ``int`` (normally ``int32`` or ``int64``)| 
| ``intp``      | Integer used for indexing (same as C ``ssize_t``; normally either ``int32`` or ``int64``)| 
| ``int8``      | Byte (-128 to 127)| 
| ``int16``     | Integer (-32768 to 32767)|
| ``int32``     | Integer (-2147483648 to 2147483647)|
| ``int64``     | Integer (-9223372036854775808 to 9223372036854775807)| 
| ``uint8``     | Unsigned integer (0 to 255)| 
| ``uint16``    | Unsigned integer (0 to 65535)| 
| ``uint32``    | Unsigned integer (0 to 4294967295)| 
| ``uint64``    | Unsigned integer (0 to 18446744073709551615)| 
| ``float_``    | Shorthand for ``float64``.| 
| ``float16``   | Half precision float: sign bit, 5 bits exponent, 10 bits mantissa| 
| ``float32``   | Single precision float: sign bit, 8 bits exponent, 23 bits mantissa| 
| ``float64``   | Double precision float: sign bit, 11 bits exponent, 52 bits mantissa| 
| ``complex_``  | Shorthand for ``complex128``.| 
| ``complex64`` | Complex number, represented by two 32-bit floats| 
| ``complex128``| Complex number, represented by two 64-bit floats| 

<hr style="border:2px solid gray"> </hr>   

## Practice Tasks

#### 1. Create an integer array with 100 ones.


```python
# START YOUR CODE HERE.

```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>np.ones(100)</code><br />
</p>
</details>

#### 2. Create a (4, 3) float array filled with zeros.


```python
# START YOUR CODE HERE.

```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>np.zeros((4, 3), dtype = "float64")</code><br />
</p>
</details>

#### 3. Create a (5, 2) array filled with 6.28.


```python
# START YOUR CODE HERE.

```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>np.full((5, 2), 6.28)</code><br />
</p>
</details>

#### 4. Create an array filled with a linear sequence, started at 0, ending at 30, stepping by 3.


```python
# START YOUR CODE HERE.

```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>np.array(range(0, 31, 3))</code><br />
</p>
</details>

#### 5. Create an array of 9 evenly  spaced values between 0 and 64 inclusive.


```python
# START YOUR CODE HERE.

```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>np.linspace(0, 64, 9)</code><br />
</p>
</details>


#### 6. Create a (5, 2) array of uniformaly distributed random values between 0 and 1.


```python
# START YOUR CODE HERE.

```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>np.random.random((5, 2))</code><br />
</p>
</details>

#### 7. Create an array of 10 random integers in the interval [0, 5].


```python
# START YOUR CODE HERE.

```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>np.random.randint(0, 6, 10)</code><br />
</p>
</details>

#### 8. Create a (4, 4) identity matrix.


```python
# START YOUR CODE HERE.

```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>np.eye(4)</code><br />
</p>
</details>
