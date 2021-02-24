from GreaterNumber import GreaterNumber as GreaterNum

def test_num1_greater():
    assert GreaterNum(9,2) == 9

def test_num2_greater():
    assert GreaterNum(2,9) == 9

def test_num1_num2_equal():
    assert GreaterNum(5,5) == 'Equal'