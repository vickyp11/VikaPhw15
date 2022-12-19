"""
Implement a class Mathematician which is a helper class for doing math operations on lists

The class doesn't take any attributes and only has methods:

square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
"""

class Mathematician:
    def square_nums(self):
        return [i**2 for i in self]

    def remove_positives(self):
        new_list = []
        for n in self:
            if n < 0:
                new_list.append(n)
        return new_list

    def filter_leaps(self):
        new_list1 = []
        for m in self:
            if m % 4 != 0:
                new_list1.append(m)
        return new_list1


list1 = [4, 2, 3]
list2 = [-25, -66, 22]
list3 = [2000, 2023, 2020]
print(Mathematician.square_nums(list1))
print(Mathematician.remove_positives(list2))
print(Mathematician.filter_leaps(list3))

