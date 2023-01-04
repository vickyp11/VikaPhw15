class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()

    @property
    def full_name(self):
        return self.first_name, self.last_name

    @full_name.setter
    def full_name(self, name):
        first = name.split(' ')[0]
        last = name.split (' ')[1]
        self.first_name = first
        self.last_name = last

    def change_name(self, name, surname):
        self.first_name = name
        self.last_name = surname
        return self.first_name.title() + ' ' + self.last_name.title()

    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.last_name = None
        print('Deleted!')

vika = Person('vika', 'panina')
print(vika.full_name)
print(vika.change_name('oleg', 'panin'))
print(vika.full_name)
vika.full_name = 'Daisy Panina'
print(vika.full_name)
del vika.full_name
print(vika.full_name)

