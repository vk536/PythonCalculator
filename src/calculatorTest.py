import unittest
from calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

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

    def test_multiplication_calculator(self):
        test_data = CsvReader("src/CsvTestFiles/Unit Test Multiplication.csv").data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_division_calculator(self):
        test_data = CsvReader("src/CsvTestFiles/Unit Test Division.csv").data
        for row in test_data:
            result = round(float(row['Result']), 7)
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square_calculator(self):
        test_data = CsvReader("src/CsvTestFiles/Unit Test Square.csv").data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.calculator.squares(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_sqrt_method_calculator(self):
        test_data = CsvReader("src/CsvTestFiles/Unit Test Square Root.csv").data
        for row in test_data:
            result = round(float(row['Result']), 7)
            self.assertEqual(self.calculator.square_root(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)


if __name__ == '__main__':
    unittest.main()
