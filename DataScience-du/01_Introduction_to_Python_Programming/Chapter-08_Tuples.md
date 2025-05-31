
# Chapter 8 - Tuples
## Hey Techie,   
Welcome to the eigth notebook of this Python tutorial series. We encourage you to take this notebook as a template to code along the instruction videos, which you may find at: https://www.py4e.com/lessons/tuples. Today's two videos deal with tuples that are very similar to lists but more efficient. There is no need to watch the video *Sorting a Dictionary Using Tuples*. In the end, please try to solve the presented task. If you want to double-check your results, you may also upload them to PY4E. For that, a Google Account is required. On the website, you find the auto-graded code tasks at the very end of each lesson.

## Have fun! :-)   
*Video length in total*: 23 minutes   
*Self-study time*: 23 minutes   
*Total*: **46 minutes**   
## Credits
Python for Everybody, Dr. Chuck Severance, https://www.py4e.com/, CC.

# Notes

- you can take a dict, reverse key,value tuples and then sort over it.

- you can use `sorted(list, reverse=True)` to reverse an order, but then even the alphabet will be reversed.

- a tuple is like a list but with `tuple = ()` instead of `list = []`, however, a tuple is immutable.

- they are used since they are more efficient than lists.

- you can only use `.count() , .index()` for tuples.

- when we use tmp variables we just use tuples.

- we can put the tuple on the left side, like this `a,b = 99,88`.

- you can return a tuple from a function! -yay, no more void functions :)-.

- they are comparable like strings, so we only see till either or is fulfilled and we break immediately.

- if you need to sort a dict we usually take it to a list of tuples, sort there and return.

- a one line that does this is as follows `print( sorted( [ (v, k) for k, v in dict.items() ] ) )`.

