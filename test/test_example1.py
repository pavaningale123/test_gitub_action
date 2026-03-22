from src.mat_operation import add, subtract

def test_add():
    assert add(1, 2) == 3
    assert add(-1) == 0
    assert add(0, 0) == 0
    assert add(2.5, 3.5) == 6.0 

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0) == -1
    assert subtract(10, 5) == 5
    assert subtract(3.5, 1.5) == 2.0