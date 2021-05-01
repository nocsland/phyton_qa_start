import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--url',
        default='https://ya.ru',
        help='This is request url'
    )

    parser.addoption(
        '--method',
        default='get',
        choices=['get', 'post', 'put', 'patch', 'delete'],
        help='method to execute'
    )

    parser.addoption(
        '--code',
        default=200,
        choices=[200, 404, 500, 300],
        help='response code'
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture
def default_method(request):
    return getattr(request, request.config.getoption('--method'))


@pytest.fixture
def default_code(request):
    return request.config.getoption('--code')


def test_url_status(base_url, default_code, default_method):
    target = base_url + f'/status/{default_code}'
    response = default_method(url=target)
    assert response.status_code == default_code
