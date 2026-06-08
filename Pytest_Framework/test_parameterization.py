import pytest
@pytest.mark.smoke
@pytest.mark.parametrize("test_input,exp",[(1,3),(3,6),(5,7)])
def test_addnum(test_input,exp):
    assert test_input+2 == exp