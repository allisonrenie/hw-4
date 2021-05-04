import unittest
import avg_of_list

class test_class(unittest.TestCase):
    #tests if list has elements
    def test_does_list_have_elements(self):
        self.assertTrue(len(avg_of_list.random_list()) > 0)

    #tests that code can accuratly caluclate an average
    def test_if_calc_avg(self):
        self.assertEqual(avg_of_list.list_average([25, 125, 5, 10, 100]), 53)

    #test if the list items are actually integers
    def test_if_ints(self):
        test_list = avg_of_list.random_list()
        self.assertTrue(isinstance(test_list[0], int))

 # python -m unittest test_avg_of_list.py
