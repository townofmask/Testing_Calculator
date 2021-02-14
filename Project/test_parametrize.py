import pytest
from Calc import Calculator

@pytest.mark.parametrize("inp1, inp2, output", [(5,5,10),(3,5,12)])
def test_add(inp1, inp2, output):
    assert inp1+inp2 == output, "failed"