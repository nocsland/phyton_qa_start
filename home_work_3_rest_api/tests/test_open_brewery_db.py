import pytest
import requests

url = 'https://api.openbrewerydb.org/breweries'
proxy = {"http": "localhost:8080", "https": "localhost:8080"}


def test_get_breweries():
    response = requests.get(url, proxies=proxy, verify=False)
    assert response.status_code == 200


def test_city_to_id():
    response = requests.get(url, proxies=proxy, verify=False, params={'by_city': 'san_diego'})
    response_body = response.json()
    assert response_body[0]["id"] == 8041


def test_postal_to_city():
    response = requests.get(url, proxies=proxy, verify=False, params={'by_postal': '44107'})
    response_body = response.json()
    assert response_body[0]['city'] == 'Lakewood'


@pytest.mark.parametrize('data_in, expected', [(5, 5), (2, 2), (10, 10)])
def test_len_page(data_in, expected):
    response = requests.get(url, proxies=proxy, verify=False, params={'per_page': data_in})
    response_body = response.json()
    assert len(response_body) == expected


@pytest.mark.parametrize('data_in, expected',
                         [('san_diego', 'San Diego'), ('boulder', 'Boulder'), ('clermont', 'Clermont')])
def test_city_to_city_name(data_in, expected):
    response = requests.get(url, proxies=proxy, verify=False, params={'by_city': data_in})
    response_body = response.json()
    assert response_body[0]['city'] == expected
