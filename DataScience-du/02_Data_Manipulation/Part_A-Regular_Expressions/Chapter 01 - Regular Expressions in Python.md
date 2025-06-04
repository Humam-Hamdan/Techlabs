
# Chapter 1 - Regular Expressions
## Hey Techie,   
Welcome to this lecture in which you will learn how to use and write regular expressions to filter text data efficiently. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://www.youtube.com/watch?v=K8L6KVGG-7o. Below you find every text-snippet which is used throughout the video. Also, the data.txt can be found in data/data.txt directory.   

## Cheat Sheet for Regexes: https://www.debuggex.com/cheatsheet/regex/python.

## Have fun! :-)   
*Video length in total*: 54 minutes   
*Self-study time*: 54 minutes   
*Total*: **108 minutes**   
## Credits
Python Tutorial: re Module - How to Write and Match Regular Expressions (Regex), Corey Schafer, https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g.
   

```python
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

with open("data/data.txt", "r", encoding="utf-8") as file:
    contents = file.read()
```


# Notes:

- you can make a regex for any text pattern thinkable -known from info1-.

- a raw string is a string with a starting r, which interprets the string literally, so no auto whitespacing and whatnot.

- we use `pattern = re.compile(r'abc')`  to set the pattern to be 'abc' in this order.

- then `matches = pattern.finditer(big_text_name)`.

- then you print the `matches` with a loop.

- what is printed then is a `span`, which gives the start and end index of the match.

- you can just then slice the string with the indexes and we're done!

- the previous search is case sensitive and order sensitive.

- if you want to get the matches of special chars then you need the backslash (to escape the regex).

- when we want an or operator we put the chars into `[]`.

- a `^` negates the matching in the char set.

- you can use `*, +, ?, {}, {min, max}` to search for a number of chars at once, i.e. `re.compile(r'\d{3}')` searches for 3 digits.

- the `()` are used to group the expression.

- you can get the group of the item, by `match.group(index)`.

- you can substitute, with `pattern.sub(r'\group_index\...', the_replaced_text)`.

- `pattern.findall` will return the matches only, with no extra data.

- `pattern.match` matches at the start of the string.

- `pattern.search` returns the first item which matches.

- in the `re.compile` if you do not care about lower/upper case shenanigans then just pass the `re.IGNORECASE`, or `re.I` flag.

