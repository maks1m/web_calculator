import math
import unittest

from utils.calculator import Calculator, CalculatorExtended


class CalculatorTestCase(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.calculate('+', 1, 2), 3)

    def test_subtraction(self):
        self.assertEqual(self.calc.calculate('-', 4, 2), 2)

    def test_multiplication(self):
        self.assertEqual(self.calc.calculate('*', 2, 2), 4)

    def test_division(self):
        self.assertEqual(self.calc.calculate('/', 4, 2), 2)
        self.assertTrue(math.isnan(self.calc.calculate('/', 4, 0)))

    def test_non_supported_operation(self):
        with self.assertRaises(NotImplementedError):
            self.calc.calculate('^', 2, 2)

    def test_list_of_top_priority_operations(self):
        self.assertEqual(self.calc.top_priority_math_ops(), {'*', '/'})


class CalculatorExtendedTestCase(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.calc = CalculatorExtended()

    def test_power(self):
        self.assertEqual(self.calc.calculate('^', 2, 3), 8)

    def test_supported_operations(self):
        self.assertEqual(self.calc.supported_math_operations(), {'+', '-', "*", '/', '^'})

    def test_list_of_top_priority_operations(self):
        self.assertEqual(self.calc.top_priority_math_ops(), {'*', '/', '^'})


if __name__ == '__main__':
    unittest.main()
