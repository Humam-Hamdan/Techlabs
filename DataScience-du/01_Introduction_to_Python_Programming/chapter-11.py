'''
Write a class Techie that has four global attributes (part of self) name (str), age (int), profession (str), and location (str). Additionally, write four methods that print one of the global attributes respectively named *get_name*, *get_age*, *get_profession*, and *get_location*.
Use the built-in input method to read hours and rate per hour separately.
Typecast both inputs to floats.
Print the result by multiplying the hours with their rate per hour using the *-operator.
'''


class Techie:
    def __init__(self, name, age, profession, location):
        self.name = name
        self.age = age
        self.profession = profession
        self.location = location

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.age)

    def get_profession(self):
        print(self.profession)

    def get_location(self):
        print(self.location)


techie = Techie(name="YourName", age=99,
                profession="YourProfession", location="YourLocation")


techie.get_name()
techie.get_age()
techie.get_profession()
techie.get_location()
