from calculations import calculate_difference, calculate_dividend


def test_calculate_difference():

    calculation = calculate_difference(5, 3)

    assert calculation == 2


def test_calculate_dividend():

    calculation = calculate_dividend(12, 3)

    assert calculation == 4