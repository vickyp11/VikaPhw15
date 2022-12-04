"""
Write a function called `choose_func` which takes a list of nums and 2 callback functions.
If all nums inside the list are positive, execute the first function on that list and return the result of it.
Otherwise, return the result of the second one
"""


def func1(nums):
    print ([num ** 2 for num in nums])

def func2(nums):
    print ([num for num in nums if num > 0])


def choose_func(nums: list, func1, func2):
    count = 0
    for i in nums:
        if i < 0:
            count += 1
    if count == 0:
        func1(nums)
    if count >= 1:
        func2(nums)




nums = [1, -2, 3, -4, 5]
# nums = [1, 2, 3, 4, 5]
choose_func(nums, func1, func2)






