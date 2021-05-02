import requests
import pytest

url = 'https://jsonplaceholder.typicode.com'
proxy = {"http": "localhost:8080", "https": "localhost:8080"}


def test_users_code_200():
    response = requests.get(f'{url}/users', proxies=proxy, verify=False)
    assert response.status_code == 200


def test_get_amount_posts_100():
    response = requests.get(f'{url}/posts', proxies=proxy, verify=False)
    response_body = response.json()
    assert len(response_body) == 100


def test_is_user_have_any_posts():
    response = requests.get(f'{url}/posts', proxies=proxy, verify=False, params={'userId': '9'})
    response_body = response.json()
    assert len(response_body) != 0


@pytest.mark.parametrize('data_in, expected', [(3, 'eum et est occaecati'), (4, 'nesciunt quas odio')])
def test_posts_title(data_in, expected):
    response = requests.get(f'{url}/posts', proxies=proxy, verify=False)
    response_body = response.json()
    assert response_body[data_in]['title'] == expected


@pytest.mark.parametrize('data_in, expected', [(0, 'hildegard.org'), (1, 'anastasia.net')])
def test_user_website(data_in, expected):
    response = requests.get(f'{url}/users', proxies=proxy, verify=False)
    response_body = response.json()
    assert response_body[data_in]['website'] == expected
