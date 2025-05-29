

# 1. Open the file data/romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
# Open the file using "with open(path, "r") as file".
# The readlines-method returns a list containing the different lines as elements.
# One line can be split into a list of words using the split-method.
# Remind yourself of the not in operator.

# MY SOLUTION

romhand = open(
    '/home/humam/github/Techlabs/DataScience-du/01_Introduction_to_Python_Programming/data/romeo.txt', 'r')

lines = romhand.readlines()
words = list()
# No need to strip
for j in lines:
    words.append(j.split())

singles = list()
for k in words:
    singles = singles + k

final = list()
for l in singles:
    if l not in final:
        final.append(l)
final.sort()
print(final)

# MODEL SOLUTION

# words = []
# with open("data/romeo.txt", "r") as file:
#     file = file.readlines()
# for line in file:
#     text = line.split()
#     for word in text:
#         if word not in words:
#             words.append(word)
# print(sorted(words))
