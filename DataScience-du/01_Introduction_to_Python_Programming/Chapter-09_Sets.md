
# Chapter 9 - Sets
## Hey Techie,   
Welcome to the ninth notebook of this Python tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://www.youtube.com/watch?v=r3R3h5ly_8g&list=PLkdX4MYXSiDvC_kSQuS3Smpl7KiRW1EpQ. Today's videos deal with sets that are like lists with non-repeating elements. In the end, please try to solve the presented task. As this lecture is not part of PY4E, you can only double-check your results using the provided test cases.

## Have fun! :-)   
*Video length in total*: 20 minutes   
*Self-study time*: 20 minutes   
*Total*: **40 minutes**   


# Notes

- sets `s1 = set([items])`, `s1 = {items}`.

- it is a list but without duplicate values.

- you can use the usual set operations?

- for an empty set `s = set()`.

- add an item `set.add(item)`.

- add items `set.update([items])`.

- you can use `.update(set2)` with a set.

- you can do both, `.update([items], set2)`.

- to remove `set.remove(item)`.

- if you remove a value that does not exist will throwback, if you do not want that then use `set.discard(item)`.

- for the intersection `set.intersection(set2, set3, ...)`.

- for the difference `set.difference(set2, ...)`.

- for the union `set.union(set2, ...)`.

- symmetric difference, returns bot direction of difference `set.symmertic_difference(set2, ...)`.

- they are really useful for removing repeating items from a list.

- you can just cast the list into a set and into a list to return a list without duplicates.

- you can throw a list into intersection.

- they are efficient for checking if an item is in there or not.

- O(n) in a list, O(1) in a set.
