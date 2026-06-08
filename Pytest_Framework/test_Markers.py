import pytest
@pytest.mark.regression
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
    
#skip--> skips the test
@pytest.mark.skipif(reason="simple")
@pytest.mark.regression
def test_add():
    assert 1+1==2

@pytest.mark.regression
@pytest.mark.xpass
def test_five():
    print("Five")