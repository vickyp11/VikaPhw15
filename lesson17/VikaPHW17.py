#Task 1
"""
Create a base class named Animal with a method called talk and then create two subclasses:
Dog and Cat, and make their own implementation of the method talk be different. For instance,
Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.

Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs talk method on input parameter.
"""
# def animal_talks(animal):
#     print(animal.talk())
#
#
# class Animal:
#     def talk(self):
#         pass
# class Dog(Animal):
#     def talk(self):
#         return 'Woof Woof'
#
# class Cat(Animal):
#     def talk(self):
#         return 'Meow Meow'
#
#
# dog = Dog()
# cat = Cat()
#
# animal_talks(cat)
# animal_talks(dog)
#
# #Task 2
#
# class Library:
#
#     def __init__(self, name, books=[], authors=[]):
#         self.name = name
#         self.books = books
#         self.authors = authors
#
#     def __repr__(self):
#         return f"This is {self.name} library"
#
#     def __str__(self):
#         return f"This is {self.name} library"
#
#     def new_book(self, name, year, author):
#         book = Book(name, year, author)
#         self.books.append(book)
#         return book
#
#     def group_by_author(self, author):
#         return [book for book in self.books if book.author == author]
#
#     def group_by_year(self, year: int):
#         return [book for book in self.books if book.year == year]
#
#
# class Book:
#     number_of_books = 0
#
#     def __init__(self, name, year, author):
#         self.name = name
#         self.year = year
#         self.author = author
#
#         Book.number_of_books += 1
#
#     def __repr__(self):
#         return f"Name = {self.name} year = {self.year} author = {self.author}"
#
#     def __str__(self):
#         return f"Name = {self.name} year = {self.year} author = {self.author}"
#
#
# class Author:
#
#     def __init__(self, name, country, birthday, books=[]):
#         self.name = name
#         self.country = country
#         self.birthday = birthday
#         self.books = books
#
#     def __repr__(self):
#         return f" {self.name} country = {self.country}, date of birth = {self.birthday}"
#
#     def __str__(self):
#         return f" {self.name} country = {self.country}, date of birth = {self.birthday}"
#
#
# l1 = Library("Central Library")
# a1 = Author("J.K.Rowling", "The United Kingdom", "31 July 1965")
# a2 = Author("Serhij Žadan", "Ukraine", "25 December 1978")
# a3 = Author("Taras Ševčenko", "Ukraine", "9 March 1814")
# a4 = Author("Terry Pratchett", "The United Kingdom", "1950")
# a5 = Author("Stanislaw Lem", "Poland", "1915")
# l1.new_book("Harry Potter", 1997, a1)
# l1.new_book("Internat", 2017, a2)
# l1.new_book("Depesh Mode", 1997, a2)
# l1.new_book("Kobzar", 1840, a3)
# l1.new_book("Colour of Magic", 1997, a4)
# l1.new_book("Cyberiada", 1978, a5)
# l1.new_book("Solaris", 1976, a5)
# l1.new_book("Harry Potter2", 1999, a1)
# l1.new_book("Harry Potter3", 2001, a1)
# print(l1.group_by_author(a2))
# print(l1.group_by_year(1997))
#
# print(type(Book("NAme", 23, "Author")))

#Task 3
"""
Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) 
з належною перевіркою й обробкою помилок. 
Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction
"""

from math import gcd


class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('Are you sure it is number?')
        else:
            self.sum_num = self.num * other.den + other.num * self.den
            self.sum_den = self.den * other.den

            res_div = gcd(self.sum_num, self.sum_den)

            res_num = self.sum_num / res_div
            res_den = self.sum_den/res_div

            return Fraction(int(res_num), int(res_den))

    def __mul__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('Are you sure it is number?')
        else:
            self.mult_num = self.num * other.num
            self.mult_den = self.den * other.den

            res_div_mult = gcd(self.mult_num, self.mult_den)

            res_num_mult = self.mult_num / res_div_mult
            res_den_mult = self.mult_den / res_div_mult

            return Fraction(int(res_num_mult), int(res_den_mult))

    def __sub__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('Are you sure it is number?')
        else:
            self.sub_num = self.num * other.den - other.den * self.den
            self.sub_den = self.den * other.den

            res_sub_div = gcd(self.sub_num, self.sub_den)

            res_sub_num = self.sub_num / res_sub_div
            res_sub_den = self.sub_den / res_sub_div


            return Fraction(int(res_sub_num), int(res_sub_den))

    def __truediv__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('Are you sure it is number?')
        else:
            self.div_num = self.num * other.den
            self.div_den = self.den * other.num

            res_div_div = gcd(self.div_num, self.div_den)

            res_div_num = self.div_num / res_div_div
            res_div_den = self.div_den / res_div_div

            return Fraction(int(res_div_num), int(res_div_den))

    def __str__(self):
        return f"Fraction({self.num}, {self.den})"

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x+y)
    print(x*y)
    print(x-y)
    print(x/y)


