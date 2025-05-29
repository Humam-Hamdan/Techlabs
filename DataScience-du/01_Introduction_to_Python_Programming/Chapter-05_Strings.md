# Chapter 5 - Strings
## Hey Techie,   
Welcome to the fifth notebook of this Python tutorial series. We encourage you to take this notebook as a template to code along the instruction videos, which you may find at: https://www.py4e.com/lessons/strings. Today's two videos deal with variables and how to store and manipulate text data using variables and functions in Python. There is no need to watch the worked exercise. In the end, please try to solve the presented task. If you want to double-check your results, you may also upload them to PY4E. For that, a Google Account is required. On the website, you find the auto-graded code tasks at the very end of each lesson.

## Have fun! :-)   
*Video length in total*: 30 minutes   
*Self-study time*: 30 minutes   
*Total*: **60 minutes**   
## Credits
Python for Everybody, Dr. Chuck Severance, https://www.py4e.com/, CC.

# Notes

- Strings are, as expected, arrays of chars.

- as with any array, you need the `[]` to get the value at the `n`-th place.

- `len(string)=int` the length.

- the less code you write, the more likely you are to be right.

- you can 'slice' a string, with `string_name[start_index:end_index+1]` this will return the chunk which starts from start index and ends obviously with end index.

- when the slice is bigger than the string there will be no trace back, just the string from the start to the end.

- when one of the indexes is not there it will be assumed that we are meaning the first/last index of the string.

- you can directly ask if a char is in a string and use it as an if condition ` 'n' in string `.

- there are a couple of 'objects methods' for strings, like '.lower()' and '.upper()' for upper and lower case.

- `dir(variable_of_type)` gives you the methods for each type.

- the `str.find('str')` gives back the position of the start index of the 'str' in the str.

- `str.replace('o', 'x')` this is a search and replace function, which replaces each 'o' with an 'x'.

- to strip white spaces we use `str.lstrip()` or `str.rstrip()` if we need to strip to the right or the left, but if we want both then a simple `str.strip()` will do.

- it even strips tabs and newlines.

- `str.startwith('stri')` it is a logical operation, depends on the case of 'stri'.

- you can concatenate with the '+' in between strings. This, will, however, not include a space unless manually added.

- `str.find('s')` gives the index of the s, if you want to find the first ss after that you use `str.find('ss', x)` where `x` is the index of said 's'.

