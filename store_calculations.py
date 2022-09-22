import json


class CalculationsStoreJSON:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        with open(self.json_file_path / "calculations.json", "w") as file:
            json.dump([], file)

    def add(self, calculation):
        with open(self.json_file_path/"calculations.json", "r+") as file:
            calculations = json.load(file)
            calculations.append(calculation)
            file.seek(0)
            json.dump(calculations, file)

    def list_operation_usages(self, operation):
        with open(self.json_file_path / "calculations.json", "r") as file:
            calculations = json.load(file)

        return [calculation for calculation in calculations if calculation['operation'] == operation]
