import requests


def test_url_status(method, url, code):
    response = requests.request(method, url)
    assert response.status_code == code
