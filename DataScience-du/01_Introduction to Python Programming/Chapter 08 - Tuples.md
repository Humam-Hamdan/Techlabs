```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/01_Introduction\ to\ Python\ Programming
```

# Chapter 8 - Tuples
### Hey Techie,   
Welcome to the eigth notebook of this Python tutorial series. We encourage you to take this notebook as a template to code along the instruction videos, which you may find at: https://www.py4e.com/lessons/tuples. Today's two videos deal with tuples that are very similar to lists but more efficient. There is no need to watch the video *Sorting a Dictionary Using Tuples*. In the end, please try to solve the presented task. If you want to double-check your results, you may also upload them to PY4E. For that, a Google Account is required. On the website, you find the auto-graded code tasks at the very end of each lesson.

#### Have fun! :-)   
*Video length in total*: 23 minutes   
*Self-study time*: 23 minutes   
*Total*: **46 minutes**   
#### Credits
Python for Everybody, Dr. Chuck Severance, https://www.py4e.com/, CC.
<hr style="border:2px solid gray"> </hr>   
   
## Tuples - Part 1


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   
   
## Tuples - Part 2


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>  

## Practice Task   
#### 1. Write a program to read through the data/mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
```From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008```
#### Once you have accumulated the counts for each hour, print out the counts, sorted by hour in the following format: Hour: Count.
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>Can you reuse code you have already written?</li>
        <li>Remind yourself of list indexing.</li>
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
    <code>hour_counts = {}</code><br />
    <code>with open("data/mbox-short.txt", "r") as file:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;file = file.readlines()</code><br />
    <code>for line in file:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;if not line.startswith("From "):</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;time = line.split()[5][:2]</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;hour_counts[time] = hour_counts.get(time, 0) + 1</code><br />
    <code>for key, value in sorted(list(hour_counts.items())):</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;print(key, value)</code><br />
</p>
</details> 
