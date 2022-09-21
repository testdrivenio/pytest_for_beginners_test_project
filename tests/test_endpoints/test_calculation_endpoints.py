from starlette.testclient import TestClient

from main import app


class TestCalculationEndpoints:
    def test_return_sum(self):
        test_data = {
            "first_val": 10,
            "second_val": 8
        }
        client = TestClient(app)

        response = client.post("/sum/", json=test_data)

        assert response.status_code == 200
        assert response.json() == 18

    def test_return_difference(self):
        test_data = {
            "first_val": 10,
            "second_val": 8
        }
        client = TestClient(app)

        response = client.post("/subtract/", json=test_data)

        assert response.status_code == 200
        assert response.json() == 2

    def test_return_product(self):
        test_data = {
            "first_val": 8,
            "second_val": 2
        }
        client = TestClient(app)

        response = client.post("/multiplication/", json=test_data)

        assert response.status_code == 200
        assert response.json() == 16

    def test_return_dividend(self):
        test_data = {
            "first_val": 8,
            "second_val": 2
        }
        client = TestClient(app)

        response = client.post("/division/", json=test_data)

        assert response.status_code == 200
        assert response.json() == 4
