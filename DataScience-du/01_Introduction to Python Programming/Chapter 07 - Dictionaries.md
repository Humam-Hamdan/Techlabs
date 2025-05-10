```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/01_Introduction\ to\ Python\ Programming
```

# Chapter 7 - Dictionaries
### Hey Techie,   
Welcome to the seventh notebook of this Python tutorial series. We encourage you to take this notebook as a template to code along the instruction videos, which you may find at: https://www.py4e.com/lessons/dictionary. Today's three videos deal with dictionaries and how to use them to store key-value associations. There is no need to watch the video *Counting Word Frequency using a Dictionary*. In the end, please try to solve the presented task. If you want to double-check your results, you may also upload them to PY4E. For that, a Google Account is required. On the website, you find the auto-graded code tasks at the very end of each lesson.

#### Have fun! :-)   
*Video length in total*: 30 minutes   
*Self-study time*: 30 minutes   
*Total*: **60 minutes**   
#### Credits
Python for Everybody, Dr. Chuck Severance, https://www.py4e.com/, CC.
<hr style="border:2px solid gray"> </hr>   
   
## Dictionaries - Part 1


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   
   
## Dictionaries - Part 2


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   
   
## Dictionaries - Part 3


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>  

## Practice Task   
#### 1. Write a program to read through the data/mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>Can you reuse code you have already written?</li>
        <li>Remind yourself of the get-method to access values in dictionaries.</li>
        <li>What does the items-method return if it is called on a dictionary?</li>
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
    <code>email_counts = {}</code><br />
    <code>with open("data/mbox-short.txt", "r") as file:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;file = file.readlines()</code><br />
    <code>for line in file:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;if not line.startswith("From "):</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;adress = line.split()[1]</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;email_counts[adress] = email_counts.get(adress, 0) + 1</code><br />
    <code>biggest_key = None</code><br />
    <code>biggest_value = None</code><br />
    <code>for key, value in email_counts.items():</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;if biggest_value is None or value > biggest_value:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;biggest_key = key</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;biggest_value = value</code><br />
    <code>print(biggest_key, biggest_value)</code><br />
    <code></code><br />
    <code># SHORT FORM TO FILTER OUT THE MAXIMUM:</code><br />
    <code>biggest_key, biggest_value = sorted(email_counts.items(), key = lambda x: -x[1])[0]</code><br />
    <code>print(biggest_key, biggest_value)</code><br />
</p>
</details> 
