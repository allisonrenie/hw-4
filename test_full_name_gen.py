import unittest
import full_name_gen

class test_class(unittest.TestCase):

    #tests that there is a first name (not empty string)
    def test_first_exist(self):
        test_name = full_name_gen.get_first()
        self.assertTrue(len(test_name) > 0)

    #tests that there is last name (not empty string)
    def test_last_exist(self):
        test_name_2 = full_name_gen.get_last()
        self.assertTrue(len(test_name_2) > 0)

    #tests that the end result full name is a string
    def test_full_name_is_str(self):
        self.assertTrue(isinstance(full_name_gen.get_full_name('Allison', 'Thompson'), str))

 # python -m unittest test_full_name_gen.py
