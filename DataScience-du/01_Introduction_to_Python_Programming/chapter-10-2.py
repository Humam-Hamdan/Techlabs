'''
Write a program to read through the data/mbox-short.txt and figure out emails as well as their line indexes. Lines that contain emails start with "From ". Store the pairs in a list of tuples named *pairs* that have the format (index, email). Sort this list with regard to the emails in alphabetical order.
First, store each email with their regarding index in a list as a tuple.
Second, sort this list with regard to the emails in alphabetical order.
'''

hfile = open(
    '/home/humam/github/Techlabs/DataScience-du/01_Introduction_to_Python_Programming/data/mbox-short.txt', 'r')

file = hfile.readlines()
pairs = list()
for index, element in enumerate(file):
    if element.startswith('From '):
        x = element.split()
        pairs.append((index, x[1]))


def name(pair): return pair[1]


pairs.sort(key=name)
print(pairs)
