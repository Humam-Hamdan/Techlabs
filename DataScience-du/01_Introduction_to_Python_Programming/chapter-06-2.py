
# 2. Open the file data/mbox-short.txt and read it line by line. When you find a line that starts with "From " like the following line:
# ```From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008```
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end. Hint: make sure not to include the lines that start with "From:".
# The startswith-method checks whether a string starts with the specified characters and returns True or  False.
# What is the continue operator good for?
# List indexing starts at 0 and goes up to n-1 if n represents the number of elements.

hfile = open(
    '/home/humam/github/Techlabs/DataScience-du/01_Introduction_to_Python_Programming/data/mbox-short.txt', 'r')

file = hfile.readlines()
counter = 0
for line in file:
    if line.startswith('From '):
        x = line.split()
        print(x[1])
        counter += 1
print(counter)
