import requests
import pytest

HOST = "http://127.0.0.1:5000/"


def test_run_parse_site_valid():
    args = {"site_url": 'https://khashtamov.com/ru/'}
    response = requests.post(HOST + "run_parse_site", data=args)

    assert response.ok
    assert response.json().get('notify', None) is not None


@pytest.mark.parametrize('url', [
    "httdps://www.goodfon.ru/",
    "https://123123/"
])
def test_run_parse_site_invalid(url):
    args = {"site_url": url}
    response = requests.post(HOST + "run_parse_site", data=args)

    assert response.ok
    assert response.json().get('error', None) is not None


def test_run_parse_site_not_allowed_get():
    response = requests.get(HOST + "run_parse_site")
    assert not response.ok


if __name__ == '__main__':
    args = {"site_url": 'https://khashtamov.com/ru/'}
    response = requests.post(HOST + "run_parse_site", data=args)

    print(response.json())
