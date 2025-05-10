```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/01_Introduction\ to\ Python\ Programming
```

# Chapter 4 - Loops and Iterations
### Hey Techie,   
Welcome to the fourth notebook of this Python tutorial series. We encourage you to take this notebook as a template to code along the instruction videos, which you may find at: https://www.py4e.com/lessons/loops. Today's four videos deal with how Python repeats statements using looping structures. There is no need to watch the worked exercise. In the end, please try to solve the presented task. If you want to double-check your results, you may also upload them to PY4E. For that, a Google Account is required. On the website, you find the auto-graded code tasks at the very end of each lesson.

#### Have fun! :-)   
*Video length in total*: 45 minutes   
*Self-study time*: 45 minutes   
*Total*: **90 minutes**   
#### Credits
Python for Everybody, Dr. Chuck Severance, https://www.py4e.com/, CC.
<hr style="border:2px solid gray"> </hr>   
   
## Loops and Iterations - Part 1


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   
   
## Loops and Iterations - Part 2


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   
   
## Loops and Iterations - Part 3


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   
   
## Loops and Iterations - Part 4


```python
# START YOUR CODE HERE.
```

<hr style="border:2px solid gray"> </hr>  

## Practice Task   
#### 1. Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>"while True" yields an infinite loop.</li>
        <li>One can exit a loop by using the break operator.</li>
        <li>A valid number can be converted to an int.</li>
    </ul>
</p>
</details>


```python
# START YOUR CODE HERE.

```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>largest = None</code><br />
    <code>smallest = None</code><br />
    <code>while True:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;try:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;num = input("Enter a number: ")</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;num = int(num)</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;except:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if num == "done": break</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print("Invalid input, please enter a number.")</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;if largest is None or num > largest:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;largest = num</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;if smallest is None or num < smallest:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;smallest = num</code><br />
    <code>print("Maximum is", largest)</code><br />
    <code>print("Minimum is", smallest)</code>
</p>
</details> 
