import requests
import pytest

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


@pytest.mark.parametrize('data_in, expected', [(0, 'boston'), (1, 'english'), (2, 'french')])
def test_body_contains(data_in, expected):
    response = requests.get(url)
    response_body = response.json()
    assert response_body['message']['bulldog'][data_in] == expected


@pytest.mark.parametrize('data_in, expected', [('australian', 1), ('bulldog', 3), ('hound', 7)])
def test_message_len(data_in, expected):
    response = requests.get(url)
    response_body = response.json()
    assert len(response_body['message'][data_in]) == expected
