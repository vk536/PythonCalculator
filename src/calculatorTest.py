import unittest
from calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_addition_calculator(self):
        test_data = CsvReader("src/CsvTestFiles/Unit Test Addition.csv").data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtraction_calculator(self):
        test_data = CsvReader("src/CsvTestFiles/Unit Test Subtraction.csv").data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.calculator.sub(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiply_method_calculator(self):
        test_data = CsvReader("src/CsvTestFiles/Unit Test Multiplication.csv").data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)


if __name__ == '__main__':
    unittest.main()
