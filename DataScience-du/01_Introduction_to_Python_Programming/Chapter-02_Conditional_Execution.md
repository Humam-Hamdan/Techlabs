# Chapter 2 - Conditional Execution
## Hey Techie,   
Welcome to the second notebook of this Python tutorial series. We encourage you to take this notebook as a template to code along the instruction videos, which you may find at: https://www.py4e.com/lessons/logic. Today's two videos deal with how Python executes some statements and skips others. There is no need to watch the worked exercises. In the end, please try to solve the presented tasks. If you want to double-check your results, you may also upload them to PY4E. For that, a Google Account is required. On the website, you find the auto-graded code tasks at the very end of each lesson.

## Have fun! :-)   
*Video length in total*: 30 minutes   
*Self-study time*: 30 minutes   
*Total*: **60 minutes**   
## Credits
Python for Everybody, Dr. Chuck Severance, https://www.py4e.com/, CC.

# Notes

- an if block looks like this:

```python
x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finish')
```

- logical operators:

    - < less than

    - <= leq

    - == equals

    - \>= geq

    - \> greater

    - != neq

    - > note, = i used for assignment

- tbh after getting used to \{\} in C python's indentation seems stupid for a programming language.

- You can nest ifs to the sky and back.

- for the if then else we use

```python
if condition :
    does this when true
else :
    does this when false
```

- you can have multi way with elifs

```python
if condition1 :
    command
elif condition2 :
    command
else :
    command
```

- python in the execution goes line by line.

- if there is no else then when the condition is not fulfilled the block will be skipped.

- we use try/catch when we deal with dangerous sections/conditions.

```python
astr = 'Hi'
try:
    ister = int(astr)
except:
    ister = -1

print('First', ister)

astr2 = '123'
try:
    ister2 = int(astr2)
except:
    istr = -1
print('Second', ister)
```

- So when try files the except runs and the program goes on.

- If there are more than one line in try, and one in the mid blows up, the rest are never tried.

- Here is a real sample

```python
rawstr = input('Enter a Number: ')
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0:
    print('Good Job')
else:
    print('NaN')
```


