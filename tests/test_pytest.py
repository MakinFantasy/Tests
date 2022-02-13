import pytest
from main import multiplicate_int, multiplicate_string

params = [(1, 1, 1), (2, 2, 4), (-5, 1, -5), (-10, -1, 10)]

# OOP is not required, but recommended as always


class TestFunctions:
    def test_multiplication_int(self):
        assert multiplicate_int(2, 2) == 4

    def test_multiplication_string(self):
        assert multiplicate_string('a', 5) == 'aaaaa'

    @pytest.mark.parametrize("a, b, result", params)
    def test_multiplication_int2(self, a, b, result):
        assert multiplicate_int(a, b) == result

    @pytest.fixture
    def data(self):
        return 1, 1, 1

    def test(self, data):
        a, b, result = data
        assert multiplicate_int(a, b) == result
