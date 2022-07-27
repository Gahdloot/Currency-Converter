import unittest
from Level_1 import converter

class test_currency(unittest.TestCase):
    def test_convert(self):
        test_value = converter(710, 500, 1)
        test_value2 = 355000
        self.assertEqual(test_value, test_value2)



if __name__ == '__main__':
    unittest.main()