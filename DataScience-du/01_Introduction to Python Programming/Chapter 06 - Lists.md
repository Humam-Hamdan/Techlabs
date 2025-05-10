```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/01_Introduction\ to\ Python\ Programming
```

# Chapter 6 - Lists
### Hey Techie,   
Welcome to the sixth notebook of this Python tutorial series. We encourage you to take this notebook as a template to code along the instruction videos, which you may find at: https://www.py4e.com/lessons/lists. Today's three videos deal with how Python simplest data structure works - the list. There is no need to watch the video *Lists, Files, and the Guardian Pattern*. In the end, please try to solve the presented tasks. To do so, you need to understand how to open text files (.txt) in Python. Therefore, please read the following article: https://www.pythontutorial.net/python-basics/python-read-text-file/. If you want to double-check your results, you may also upload them to PY4E. For that, a Google Account is required. On the website, you find the auto-graded code tasks at the very end of each lesson.

#### Have fun! :-)   
*Video length in total*: 30 minutes   
*Self-study time*: 50 minutes   
*Total*: **80 minutes**   
#### Credits
Python for Everybody, Dr. Chuck Severance, https://www.py4e.com/, CC.
<hr style="border:2px solid gray"> </hr>   
   
## Lists - Part 1


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   
   
## Lists - Part 2


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   
   
## Lists - Part 3


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>  

## Practice Tasks   
#### 1. Open the file data/romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>Open the file using "with open(path, "r") as file".</li>
        <li>The readlines-method returns a list containing the different lines as elements.</li>
        <li>One line can be split into a list of words using the split-method.</li>
        <li>Remind yourself of the not in operator.</li>
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
    <code>words = []</code><br />
    <code>with open("data/romeo.txt", "r") as file:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;file = file.readlines()</code><br />
    <code>for line in file:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;text = line.split()</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;for word in text:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if word not in words:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;words.append(word)</code><br />
    <code>print(sorted(words))</code>
</p>
</details>   
  
#### 2. Open the file data/mbox-short.txt and read it line by line. When you find a line that starts with "From " like the following line:
```From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008```
#### You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end. Hint: make sure not to include the lines that start with "From:".
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>The startswith-method checks whether a string starts with the specified characters and returns True or  False.</li> 
        <li>What is the continue operator good for?</li>
        <li>List indexing starts at 0 and goes up to n-1 if n represents the number of elements.</li>
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
    <code>count = 0</code><br />
    <code>with open("data/mbox-short.txt", "r") as file:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;file = file.readlines()</code><br />
    <code>for line in file:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;if not line.startswith("From "):</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;else:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count += 1</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(line.split()[1])</code><br />
    <code>print("There were", count, "lines in the file with From as the first word.")</code><br />
</p>
</details>   
