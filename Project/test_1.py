import pytest
from Calc import Calculator
def test_method1():
    x=5
    y=6
    assert x+1 == y, "test failed"
    assert x == y, "test failed"
def test_method2():
    x=5
    y=6
    assert x+1 == y, "test failed"