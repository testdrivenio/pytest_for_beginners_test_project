from calculations import calculate_sum, calculate_product


def test_calculate_sum():

    calculation = calculate_sum(5, 3)

    assert calculation == 8


def test_calculate_product():

    calculation = calculate_product(5, 3)

    assert calculation == 15