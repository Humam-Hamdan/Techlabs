# Chapter 7 - Dictionaries
## Hey Techie,   
Welcome to the seventh notebook of this Python tutorial series. We encourage you to take this notebook as a template to code along the instruction videos, which you may find at: https://www.py4e.com/lessons/dictionary. Today's three videos deal with dictionaries and how to use them to store key-value associations. There is no need to watch the video *Counting Word Frequency using a Dictionary*. In the end, please try to solve the presented task. If you want to double-check your results, you may also upload them to PY4E. For that, a Google Account is required. On the website, you find the auto-graded code tasks at the very end of each lesson.

## Have fun! :-)   
*Video length in total*: 30 minutes   
*Self-study time*: 30 minutes   
*Total*: **60 minutes**   
## Credits
Python for Everybody, Dr. Chuck Severance, https://www.py4e.com/, CC.

# Notes

- a dictionary is a type of collection.

- a dict is a key-value pairing.

- you can search in a dict with a key.

- you need to pick a label and a value.

- `dict['key'] = value` is how to add a pair.

- to init a dict `dict = {}`.

- a dict is implemented with a hashmap.

- one of the usual uses is the Histogram.

- one common way to use dicts is counting the number of 'how many' is the element seen.

- in a dict you can not look for an element which does not exist, yet you can use the `in` operator.

- `dict.get(key, default)` if the key exists you get the value or you get the default.

- for a count we usually use `dict[key] = dict.get(key, 0) + 1`.

- to count words in a text we usually split the lines into words and go from there.

- a `list(dict.keys())` will give back a list with the keys.

- similarly a `list(dict.values())` returns a list with values.

- also, a `list(dict.items())` returns a list with the key-value tuple.

- then, you can iterate like this `for a,b in dict.items() : print(a,b)` (python only).

