"""
Make a class called Person. Make the __init__() method take firstname, lastname,
and age as parameters and add them as attributes. Make another method called talk() which makes prints a greeting from the person containing, f
or example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.
"""

class Person:
    def __init__(self, firstname, lastname, age):
        self.firtsname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print('Hello! I am', self.firtsname, self.lastname, 'and I am', self.age, 'years old')

myself = Person('Vika', 'Panina', 25)

myself.talk()
