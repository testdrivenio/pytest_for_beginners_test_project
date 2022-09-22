import requests

from number_facts import get_number_fact


class MockedResponse:

    def __init__(self, json_body):
        self.json_body = json_body

    def json(self):
        return self.json_body


def mock_get(*args, **kwargs):
    return MockedResponse({
        "text": "7 is the number of days in a week.",
        "number": 7,
        "found": "true",
        "type": "trivia"
    })


def test_get_joke(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_get)

    number = 7
    fact = '7 is the number of days in a week.'

    assert get_number_fact(number) == fact
