"""
Write a program to read through the data/mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
Can you reuse code you have already written?
Remind yourself of the get-method to access values in dictionaries.
What does the items-method return if it is called on a dictionary?
"""


hfile = open(
    '/home/humam/github/Techlabs/DataScience-du/01_Introduction_to_Python_Programming/data/mbox-short.txt', 'r')

file = hfile.readlines()

dict = {}

for line in file:
    if line.startswith('From '):
        x = line.split()
        dict[x[1]] = dict.get(x[1], 0) + 1

maxnum = -1
maxwrd = None
for key, value in dict.items():
    if value > maxnum:
        maxnum = value
        maxwrd = key

print(maxwrd, maxnum)
