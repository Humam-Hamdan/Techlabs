```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/01_Introduction\ to\ Python\ Programming
```

# Chapter 9 - Sets
### Hey Techie,   
Welcome to the ninth notebook of this Python tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://www.youtube.com/watch?v=r3R3h5ly_8g&list=PLkdX4MYXSiDvC_kSQuS3Smpl7KiRW1EpQ. Today's videos deal with sets that are like lists with non-repeating elements. In the end, please try to solve the presented task. As this lecture is not part of PY4E, you can only double-check your results using the provided test cases.

#### Have fun! :-)   
*Video length in total*: 20 minutes   
*Self-study time*: 20 minutes   
*Total*: **40 minutes**   

<hr style="border:2px solid gray"> </hr>   
   
## Sets - Set Methods and Operations to Solve Common Problems


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>  

## Practice Task   
#### 1. Write a program to read through the data/mbox-short.txt and figure out a non-repeating collection of emails. You can pull the emails from lines that start with "From ". 
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>First, store each email you can find in the file</li>
        <li>Second, remove the repeating ones from your data structure.</li>
    </ul>
</p>
</details>


```python
# START YOUR CODE HERE

# THIS ELEMENT SHOULD CONTAIN THE NON-REPEATING EMAIL COLLECTION. 
emails = ...
print(emails)
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert "gopal.ramasammycook@gmail.com" in emails, "You did not filter out all emails!"
assert "wagnermr@iupui.edu" in emails, "You did not filter out all emails!"
assert len(emails) == 11, "Your collection is not non-repeating!"
```

<details>
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>emails = []</code><br />
    <code>with open("data/mbox-short.txt", "r") as file:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;file = file.readlines()</code><br />
    <code>for line in file:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;if not line.startswith("From "):</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;emails.append(line.split()[1])</code><br />
    <code>emails = set(emails)</code><br />
    <code>print(emails)</code><br />
</p>
</details> 
