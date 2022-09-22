from store_calculations import CalculationsStoreJSON

# tmp_path example
def test_correct_calculations_listed_from_json(tmp_path):
    store = CalculationsStoreJSON(tmp_path)
    calculation_with_multiplication = {"value_1": 2, "value_2": 4, "operation": "multiplication"}

    store.add(calculation_with_multiplication)

    assert store.list_operation_usages("multiplication") == [{"value_1": 2, "value_2": 4, "operation": "multiplication"}]