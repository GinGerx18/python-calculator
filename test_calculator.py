import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add1(self):
        self.assertEqual(self.calc.add(5, 2), 7)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(3, 1), 2)

    def test_sub1(self):
        self.assertEqual(self.calc.subtract(19, 20), -1)
    # Add the following test methods to the TestCalculator class:

    def test_mul(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_mul1(self):
        self.assertEqual(self.calc.multiply(10, 21), 210)

    def test_div(self):
        self.assertEqual(self.calc.divide(21, 0), "Error")

    def test_div1(self):
        self.assertEqual(self.calc.divide(72, 3), 24)

    def test_mod(self):
        self.assertEqual(self.calc.modulo(21, 3), 0)

    def test_mod2(self):
        self.assertEqual(self.calc.modulo(45, 4), 1)
if __name__ == '__main__':
    unittest.main()