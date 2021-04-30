import requests

proxy = {"http": "localhost:8080", "https": "localhost:8080"}
header = {"Content-Type": "application/json"}
url = 'https://dog.ceo/api/breeds/list/all'


def test_is_ok():
    response = requests.get(url, headers=header, proxies=proxy, verify=False)
    assert response.ok


def test_encode():
    response = requests.get(url)
    assert response.encoding == 'utf-8'


def test_app_json():
    response = requests.get(url, proxies=proxy, verify=False)
    assert response.headers['Content-Type'] == 'application/json'


def test_body_contains():
    response = requests.get(url)
    response_body = response.json()
    assert response_body['message']['bulldog'][0] == 'boston'


def test_message_len():
    response = requests.get(url)
    response_body = response.json()
    assert len(response_body['message']) == 95
