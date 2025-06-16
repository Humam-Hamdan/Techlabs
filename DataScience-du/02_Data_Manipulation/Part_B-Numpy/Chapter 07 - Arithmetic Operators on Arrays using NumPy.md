# Chapter 7 - Arithmetic Operators on Arrays using NumPy
## Hey Techie,   
Welcome to the seventh notebook of this Numpy tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/JZfsZuLKaJ4. Today's video explains how to apply different arithmetic operations on Numpy arrays. In the end, please try to solve the presented tasks. In case you are interested, you find a complete walk through the tasks at: https://youtu.be/ccDPI7v-0QE. 

## Have fun! :-)   
*Video length in total*: 26 minutes   
*Self-study time*: 26 minutes   
*Total*: **52 minutes**   
## Credits
Complete Python Numpy Tutorial for Beginners, Nate at StrataScratch, https://www.youtube.com/channel/UCW8Ews7tdKKkBT6GdtQaXvQ.

# Computation on NumPy Arrays: Universal Functions

Up until now, we have been discussing some of the basic nuts and bolts of NumPy; in the next few sections, we will dive into the reasons that NumPy is so important in the Python data science world.
Namely, it provides an easy and flexible interface to optimized computation with arrays of data.

Computation on NumPy arrays can be very fast, or it can be very slow.
The key to making it fast is to use *vectorized* operations, generally implemented through NumPy's *universal functions* (ufuncs).
This section motivates the need for NumPy's ufuncs, which can be used to make repeated calculations on array elements much more efficient.
It then introduces many of the most common and useful arithmetic ufuncs available in the NumPy package.

Vectorized operations in NumPy are implemented via *ufuncs*, whose main purpose is to quickly execute repeated operations on values in NumPy arrays.
Ufuncs are extremely flexible – before we saw an operation between a scalar and an array, but we can also operate between two arrays:


```python
import numpy as np
```


```python
np.arange(5) / np.arange(1, 6)
```

And ufunc operations are not limited to one-dimensional arrays–they can also act on multi-dimensional arrays as well:

```python
x = np.arange(9).reshape((3, 3))
2 ** x
```

## Exploring NumPy's UFuncs

Ufuncs exist in two flavors: *unary ufuncs*, which operate on a single input, and *binary ufuncs*, which operate on two inputs.
We'll see examples of both these types of functions here.

### Array arithmetic

NumPy's ufuncs feel very natural to use because they make use of Python's native arithmetic operators.
The standard addition, subtraction, multiplication, and division can all be used:

```python
x = np.arange(4)
print("x     =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
print("x // 2 =", x // 2)  # floor division
```

There is also a unary ufunc for negation, and a ``**`` operator for exponentiation, and a ``%`` operator for modulus:

```python
print("-x     = ", -x)
print("x ** 2 = ", x ** 2)
print("x % 2  = ", x % 2)
```

In addition, these can be strung together however you wish, and the standard order of operations is respected:

```python
-(0.5*x + 1) ** 2
```

Each of these arithmetic operations are simply convenient wrappers around specific functions built into NumPy; for example, the ``+`` operator is a wrapper for the ``add`` function:

```python
np.add(x, 2)
```

The following table lists the arithmetic operators implemented in NumPy:

| Operator	    | Equivalent ufunc    | Description                           |
|---------------|---------------------|---------------------------------------|
|``+``          |``np.add``           |Addition (e.g., ``1 + 1 = 2``)         |
|``-``          |``np.subtract``      |Subtraction (e.g., ``3 - 2 = 1``)      |
|``-``          |``np.negative``      |Unary negation (e.g., ``-2``)          |
|``*``          |``np.multiply``      |Multiplication (e.g., ``2 * 3 = 6``)   |
|``/``          |``np.divide``        |Division (e.g., ``3 / 2 = 1.5``)       |
|``//``         |``np.floor_divide``  |Floor division (e.g., ``3 // 2 = 1``)  |
|``**``         |``np.power``         |Exponentiation (e.g., ``2 ** 3 = 8``)  |
|``%``          |``np.mod``           |Modulus/remainder (e.g., ``9 % 4 = 1``)|


### Absolute value

Just as NumPy understands Python's built-in arithmetic operators, it also understands Python's built-in absolute value function:

```python
x = np.array([-2, -1, 0, 1, 2])
abs(x)
```

The corresponding NumPy ufunc is ``np.absolute``, which is also available under the alias ``np.abs``:

```python
np.absolute(x)
np.abs(x)
```

This ufunc can also handle complex data, in which the absolute value returns the magnitude:

```python
x = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j])
np.abs(x)
```

### Trigonometric functions

NumPy provides a large number of useful ufuncs, and some of the most useful for the data scientist are the trigonometric functions.
We'll start by defining an array of angles:

```python
theta = np.linspace(0, np.pi, 3)
```

Now we can compute some trigonometric functions on these values:

```python
print("theta      = ", theta)
print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))
```

The values are computed to within machine precision, which is why values that should be zero do not always hit exactly zero.
Inverse trigonometric functions are also available:

```python
x = [-1, 0, 1]
print("x         = ", x)
print("arcsin(x) = ", np.arcsin(x))
print("arccos(x) = ", np.arccos(x))
print("arctan(x) = ", np.arctan(x))
```

### Exponents and logarithms

Another common type of operation available in a NumPy ufunc are the exponentials:

```python
x = [1, 2, 3]
print("x     =", x)
print("e^x   =", np.exp(x))
print("2^x   =", np.exp2(x))
print("3^x   =", np.power(3, x))
```

The inverse of the exponentials, the logarithms, are also available.
The basic ``np.log`` gives the natural logarithm; if you prefer to compute the base-2 logarithm or the base-10 logarithm, these are available as well:

```python
x = [1, 2, 4, 10]
print("x        =", x)
print("ln(x)    =", np.log(x))
print("log2(x)  =", np.log2(x))
print("log10(x) =", np.log10(x))
```

There are also some specialized versions that are useful for maintaining precision with very small input:

```python
x = [0, 0.001, 0.01, 0.1]
print("exp(x) - 1 =", np.expm1(x))
print("log(1 + x) =", np.log1p(x))
```

When ``x`` is very small, these functions give more precise values than if the raw ``np.log`` or ``np.exp`` were to be used.

# Practice Tasks   

## 1. Add 2 to every element in *x*, subtract 2 from every element in *x*, multiply every element in *x* with 3.

```python
x = np.arange(9)
# INSERT CODE BELOW.
print("Add 2:", x+2)
print("Subtract 2:", x-2)
print("Multiply 3:", 3*x)
```

## 2. Negate every element in *x*, cube every element in *x*, calcualte the remainder if you divide every element by 4 in *x*.

```python
# INSTERT CODE BELOW.
print("Negation:", -x)
print("Cubed:", x ** 3)
print("Mod 4:", x % 4)
```

## 3. Print the absolute value for every element in *x*.

```python
x = np.arange(-4, 5)
# START YOUR CODE HERE.
abs(x)
```

## 4. Print the results sine, cosine, and tangent on the elements of *theta*.

```python
theta = np.linspace(0, np.pi, 3)
# INSERT CODE BELOW.
print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))
```

## 5. Print the results arcsine, arccosine, and arctangent on the elements of *x*.

```python
x = [-1, 0, 1]
# INSERT CODE BELOW.
print("arcsin(x) = ", np.arcsin(x))
print("arccos(x) = ", np.arccos(x))
print("arctan(x) = ", np.arctan(x))
```

## 6. Print the results of e^x, 2^x, and 5^x.

```python
x = [1, 2, 3]
# INSERT CODE BELOW.
print("e^x =", np.exp(x))
print("2^x =", np.exp2(x))
print("5^x =", np.power(5,x))
```

## 7. Print the results of ln, log 2, and log 10 on x.

```python
x = [1, 2, 4, 10]
# INSERT CODE BELOW.
print("ln(x) =", np.log(x))
print("log2(x) =", np.log2(x))
print("log10(x) =", np.log10(x))
```

## 8. Print the results of exp(z) - 1 and expm1(z) to see that expm1 is more precise.

```python
z = [0, 0.0000000001, 0.000000001, 0.00000001]
# INSERT CODE BELOW.
print("(e^z)-1 =", np.exp(z)-1)
print("(e^z)-1 =", np.expm1(z))
```

