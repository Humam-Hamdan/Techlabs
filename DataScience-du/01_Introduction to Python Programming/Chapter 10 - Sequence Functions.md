```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/01_Introduction\ to\ Python\ Programming
```

# Chapter 10 - Sequence Functions
### Hey Techie,   
Welcome to the tenth notebook of this Python tutorial series. We encourage you to take this notebook as a template to code along the instruction videos, which you may find at: https://www.youtube.com/watch?v=-MZiQaNI0QA&list=PLkdX4MYXSiDssQypMzg9goukgtVzq97nN.  Today's three videos deal with different methods that are useful for working with sequences (lists, tuples, sets, etc.). As this lecture is not part of PY4E, you can only double-check your results using the provided test cases.

#### Have fun! :-)   
*Video length in total*: 13 minutes   
*Self-study time*: 13 minutes   
*Total*: **26 minutes**   
<hr style="border:2px solid gray"> </hr>   

## Python Enumerate Function - Python Quick Tips


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   
   
## Sorting in Python || Learn Python Programming (Computer Science)


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   
   
## Zip Function - Python Quick Tips


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   

## Practice Task   
#### 1. Write a program to read through the data/mbox-short.txt and figure out the line indexes (starting at zero) that contain emails. Every line that contains an email starts with "From ". Store the indexes in a list called *indexes*.
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>Which of the discussed methods can you use?</li>
        <li>Instead of storing the emails, store their line indexes.</li>
    </ul>
</p>
</details>


```python
indexes = []
# START YOUR CODE HERE.

```


```python
# THIS CELL TESTS YOUR RESULTS.
assert len(indexes) == 27, "It seems as you did filter out not every line index!"
assert indexes[2] == 130, "You filtered out a wrong line!"
assert indexes[-1] == 1837, "Your filtered out a wrong line!"
```

<details>
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>indexes = []</code><br />
    <code>with open("data/mbox-short.txt", "r") as file:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;file = file.readlines()</code><br />
    <code>for index, line in enumerate(file):</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;if not line.startswith("From "):</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;indexes.append(index)</code>
</p>
</details>   
   
#### 2. Write a program to read through the data/mbox-short.txt and figure out emails as well as their line indexes. Lines that contain emails start with "From ". Store the pairs in a list of tuples named *pairs* that have the format (index, email). Sort this list with regard to the emails in alphabetical order.
<br /> 
<details>
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>First, store each email with their regarding index in a list as a tuple.</li>
        <li>Second, sort this list with regard to the emails in alphabetical order.</li>
    </ul>
</p>
</details>


```python
pairs = []
# START YOUR CODE HERE.

```


```python
# THIS CELL TESTS YOUR RESULTS.
assert len(pairs) == 27, "It seems as you did not filter out every pair!"
assert pairs[2][0] == 493, "You filtered out a wrong pair!"
assert pairs[-1][0] == 904, "Your filtered out a wrong pair!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>pairs = []</code><br />
    <code>with open("data/mbox-short.txt", "r") as file:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;file = file.readlines()</code><br />
    <code>for index, line in enumerate(file):</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;if not line.startswith("From "):</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;pairs.append((index, line.split()[1]))</code><br />
    <code>pairs = sorted(pairs, key = lambda x: x[1])</code><br />
</p>
</details>   
