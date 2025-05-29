'''
Write a program to read through the data/mbox-short.txt and figure out a non-repeating collection of emails. You can pull the emails from lines that start with "From ". 
First, store each email you can find in the file
Second, remove the repeating ones from your data structure.
'''

hfile = open(
    '/home/humam/github/Techlabs/DataScience-du/01_Introduction_to_Python_Programming/data/mbox-short.txt', 'r')

file = hfile.readlines()
set = set()
for line in file:
    if line.startswith('From '):
        x = line.split()
        set.add(x[1])
print(set)
