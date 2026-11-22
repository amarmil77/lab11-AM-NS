import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,2), 4)
        self.assertEqual(mul(-5, 2), -10)
        self.assertEqual(mul(1, 0), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(4,2),2)
        self.assertEqual(div(72, 9), 8)
        self.assertEqual(div(2, -2), -1)
    ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)


    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(20, 15), 25)
        self.assertAlmostEqual(hypotenuse(6, -4), 7)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        with self.assertRaises(ValueError):
           square_root(-1)
        # Test basic function
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(100), 10)
        self.assertAlmostEqual(square_root(1), 1)
        #fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()