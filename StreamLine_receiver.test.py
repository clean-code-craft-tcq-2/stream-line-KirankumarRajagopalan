import unittest

from Sender import parameter

class rangeSorterTest(unittest.TestCase):

    def test_parameter_method_get_Value(self):
        testParameter = parameter("Test",-2,200)
        value = testParameter.get_value()
        self.assertTrue(value >= -2 and value <=200)

if __name__ == '__main__':
    unittest.main()
