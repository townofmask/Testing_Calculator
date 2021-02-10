import pytest
from calc import Calc
@pytest.fixture
def supply_calc():
    return Calc()