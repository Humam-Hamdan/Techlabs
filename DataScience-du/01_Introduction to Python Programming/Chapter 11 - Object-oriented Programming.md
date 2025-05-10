```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/01_Introduction\ to\ Python\ Programming
```

# Chapter 11 - Object-oriented Programming
### Hey Techie,   
Welcome to the final notebook of this Python tutorial series. We encourage you to take this notebook as a template to code along the instruction videos, which you may find at: https://www.py4e.com/lessons/Objects. Today's four videos deal with concept of object-oriented programming. In the end, please try to solve the presented task. As PY4E does not offer an auto-graded assigment for this lecture, you can only double-check your results using the provided test cases.

#### Have fun! :-)   
*Video length in total*: 30 minutes   
*Self-study time*: 30 minutes   
*Total*: **60 minutes**   
#### Credits
Python for Everybody, Dr. Chuck Severance, https://www.py4e.com/, CC.
<hr style="border:2px solid gray"> </hr>   
   
## Object-oriented Programming - Part 1


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   
   
## Object-oriented Programming - Part 2


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   
   
## Object-oriented Programming - Part 3


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   
   
## Object-oriented Programming - Part 4


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>  

## Practice Task   
#### 1. Write a class Techie that has four global attributes (part of self) name (str), age (int), profession (str), and location (str). Additionally, write four methods that print one of the global attributes respectively named *get_name*, *get_age*, *get_profession*, and *get_location*.
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>Use the built-in input method to read hours and rate per hour separately.</li>
        <li>Typecast both inputs to floats.</li>
        <li>Print the result by multiplying the hours with their rate per hour using the *-operator.</li>
    </ul>
</p>
</details>


```python
# START YOUR CODE HERE.

```


```python
# ENTER YOUR ATTRIBUTES HERE.
techie = Techie(name = "YourName", age = 99, profession = "YourProfession", location = "YourLocation")
# IF ALL FOUR ATTRIBUTES ARE PRINTED, EVERYTHING WORKS FINE!
techie.get_name()
techie.get_age()
techie.get_profession()
techie.get_location()
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Sample Solution (click to expand)</b></font>
</summary>
<p>
    <code>class Techie:</code><br />
    <code></code><br />
    <code>def __init__(self, name: str, age: int, profession: str, location: str):</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;self.name = name</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;self.age = age</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;self.profession = profession</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;self.location = location</code><br />
    <code></code><br />
    <code>def get_name(self):</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;print("My name is", self.name, ".")</code><br />
    <code></code><br />
    <code>def get_age(self):</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;print("I am", self.age, "years old!")</code><br />
    <code></code><br />
    <code>def get_profession(self):</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;print("I am a/an", self.profession, ".")</code><br />
    <code></code><br />    
    <code>def get_location(self):</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;print("I participate at TechLabs", self.location, ".")</code>
</p>
</details> 
