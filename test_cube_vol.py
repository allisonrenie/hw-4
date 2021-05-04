import unittest
import cube_vol

class test_class(unittest.TestCase):
    #tests if the squaring funciton properly squares a number
    def test_if_squares(self):
        self.assertEqual(cube_vol.cube_volume(3), 27)              #small num
        self.assertEqual(cube_vol.cube_volume(90), 729000)         #bigger num

    #tests if get_side returns an integer
    def test_side_is_int(self):
        self.assertTrue(isinstance(cube_vol.get_side(), int))

    #tests if get_side returns a positive number
    def test_reject_neg(self):
        self.assertTrue(cube_vol.get_side() > 0)

 # python -m unittest test_cube_vol.py
