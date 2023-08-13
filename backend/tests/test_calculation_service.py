import unittest

from services.calculation_service import CalculationService


class CalculationServiceTest(unittest.TestCase):

    def setUp(self) -> None:
        self.service = CalculationService()

    def test_calculate(self):
        # 1 + 2
        args = [1, 2]
        ops = ['+']
        self.assertEqual(self.service.calculate(args, ops), 3)

        # 1 + 2 - 3
        args = [1, 2, 3]
        ops = ['+', '-']
        self.assertEqual(self.service.calculate(args, ops), 0)

        # 1 + 2 + 2 * 2
        args = [1, 2, 2, 2]
        ops = ['+', '+', '*']
        self.assertEqual(self.service.calculate(args, ops), 7)

        # 1 + 2 + 2 * 2 / 4
        args = [1, 2, 2, 2, 4]
        ops = ['+', '+', '*', '/']
        self.assertEqual(self.service.calculate(args, ops), 4)


if __name__ == '__main__':
    unittest.main()
