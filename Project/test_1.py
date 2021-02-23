import pytest
from Calculator import Calculator
from Calculator import str_check
from Calc import calculatim

#(с input) pytest -s test_1.py
# pytest -v test_1.py

def test_calculating1():
    result = 7
    assert calculatim(znak= '+', a=3.0, b=4.0) == result

def test_calculating2():
    result = 40
    assert calculatim(znak= '-', a=45.0, b=5.0) == result

def test_calculating3():
    result = 120
    assert calculatim(znak= '*', a=30.0, b=4.0) == result

def test_calculating4():
    result = 12
    assert calculatim(znak= '/', a=300.0, b=25.0) == result

def test_calculating_br():
    user_input = '(258.0+25)'
    res = 283.0
    assert Calculator().calculate(user_input) == res

def test_calculating_br1():
    user_input = '(100.0-95)'
    res = 5.0
    assert Calculator().calculate(user_input) == res

def test_calculating_br2():
    user_input = '(100.0*25)'
    res = 2500.0
    assert Calculator().calculate(user_input) == res

def test_calculating_br3():
    user_input = '(258/129)'
    res = 2.0
    assert Calculator().calculate(user_input) == res

def test_calculating_more():
    user_input = '1+10+23-1'
    res = 33.0
    assert Calculator().calculate(user_input) == res

def test_calculating_more2():
    user_input = '12*6/4'
    res = 18.0
    assert Calculator().calculate(user_input) == res

def test_calculating_more3():
    user_input = '(42/2)*9'
    res = 189.0
    assert Calculator().calculate(user_input) == res

def test_calculating_more4():
    user_input = '42-2-9'
    res = 31.0
    assert Calculator().calculate(user_input) == res

def test_calculating_more5():
    user_input = '(42-2)+9+(4-3)'
    res = 50.0
    assert Calculator().calculate(user_input) == res

def test_calculating_more5():
    user_input = '((42-2)+(4-3))'
    res = 41.0
    assert Calculator().calculate(user_input) == res

def test_calcucating_minus():
    user_input = '6-(3+1)'
    res = 2.0
    assert Calculator().calculate(user_input) == res

def test_calcucating_minus1():
    user_input = '(6*2)-(3+1)'
    res = 8.0
    assert Calculator().calculate(user_input) == res

def test_calcucating_minus2():
    user_input = '((6*2)-(3+1))-3'
    res = 5.0
    assert Calculator().calculate(user_input) == res

def test_calcucating_minus3():
    user_input = '(6+3)-1'
    res = 8.0
    assert Calculator().calculate(user_input) == res

def test_str_parse():
    user_input = '-1'
    res = None
    assert str_check(user_input) == res

def test_str_parse2():
    user_input = 'lkj'
    res = None
    assert str_check(user_input) == res

def test_str_parse3():
    user_input = '1.1.1.1'
    res = None
    assert str_check(user_input) == res

def test_str_parse4():
    user_input = '123456'
    res = None
    assert str_check(user_input) == res

def test_str_parse5():
    user_input = '/*-+'
    res = None
    assert str_check(user_input) == res

def test_error():
    user_input = '42/2*9'
    res = 189.0
    assert Calculator().calculate(user_input) == res, '42/2*9, error priority'

def test_error2():
    user_input = '42/2+9'
    res = 16.0
    assert Calculator().calculate(user_input) == res, '42/2+9, error priority'

def test_error3():
    user_input = '((6-(3+1))+(1*1))'
    res = 3.0
    assert Calculator().calculate(user_input) == res, '((6-(3+1))+(1*1)), error ne dodelano'
