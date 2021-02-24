def GreaterNumber(num1 : int, num2 : int):

    """compares two element return greatest element

    >>>print(GreaterNumber(9,2))
    9
    """

    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        return "Equal"

import doctest
doctest.testmod()

import unittest

class TestingGraterNumber(unittest.TestCase):

    def test_num1(self):
        self.assertEquals(GreaterNumber(9,2), 9)
    
    def test_num2(self):
        self.assertEquals(GreaterNumber(2,9), 9)

    def test_Equal(self):
        self.assertEquals(GreaterNumber(5,5), 'Equal')

if __name__ == '__main__':
    unittest.main()