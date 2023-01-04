#Task 1
"""
Щоб спростити завдання та не дотримуватися всіх вимог до адреси електронної пошти, визначених у відповідних RFC специфікаціях, ми визначимо такі вимоги до рядка адреси електронної пошти:
- загальні: формат адреси електронної пошти – local-part@domain, де локальна частина може мати довжину до 64 символів, а домен – максимум 255 символів;
- локальна частина: символи ASCII – латинські літери від A до Z і від a до z ; цифри від 0 до 9 ;
- друковані символи ! # $% (амперсанд) '* + - / =? ^ _ `{|} ~ ; крапка . , за умови, що це не перший і не останній символ, а також за умови, що він не з'являється послідовно; пробіли та спеціальні символи "(),:; (математичний знак менше ніж)> @ [\] "(),:; (математичний знак менше ніж)> @ [\] не допускаються;
- частина домену: символи ASCII: латинські літери від A до Z і від a до z ; цифри від 0 до 9 ; дефіс – за умови, що це не перший і не останній символ.
Атрибут email має мати початкове значення None
"
"""

# allowed_symbols = ['!', '#', '$', '%','+', '-', '/', '=', '?', '^', '_', '{', '|', '}', '~', '.', ',']
# restricted_symbols = ['(', ')', ':', ';', '<', '>', '@', '[', ']', '"', ' ']
# domain_symbols = ['-']
#
# class Email:
#     def __init__(self):
#        inp_email = None
#
#     def __str__(self):
#         return self.inp_email
#
#     @property
#     def email(self):
#         return self.inp_email
#
#     @email.setter
#     def email(self, new_email):
#         self.inp_email = self._validate(new_email)
#
#     def _validate(self, new_email):
#         local = new_email.split('@')[0]
#         domain = new_email.split('@')[1]
#
#         if len(local) < 64 and local.isascii() or local.isdigit():
#             for i, v in enumerate(local):
#                 if v in allowed_symbols:
#                     if i == 0 or i == len(local)-1:
#                         raise ValueError('Special symbol cannot be the first/last!')
#                     if local[i+1] in allowed_symbols:
#                         raise ValueError('Special symbols cannot follow one each other!')
#                 if v in restricted_symbols:
#                     raise ValueError('Invalid symbol used')
#
#         if len(domain) < 225 and domain.isascii() or domain.isdigit():
#             for ind, val in enumerate(domain):
#                 if val in domain_symbols:
#                     if ind == 0 or ind == len(domain)-1:
#                         raise ValueError('Hyphen cannot be used at the first and last place within the domain!')
#
#             return new_email
#
#         else:
#             print('Invalid email')
#
#
# email_instance = Email()
# email_instance.email = "f9o633@email.com"
# print(email_instance.inp_email)

#Task 2
"""
Реалізуйте 2 класи: Boss і Worker. Worker має властивість boss і його значення має бути екземпляром класу Boss.
Ви можете переприсвоїти це значення, але слід перевіряти, чи є нове значення Boss.
Кожен Boss має список працівників. Потрібно реалізувати метод, який дозволить додавати працівників до Boss.
Не можна додавати екземпляри класу Boss до списку працівників безпосередньо через доступ до атрибутів. Замість цього, використовуйте геттери і сеттери.
Можна змінювати наявний код.
id_ – це просто випадкове унікальне ціле число.
Якщо переданий в сетер об'єкт не є об'єктом потрібного класу, потрібно викликати ValueError
"""
#
# class Boss:
#     def __init__(self, id_: int, name: str, company: str):
#         self.id = id_
#         self.name = name
#         self.company = company
#         self.workers = []
#
#     @property
#     def add_worker(self):
#         return self.workers
#
#     @add_worker.setter
#     def add_worker(self, worker):
#         if worker.boss == self:
#             self.workers.append(worker)
#         else:
#             raise ValueError('Different Boss!')
#         return self.workers
#
#     @add_worker.deleter
#     def add_worker(self, worker_name):
#         self.workers.remove(worker_name)
#
#     def __str__(self):
#         return f"{self.name}"
#
#     def __repr__(self):
#         return self.workers
#
#
# class Worker:
#     def __init__(self, id_: int, name: str, company: str, boss: Boss):
#         self.id = id_
#         self.name = name
#         self.company = company
#         self.boss = boss
#
#
#     def __str__(self):
#         return f"ID - {self.id}. Worker - {self.name}. Company - {self.company}. Boss - {self.boss} "
#
#     def __repr__(self):
#         return f"ID - {self.id}. Worker - {self.name}. Company - {self.company}. Boss - {self.boss} "
#
#
# boss1 = Boss(4567, 'Kateryna', 'Wix')
# worker1 = Worker(12345, 'Vika', 'Wix', boss1)
# boss2 = Boss(7908, 'Nadiya', 'Wix')
# worker2 = Worker(78923, 'Yuliia', 'Wix', boss2)
# worker3 = Worker(1234532, 'Max', 'Wix', boss1)
#
# boss1.add_worker = worker1
# print(boss1.workers)
# # boss2.add_worker = worker1
# # print(boss2.workers)
# boss1.add_worker = worker3
# print(boss1.workers)


#Task 3
"""
Напишіть клас TypeDecorators, який має різні методи конвертації результатів функцій у зазначений тип, якщо це неможливо – викликати відповідний виняток.
Методи:
to_int
to_str
to_bool
to_float
Не забувайте використовувати @wraps
—
class TypeDecorators:
 pass
@TypeDecorators.to_int
def do_nothing(string: str):
 return string
@TypeDecorators.to_bool
def do_something(string: str):
 return string
assert do_nothing('25') == 25
"""
from functools import wraps


class TypeDecorators:

    def to_int(self):
        @wraps(self)
        def wrapper(self):
            if type(self) == int:
                return self
            if type(self) == float:
                return round(self)
            if type(self) == str:
                if str(self).isdigit():
                    return int(self)
            if type(self) == bool:
                return int(self)
            else:
                raise ValueError('this cannot be converted to integer')
        return wrapper

    def to_str(self):
        @wraps(self)
        def wrapper(self):
            try:
                return str(self)
            except:
                raise ValueError('This value cannot be converted to string')
        return wrapper

    def to_bool(self):
        @wraps(self)
        def wrapper(self):
            try:
                return bool(self)
            except:
                raise ValueError('This value cannot be converted to boolean')
        return wrapper

    def to_float(self):
        @wraps(self)
        def wrapper(self):
            try:
                return float(self)
            except:
                raise ValueError('This value cannot be converted to float')
        return wrapper


@TypeDecorators.to_int
def test_int(inp):
    return inp

# print(test_int('True'))
# print(test_int('1234'))

@TypeDecorators.to_str
def test_str(string):
    return string

# print(test_str(1234))
# print(test_str(True))

@TypeDecorators.to_bool
def test_bool(boo):
    return boo

# print(test_bool(''))
# print(test_bool('1234'))

@TypeDecorators.to_float
def test_float(flo):
    return flo

# print(test_float('123'))
# print(test_float('sdfg'))











