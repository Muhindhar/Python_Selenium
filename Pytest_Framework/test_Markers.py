import pytest

@pytest.mark.smoke
def test_one():
    print("Hi")

@pytest.mark.regression
def test_two():
    print("Two")

@pytest.mark.regression
def test_three():
    print("Three")

@pytest.mark.regression
@pytest.mark.xfail(reason="demo")
def test_four():
    print("Four")

@pytest.mark.skip(reason="simple")
@pytest.mark.regression
def test_add():
    assert 1+1 == 2

@pytest.mark.regression
def test_five():
    print("Five")