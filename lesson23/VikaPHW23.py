# #task 1
# from typing import Optional, Union
#
#
# def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
#     """
#     Returns  x ^ exp
#
#     to_power(2, 3) == 8
#     True
#
#     to_power(3.5, 2) == 12.25
#     True
#
#     to_power(2, -1)
#     ValueError: This function works only with exp > 0.
#     """
#     if exp == 0:
#         return 1
#     if exp == 1:
#         return x
#     if exp < 0:
#         raise ValueError('This function works only with exp > 0')
#     return x*to_power(x, exp-1)
#
# print(to_power(2, 3))
# print(to_power(3.5, 2) == 12.25)
# print(to_power(2, -1))

#task 2

from typing import Optional
# def is_palindrome(looking_str: str, index: int = 0) -> bool:
#
#     """
#     Checks if input string is Palindrome
#     is_palindrome('mom')
#     True
#
#      is_palindrome('sassas')
#     True
#
#     is_palindrome('o')
#     True
#     """
#
#     if len(looking_str) <= 1:
#         return True
#     elif looking_str[index] != looking_str[-1]:
#         return False
#     else:
#         return is_palindrome(looking_str[1:-1])
#
#
# print(is_palindrome('o'))
# print(is_palindrome('sassas'))
# print(is_palindrome('mom'))
# print(is_palindrome('l2mm5l'))


#task 3
from typing import Optional
# def mult(a: int, n: int) -> int:
#     """
#     This function works only with positive integers
#
#     mult(2, 4) == 8
#     True
#
#     mult(2, 0) == 0
#     True
#
#     mult(2, -4)
#     ValueError("This function works only with postive integers")
#     """
#
#     if a < 0 or n < 0:
#         raise ValueError ('This function works only with postive integers')
#     if n == 0 or a == 0:
#         return 0
#     return a+mult(a, n-1)
#
# print(mult(2, 4))
# print(mult(2, 0) == 0)
# print(mult(2, -4))


#task 4
#
# def reverse(input_str: str) -> str:
#     """
#     Function returns reversed input string
#     reverse("hello") == "olleh"
#     True
#     reverse("o") == "o"
#     True
#     """
#
#     if input_str == '':
#         return input_str
#     return reverse(input_str[1:]) + input_str[0]
#
#
# print(reverse('hello'))
# print(reverse("o") == "o")

#task 5
def sum_of_digits(digit_string: str) -> int:
    """
    sum_of_digits('26') == 8
    True

    sum_of_digits('test')
    ValueError("input string must be digit string")
    """
    if len(digit_string) == 1:
        return int(digit_string)
    if digit_string.isdigit():
        return int(digit_string[0]) + int(sum_of_digits(digit_string[1:]))
    else:
        raise ValueError('input string must be digit string')


print(sum_of_digits('26'))
print(sum_of_digits('26199'))
print(sum_of_digits('test'))





