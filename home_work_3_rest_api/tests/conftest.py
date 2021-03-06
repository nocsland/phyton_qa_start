import pytest
import urllib3



def pytest_addoption(parser):
    parser.addoption(
        '--url',
        default='https://ya.ru',
        help='request url'
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
        choices=[200, 404],
        type=int,
        help='response code'
    )


@pytest.fixture
def url(request):
    urllib3.disable_warnings()
    return request.config.getoption('--url')


@pytest.fixture
def method(request):
    return request.config.getoption('--method')


@pytest.fixture
def code(request):
    return request.config.getoption('--code')
