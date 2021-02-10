import pytest
from calc import Calc
@pytest.mark.parametrize("a, b, ans", [(5, 5, 10),(3, 5, 12),(55, 45, 100),(19, 11, 30)])
def test_valid(supply_calc, a, b, ans):
     assert supply_calc.add(a, b) == ans, "addition failed"


# @pytest.mark.parametrize("a, b, ans", [(1, 2, -1)])
# def test_minus(supply_calc, a, b, ans):
#     assert supply_calc.minus(a, b) == ans, "minus isbad"


# @pytest.mark.parametrize("a, b, ans", [(4, 3, 12), (4, 0, 0), (0, 0, 0)])
# def test_mult(supply_calc, a, b, ans):
#     assert supply_calc.mult(a, b) == ans, "multi is bad"


# @pytest.mark.parametrize("a, b, ans", [(120, 6, 20), (1, 0, 'zero division'), (0, 0, 'zero division' )])
# def test_divis(supply_calc, a, b, ans):
#     assert supply_calc.divis(a, b) == ans, "division is bad"

# @pytest.mark.parametrize("a, b, ans", [(2, 4, 16), (0, 900, 0), (98, 1, 98), (98, 0, 1), (0, 0, 1)])
# def test_sterp(supply_calc, a, b, ans):
#     assert supply_calc.step(a, b) == ans, "multi step is bad"
