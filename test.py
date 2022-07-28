import unittest
from Level_1 import converter
from Level_2 import currency

class test_currency(unittest.TestCase):

    def test_convert_level1(self):
        test_value = converter(710, 500, 1)
        test_value2 = 355000
        self.assertEqual(test_value, test_value2)

    def test_convert_level2(self):
        value_difference = currency('usd', 'ngn')

        self.assertEqual(value_difference.convert(), 417)



if __name__ == '__main__':
    unittest.main()