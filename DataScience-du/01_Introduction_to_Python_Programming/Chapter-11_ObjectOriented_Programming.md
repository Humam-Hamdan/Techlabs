
# Chapter 11 - Object-oriented Programming
## Hey Techie,   
Welcome to the final notebook of this Python tutorial series. We encourage you to take this notebook as a template to code along the instruction videos, which you may find at: https://www.py4e.com/lessons/Objects. Today's four videos deal with concept of object-oriented programming. In the end, please try to solve the presented task. As PY4E does not offer an auto-graded assigment for this lecture, you can only double-check your results using the provided test cases.

## Have fun! :-)   
*Video length in total*: 30 minutes   
*Self-study time*: 30 minutes   
*Total*: **60 minutes**   
## Credits
Python for Everybody, Dr. Chuck Severance, https://www.py4e.com/, CC.

# Notes

- An Object is self contained code and data that you use in the Program.

- You use them because your problem is complex and you split it up into a couple of more doable ones.

- You take the input and then transfer it between objects and then throw it out.

- Objects make you ignore -abstract- over the use/process that is done in/with that object.

- Definitions:

    - Class: a template, that defines the specification of the object -a cookie cutter-.

    - Object: an instance of the Class.

    - Method: a function that lives inside the Class.

    - Fields: data items in the Class.

- Example:

```python
class PartyAnimal:
    def __init(self)__:
        self.x = 0
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)
an = PartyAnimal()

an.party()
an.party()
an.party()
```

- note that `an.party()` is the same as `PartyAnimal.party(an)`.

- using `type()` returns the type of the item, and `dir()` returns the methods.

- we usually use constructors, as destructors are called by python automatically.

- Example Code:

```python
class PartyAnimal:
    def __init__(self):
        self.x = 0
        print("Constructed")
    def party(self):
        self.x += 1
        print("So far", self.x)
    def __del__(self):
        print("Desstoryed", self.x)
an = PartyAnimal()
an.party()
an.party()
an = 42
print("an contains", an)
```

- Example for multiple instances of objects:

```python
class PartyAnimal:
    def __init__(self, z):
        self.x = 0
        self.name = z
        print(self.name, "Constructed")
    def party(self):
        self.x += 1
        print(self.name, "Party count", self.x)
s = PartyAnimal("Sally")
s.party()
j = PartyAnimal("Jay")
j.party()
s.party()
```

- You can extend a class by inheritance.

- OG Class = Class/Parent. Child/SubClass.

- Example:

```python
class PartyAnimal:
    def __init__(self, nam):
        self.x = 0
        self.name = nam
        print(self.name, "Constructed")
    def party(self):
        self.x += 1
        print(self.name, "Party count", self.x)
class FootballFan(PartyAnimal):
    def __init__(self, nam):
        super().__init__(nam)
        self.points = 0
    def touchdown(self):
        self.points += 7
        self.party()
        print(self.name, "points", self.points)
s = PartyAnimal("sally")
s.party()
j = FootballFan("jay")
j.party()
j.touchdown()
```


