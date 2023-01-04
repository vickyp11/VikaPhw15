"""
1. Count
Вивести список кортежів, в якого перший елемент кортежа починається з 0.
Вхідні списки: ["A", "B", "C"], ['a', 'b', 'c']

"""
import itertools
import random

m = list(zip(itertools.count(start=0), ["A", "B", "C"], ['a', 'b', 'c']))
print('Count', m)

"""
2. Chain
Об“єднати кілька списків ["A", "B", "C"], ['a', 'b', 'c']
"""
print('Chain')
for i in itertools.chain(["A", "B", "C"], ['a', 'b', 'c']):
    print(i, end=' ')

"""
Згенеруйте два списки, довжиною 20 символів,
перший приймає значення від 1 до 10
другий – 0, та 1
З допомогою даної функції виведіть результуючий список (перший список, елементи якого по індексах співпадають з 1 в другому списку).
"""
print('\nCompress:')
n =list(itertools.compress(
    [random.randint(1, 10) for i in range(20)],
    [random.randint(0, 1) for i in range(20)]))
print(n)

"""
4. Takewhile
Даний список a_list = [(1, "B"), (2, "C"), (3, "A"), (4, "D"), (4, "D")]
Сформуйте результуючий список , що відповідає умові x[0] < 3
"""
print('Takewhile:')
a_list = [(1, "B"), (2, "C"), (3, "A"), (4, "D"), (4, "D")]
print(list(itertools.takewhile(lambda x:x[0] < 3, a_list)))

"""
5. StarMap
Даний список a_list = [[1,2,3], [4,5,6,7,8,89,7,6,4,3,1,3,2], [0]]
Поверніть список максимальних значень вкладених списків.
"""
print('StarMap')
a_list = [[1,2,3], [4,5,6,7,8,89,7,6,4,3,1,3,2], [0]]

def cond(*args):
    return max(args)

print(list(itertools.starmap(cond, a_list)))

"""
6. Product
Сформуйте варіанти з:
'AB', "ab", 'ef'
"""

print('Product\n', list(itertools.product('AB', "ab", 'ef')))

"""
7. combinations
Сформуйте комбінації по 3 символи з набору „ABCDE“
"""

print('Combinations\n', list(itertools.combinations('ABCDE', 3)))

"""
8. permutations
Сформуйте комбінації по 3 символи з набору „ABCDE“
"""

print('Permutations\n', list(itertools.permutations('ABCCDE', 3)))

