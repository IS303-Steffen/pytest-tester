import pytest


def test_add_five(sample_number, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Example")
    from example_function import add_5
    assert add_5(3) == 8
    assert add_5(sample_number) == 15
    assert add_5(-5) == 0
