'''
Write a program to read through the data/mbox-short.txt and figure out the line indexes (starting at zero) that contain emails. Every line that contains an email starts with "From ". Store the indexes in a list called *indexes*.
Which of the discussed methods can you use?
Instead of storing the emails, store their line indexes.
'''


hfile = open(
    '/home/humam/github/Techlabs/DataScience-du/01_Introduction_to_Python_Programming/data/mbox-short.txt', 'r')

file = hfile.readlines()
indexes = list()
for index, element in enumerate(file):
    if element.startswith('From '):
        # print(index, element)
        indexes.append(index)
print(indexes)
