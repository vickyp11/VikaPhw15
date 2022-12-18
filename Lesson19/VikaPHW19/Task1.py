"""
Create your own implementation of a built-in function enumerate, named `with_index`, which takes two parameters: `iterable` and `start`, default is 0.
Tips: see the documentation for the enumerate function
"""
my_list = ['a', 'b', 'c']
# This is to check how built-in enumerate function works:
# for ind, val in enumerate(my_list, 3):
#     print(ind, val)

#This is my fucntion for enumerate:
# def with_index(iterable, start=0):
#     for i in iterable:
#         print(start, i)
#         start += 1
#
# with_index(my_list)
# with_index(my_list, 3)


#Task 2
"""
Create your own implementation of a built-in function range, named in_range(), which takes three parameters: `start`, `end`, and optional step. 
Tips: See the documentation for `range` function
"""
#This for checking if my function is working correctly:
# print(list(range(2,8,2)))

#This my fuction:
# def in_range(start, end, step=1):
#     new_list = []
#     i = 0
#     while start < end:
#         new_list.append(start)
#         start += step
#     return new_list
#
# print(in_range(2,8,2))


#Task 3
"""
Create your own implementation of an iterable, which could be used inside for-in loop. 
Also, add logic for retrieving elements using square brackets syntax.
"""



class MyIter:
    def __init__(self, iter_elem):
        self.iter_elem = iter_elem

    def my_iter(self):
        for i in self.iter_elem:
            return i

    def __getitem__(self, item):
        return self.iter_elem[item]


list_3 = MyIter(['vika', 'oleg', 'daisy'])
print(MyIter.my_iter(list_3))
print(MyIter.__getitem__(list_3,2))


