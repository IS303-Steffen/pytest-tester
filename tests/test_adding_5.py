from example_function import add_5


def test_add_five():
    assert add_5(3) == 8
    assert add_5(10) == 15
    assert add_5(-5) == 0
