import requests


def test_url_status(method, url, code):
    response = requests.request(method, url, verify=False)
    assert response.status_code == code
