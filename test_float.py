import pytest


@pytest.mark.parametrize("test_input,expected", [
    ("1.0 and 1.0", 1.0),
    ("1.0 or 1.0", 1.0),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


def test_float():
    assert float(1) == 1.0
    assert float(-1) == -1.0
    assert 1.0 + 2.1 == 3.1
    assert 1.0 + (-2.1) == -1.1
    assert 1.0 - 0.5 == 0.5
    assert 1.0 - 1.5 == -0.5
    assert 1.0 - (-1.5) == 2.5
    assert 1.0 * 2.0 == 2.0
    assert 1.0 * (-2.0) == -2.0
    assert 1.0 / 2.0 == 0.5
    assert 1.0 / (-2.0) == -0.5
    assert 1.0 + 1 == 2.0
    assert 1.0 - 1 == 0.0
    assert 1.0 * 1 == 1.0
    assert 1.0 / 1 == 1.0
