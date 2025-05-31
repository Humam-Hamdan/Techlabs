
# Chapter 1 - Variables, Expressions, and Statements
## Hey Techie,   
Welcome to the first notebook of this Python tutorial series. We encourage you to take this notebook as a template to code along the instruction videos, which you may find at: https://www.py4e.com/lessons/memory. Today's two videos deal with variables and how we can use them to store data. There is no need to watch the worked exercises. In the end, please try to solve the presented task. If you want to double-check your results, you may also upload them to PY4E. For that, a Google Account is required. On the website, you find the auto-graded code tasks at the very end of each lesson.

## Have fun! :-)   
*Video length in total*: 30 minutes   
*Self-study time*: 30 minutes   
*Total*: **60 minutes**   
## Credits
Python for Everybody, Dr. Chuck Severance, https://www.py4e.com/, CC.

# Notes

- String constants are in single or double quotes.

- Reserved words can not be used outside of the language's implementation.

- when you make a variable you are allocating a piece of memory to some data with a specific name.

- for 'x = 12' we tell python to take 12 and find a place for it in memory and mark the place with it. (a pointer really.)

- when you reuse the same var the value changes, hence, _variable_.

- usually we use smallcaps for var names.

- choose var names with good readability.

- Operators:

    - + add

    - - minus

    - * by

    - / over

    - ** to the power of

    - % mod

- Python knows what a string and what an integer is.

- we use the function `type()` to discern the type.

- As usual, int, float.

- casting is as usual, `int(...)` and `float(...)`.

- implicit casting between `int` and `float` happens like usual.

- / in python 3 just casts everything into floats, calculates it and when needed prints as an integer.

- tbh the C standard -which was used in python 2- is more predictable, that is, if you know C :).

- you can casts strings which are made of integers.

- you use `input()` to get user input, `print("",value)` to print a string with a value.

- a comment in python begins with a `#`.

- Example:

```python
# Change from EU to US floor convection.

eu_floor = int(input('Europe Floor?'))
us_floor = eu_floor + 1
print("US Floor", us_floor)
```


