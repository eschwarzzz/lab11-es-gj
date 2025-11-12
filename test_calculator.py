# https://github.com/eschwarzzz/lab11-es-gj.git
# Eric Schwarz & Guiliano Jules

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(-2, 1), -1)


    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(5, -3), 8)
        self.assertEqual(subtract(-5, 3), 2)
    ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 9), 27)
        self.assertEqual(mul(-1, -10), 10)
        self.assertEqual(mul(2, 2), 4)
        
    def test_divide(self): # 3 assertions
        self.assertEqual(div(3, -3), -1)
        self.assertAlmostEqual(div(3, 1.00000000001), 1/3)
        self.assertEqual(div(-3, 24), -8)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10, 10), 1)
        self.assertEqual(logarithm(100, 10), 2)
        self.assertEqual(logarithm(1000, 10), 3)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(10, 0)
            
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)
  

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, -4), 5)
        self.assertAlmostEqual(hypotenuse(1, 1), 1.4142135623)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-3)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(144), 12)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()