
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
   
## Text-Snippets


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



# Task: For this example, we will work with the Data Science Wikipedia article. First, please inspect the text below.


```python
with open("data/practice.txt", "r") as file:
    wikipedia_article = file.read()
# INSPECT TEXT HERE.
# print(wikipedia_article)
```

Your task is to filter out every heading (i.e., Foundations, Relationship to statistics etc.) using a regular expression. To do so, please complement the below function, which should return a list of strings that contains the different headings as elements.
You can identify the headings by using the leading and ending '==.'
Design a regex-pattern with three groups, where groups one and three capture the '==' and group 2 captures the heading itself


```python
def answer():
    # START YOUR CODE HERE.
    
    return # RETURN YOUR ANSWER HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert type(answer()) == type([]), "Please return a list!"
assert type(answer()[0]) == type(str()), "The returned list should contain strings as elements!"
assert len(answer()) == 10, "Your results seem to be incomplete!"
assert "Foundations" in answer(), "Your results seem to be incomplete!"
assert "Modern usage" in answer(), "Your results seem to be incomplete!"
```

