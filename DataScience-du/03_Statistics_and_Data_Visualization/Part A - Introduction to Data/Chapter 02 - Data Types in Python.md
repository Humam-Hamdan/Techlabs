```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/03_Statistics\ and\ Data\ Visualization/Part\ A\ -\ Introduction\ to\ Data
```

# Chapter 2 - Data Types in Python   
### Hey Techie,
Welcome to the second notebook of this part. Its contents refer to a video which you may find under: https://www.coursera.org/learn/understanding-visualization-data/lecture/WmlLl/data-types-in-python. To access this video, you need to audit the Understanding and Visualizing Data with Python course (https://www.coursera.org/learn/understanding-visualization-data) on Coursera first.   
We encourage you to take this notebook as a template to code along the instruction video and try things out for yourself.
#### Have fun! :-)   

### Credits
Understanding and Visualizing Data with Python, University of Michigan (Coursera), https://www.coursera.org/learn/understanding-visualization-data
   
<hr style="border:2px solid gray"> </hr>   
   
## Notes

* Take notes here.
    * And here.
* ...
* ...

<hr style="border:2px solid gray"> </hr>   

## Data Types in Python 


```python
import math
```

The following data types can be used in base python:
* **boolean**
* **integer**
* **float**
* **string**
* **list**
* **None**
* complex
* object
* set
* dictionary

We will only focus on the **bolded** ones

Let's connect these data types to the the variable types we learned from the [Variable Types video](https://www.coursera.org/learn/understanding-visualization-data/lecture/iDodZ/variable-types).

###  Numerical or Quantitative (taking the mean makes sense)
* Discrete
    * Integer (int) # Stored exactly
* Continuous
    * Float (float) # Stored similarly to scientific notation. Allows for decimal places but loses precision.


```python
type(4)
```


```python
type(0)
```


```python
type(-3)
```


```python
#try taking the mean
numbers = [2, 3, 4, 5]
print(sum(numbers)/len(numbers))
type(sum(numbers)/len(numbers)) #In Python 3 returns float, but in Python 2 would return int
```

**Floats**


```python
3/5
```


```python
6*10**(-1)
```


```python
type(3/5)
```


```python
type(math.pi)
```


```python
type(4.0)
```


```python
# Try taking the mean
numbers = [math.pi, 3/5, 4.1]
type(sum(numbers)/len(numbers))
```

### Categorical or Qualitative
* Nominal
    * Boolean (bool)
    * String (str)
    * None (NoneType)
* Ordinal
    * Only defined by how you use the data
    * Often important when creating visuals
    * Lists can hold ordinal information because they have indices

**Boolean**


```python
# Boolean
type(True)
```


```python
# Boolean
if 6 < 5:
    print("Yes!")
```


```python
myList = [True, 6<5, 1==3, None is None]
for element in myList:
    print(type(element))
```


```python
print(sum(myList)/len(myList))
type(sum(myList)/len(myList))
```

**String**


```python
type("This sentence makes sense")
```


```python
type("Makes sentense this sense")
```


```python
type("math.pi")
```


```python
strList = ['dog', 'koala', 'goose']
sum(strList)/len(strList)
```

**Nonetype**


```python
# None
type(None)
```


```python
# None
x = None
type(x)
```


```python
noneList = [None]*5
sum(noneList)/len(noneList)
```

**Lists**

A list can hold many types and can also be used to store ordinal information.


```python
# List
myList = [1, 1.1, "This is a sentence", None]
for element in myList:
    print(type(element))
```


```python
sum(myList)/len(myList)
```


```python
# List
myList = [1, 2, 3]
for element in myList:
    print(type(element))
sum(myList)/len(myList) # note that this outputs a float
```


```python
myList = ['third', 'first', 'medium', 'small', 'large']
myList[0]
```


```python
myList.sort()
myList
```

There are more datatypes available when using different libraries such as Pandas and Numpy, which we will introduce to you as we use them.
