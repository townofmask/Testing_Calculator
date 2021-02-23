import unittest
from Calculator import Calculator
from Calculator import str_check
from Calc import calculatim

# python test_unit.py -v

class TestUnits(unittest.TestCase):
    def test_str_check_bad(self):
        str = ['((', '()', '-', 'abc', '1+a', '1+1a', ' ']
        for i in str:
            print(i, '   OK!!!')
            self.assertEqual(str_check(i), None)
    
    def test_calc(self):
        arr1 = '1.0*4'
        arr2 = '1.0+4.0'
        arr3 = '13.0 - 3.0 + 3.0'
        arr4 = '15 /  15.0 * 1.0'
        arr5 = '15.0 - 7.0 - 2.0'
        self.assertEqual(Calculator().calculate(arr1), 4.0)
        self.assertEqual(Calculator().calculate(arr2), 5.0)
        self.assertEqual(Calculator().calculate(arr3), 13.0)
        self.assertEqual(Calculator().calculate(arr4), 1.0)
        self.assertEqual(Calculator().calculate(arr5), 6.0)
    
    def test_brackets(self):
        arr1 = '(42/2)*9'
        arr2 = '(42-2)+(4-3)'
        arr3 = '(42-2)+9+(4-3)'
        arr4 = '(6+3)-(4+5)'
        self.assertEqual(Calculator().calculate(arr1), 189.0)
        self.assertEqual(Calculator().calculate(arr2), 41.0)
        self.assertEqual(Calculator().calculate(arr3), 50.0)
        self.assertEqual(Calculator().calculate(arr4), 0)

if __name__ == '__main__':
    unittest.main()
