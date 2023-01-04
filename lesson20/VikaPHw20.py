# Task 1
"""
Pick your solution to one of the exercises in this module. Design tests for this solution and write tests using unittest library.
"""
from math import gcd

class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __add__(self, other):
        if not isinstance(other.num, int) or not isinstance(other.den, int) or not isinstance(self.num, int) or not isinstance(self.den, int):
            raise TypeError('Are you sure it is number?')
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


#Task 2


class Person:
    def __init__(self, name, birth_year, address, phone_number):
        self.name = name
        self.birth_year = birth_year
        self.address = address
        self.phonr_number = phone_number


class Student(Person):
    def __init__(self, name, birth_year, address, phone_number, year_of_uni, degree, acad_performance, graduate_year, class_number):
        super().__init__(name, birth_year, address, phone_number)
        self.year_of_uni = year_of_uni
        self.degree = degree
        self.acad_performance = acad_performance
        self.graduate_year = graduate_year
        self.class_number = class_number

    def grad_age(self):
        graduate_age = self.graduate_year - self.birth_year
        return f'Graduate year: {graduate_age}'

    def credits(self):
        numb_credits = self.class_number * self.year_of_uni
        return f"Current credits: {numb_credits}"

    def performance(self):
        return f"Current performance is: {self.acad_performance} out of 100"


class Teacher(Person):
    def __init__(self, name, birth_year, address, phone_number, experience, lessons, price_per_lesson):
        super().__init__(name, birth_year, address, phone_number)
        self.experience = experience
        self.lessons = lessons
        self.price_per_lesson = price_per_lesson

    def salary(self):
        teacher_salary = self.price_per_lesson * self.lessons
        return f"Salary is: {teacher_salary} UAH"



