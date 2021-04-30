import requests

url = 'https://api.openbrewerydb.org/breweries'
proxy = {"http": "localhost:8080", "https": "localhost:8080"}


def test_get_breweries():
    response = requests.get(url, proxies=proxy, verify=False)
    assert response.status_code == 200


def test_assert_id():
    response = requests.get(url, proxies=proxy, verify=False, params={'by_city': 'san_diego'})
    response_body = response.json()
    assert response_body[0]["id"] == 8041


def test_assert_city():
    response = requests.get(url, proxies=proxy, verify=False, params={'by_postal': '44107'})
    response_body = response.json()
    assert response_body[0]['city'] == 'Lakewood'
