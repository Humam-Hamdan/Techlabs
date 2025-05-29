
"""
Write a program to read through the data/mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
```From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008```
Once you have accumulated the counts for each hour, print out the counts, sorted by hour in the following format: Hour: Count.
Can you reuse code you have already written?
Remind yourself of list indexing.
Remind yourself of the get-method to access values in dictionaries.
What does the items-method return if it is called on a dictionary?
"""

hfile = open(
    '/home/humam/github/Techlabs/DataScience-du/01_Introduction_to_Python_Programming/data/mbox-short.txt', 'r')

file = hfile.readlines()

dict = {}
list = []
for line in file:
    if line.startswith('From '):
        x = line.split()
        list.append(x[5])
        for time in list:
            y = time.split(':')
            print(y[0])
            dict[y[0]] = dict.get(y[0], 0) + 1
            print(dict)

templist = []
for k, v in dict.items():
    templist.append((v, k))
templist = sorted(templist)

for v, k in templist:
    print('Hour:', k, 'Count:', v)


"""
hour_counts = {}

# Open and read the file line by line
with open("data/mbox-short.txt", "r") as file:
    for line in file:
        # Skip lines that don't start with "From "
        if not line.startswith("From "):
            continue

        # Extract the hour from the timestamp (6th element in the line)
        time = line.split()[5]
        hour = time[:2]

        # Count the occurrences of each hour
        hour_counts[hour] = hour_counts.get(hour, 0) + 1

# Print the counts sorted by hour
for hour, count in sorted(hour_counts.items()):
    print(hour, count)

"""
