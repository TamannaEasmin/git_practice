import pytest
from calculator import add, subtract


@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def zero_pair():
    return (0, 0)


def test_sum_with_fixture(numbers):
    assert sum(numbers) == 15


def test_add_with_zero(zero_pair):
    a, b = zero_pair
    assert add(a, b) == 0


def test_subtract_with_zero(zero_pair):
    a, b = zero_pair
    assert subtract(a, b) == 0
