
# Chapter 10 - Sequence Functions
## Hey Techie,   
Welcome to the tenth notebook of this Python tutorial series. We encourage you to take this notebook as a template to code along the instruction videos, which you may find at: https://www.youtube.com/watch?v=-MZiQaNI0QA&list=PLkdX4MYXSiDssQypMzg9goukgtVzq97nN.  Today's three videos deal with different methods that are useful for working with sequences (lists, tuples, sets, etc.). As this lecture is not part of PY4E, you can only double-check your results using the provided test cases.

## Have fun! :-)   
*Video length in total*: 13 minutes   
*Self-study time*: 13 minutes   
*Total*: **26 minutes**   

# Python Enumerate Function - Python Quick Tips

- if you want to get the items with the indexes, then `for index, element in enumerate(list): print(index, element)` will spit out the index for each element.


# Sorting in Python || Learn Python Programming (Computer Science)

- if you have a list of tuples and want to sort it according to an element you do a `name = lambda item: item[index]` then a `list.sort(key=name)`.

- you can use `clist = sorted(list, key=, reverse=)` to make a sorted copy of a list.

- you can pass a tuple to `sorted()` function.

# Zip Function - Python Quick Tips

- the zip function is basically a cardinal product of sets, and true, it returns a list of tuples.

- the cardinality of the returned list is equal to the one of the smaller list.

- it will pair the element with the same index number only.

- you can do the same-check like this:

```python
x = [1, 2, 3, 4]
y = [1, 2, 3, 4, 5]

for i, j in zip(x, y):
    if i == j:
        print('Yay')
    else:
        print('Nay')
```

