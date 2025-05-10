```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/01_Introduction\ to\ Python\ Programming
```

# Chapter 5 - Strings
### Hey Techie,   
Welcome to the fifth notebook of this Python tutorial series. We encourage you to take this notebook as a template to code along the instruction videos, which you may find at: https://www.py4e.com/lessons/strings. Today's two videos deal with variables and how to store and manipulate text data using variables and functions in Python. There is no need to watch the worked exercise. In the end, please try to solve the presented task. If you want to double-check your results, you may also upload them to PY4E. For that, a Google Account is required. On the website, you find the auto-graded code tasks at the very end of each lesson.

#### Have fun! :-)   
*Video length in total*: 30 minutes   
*Self-study time*: 30 minutes   
*Total*: **60 minutes**   
#### Credits
Python for Everybody, Dr. Chuck Severance, https://www.py4e.com/, CC.
<hr style="border:2px solid gray"> </hr>   
   
## Strings - Part 1


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   
   
## Strings - Part 2


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>  

## Practice Task   
#### 1. Write code using find() and string slicing to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>The find method returns the index of the character you have been searching for.</li>
        <li>String slicing starts at zero and ends at n-1 if n refers to the number of characters.</li>
        <li>String slicing is applied from including up to excluding.</li>
    </ul>
</p>
</details>


```python
text = "X-DSPAM-Confidence:    0.8475"
# START YOUR CODE HERE.

```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>text = "X-DSPAM-Confidence:    0.8475"</code><br />
    <code>pos = text.find("0")</code><br />
    <code>num = float(text[pos:])</code><br />
    <code>print(num)</code><br />
</p>
</details> 
