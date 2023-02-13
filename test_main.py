import pytest
from main import main

@pytest.mark.parametrize(
    "values, less, lower, upper, greater, expected",
    [
       ([3, 9, 3, 4, 6], 4, 3, 6, 4, (2, 4, 2)),
       ([7, 7, 3, 4, 2, 3, 4], 3, 1, 5, 6, (1, 5, 2)),
       ([11, 12], 15, 5, 8, 10, (2, 0, 2)),
       ([1, 5, 9, 13], 6, 5, 8, 13, (2, 1, 0)),
       ([1, 152, 3, 1, 952, 2], 1000, 2, 100, 1, (6, 2, 4)),
       ([3, 9, 3, 4, 6], 3, 3, 6, 4, (0, 4, 2)),
       ([1, 5, 9, 13], 1, 5, 9, 13, (0, 2, 0)),
    ]
)
def test_main(values: list, less: int, lower: int, upper: int, greater: int, expected: tuple):
    assert main(values, less, lower, upper, greater) == expected