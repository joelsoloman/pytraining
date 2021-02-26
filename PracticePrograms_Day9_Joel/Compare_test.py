import pytest
from Compare import comp

@pytest.mark.parametrize(
    "element1,element2,expected",
    [
        (9,2,9),
        (2,9,9),
        (1,1,0),
    ]
)

def test_num1_greater(element1, element2, expected):
    assert comp(element1, element2) == expected

@pytest.mark.skip()
def test_num1_fail():
    assert comp(2,9) == 9

@pytest.mark.skipif(True, reason = "Skipping in Condition")
def test_num2_fail():
    assert comp(9,2) == 9

@pytest.mark.xfail
def test_failing_condition():
    assert comp(-5,-10) == -10