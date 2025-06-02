
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

- 

