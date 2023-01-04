#tests for Task 1

import unittest
from VikaPHw20 import Fraction, Person, Student, Teacher

# class TestForFractions(unittest.TestCase):
#
#     def test_fractions(self):
#         a = Fraction(5, 6)
#         b = Fraction(8, 6)
#         self.assertEqual(a.num, 5)
#         self.assertEqual(b.den, 100)
#
#
# if __name__ == '__main__':
#     unittest.main()

#test for task 2
#since it's possible to test the task with Contact list with inputs, I have selected another task for testing

class TestForTaskTwo(unittest.TestCase):

    def test_for_teacher(self):
        test_teacher = Teacher('Vira Ivanove', 1990, 'Kyiv, Peremohy ave, 10', '3806477739980', 7, 30, 50)
        #self.assertEqual(test_teacher.experience, 7)
        #self.assertTrue(test_teacher.price_per_lesson == 70)
        #self.assertGreater(test_teacher.birth_year, 2000)
        self.assertFalse(type(test_teacher.phonr_number) == int)

if __name__ == '__main__':
     unittest.main()