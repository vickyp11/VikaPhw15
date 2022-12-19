"""
Make a class structure in python representing people at school.
Make a base class called Person, a class called Student, and another one called Teacher.
Try to find as many methods and attributes as you can which belong to different classes, and keep in mind which are common and which are not.
For example, the name should be a Person attribute, while salary should only be available to the teacher.
"""

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


student1 = Student('Ivan Ivanov', 2000, 'Kyiv, Khreschatyk str', 380998883445, 3, 'Aeronavigation', 87, 2024, 6)
print(student1.grad_age())
print(student1.credits())
print(student1.performance())

teacher1 = Teacher('Maryna Hoffman', 1986, 'Kyiv, Shevchenka blvd', 3809923334, 4, 30, 600)
print(teacher1.salary())

