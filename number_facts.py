import requests


def get_number_fact(number):
    url = f"http://numbersapi.com/{number}?json"
    response = requests.get(url)
    json_resp = response.json()

    if json_resp["found"]:
        return json_resp["text"]

    return "No fact about this number."
