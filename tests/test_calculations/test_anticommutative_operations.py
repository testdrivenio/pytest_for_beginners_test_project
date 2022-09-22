import pytest

from calculations import calculate_difference, calculate_dividend


# paremtrization example:
@pytest.mark.parametrize(
    "first_value, second_value, expected_output",
    [
        (10, 8, 2),
        (8, 10, -2),
        (-10, -8, -2),
        (-8, -10, 2),
    ]
)
def test_calculate_difference(first_value, second_value, expected_output):

    calculation = calculate_difference(first_value, second_value)

    assert calculation == expected_output


def test_calculate_dividend():

    calculation = calculate_dividend(12, 3)

    assert calculation == 4