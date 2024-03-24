import pytest

from src.api_class import ApiHhVacancy


@pytest.fixture()
def api_test1():
    return ApiHhVacancy("повар")


@pytest.fixture()
def api_test2():
    ap = ApiHhVacancy("повар")
    ap.url_get = "https://api.hh.ru/bed"
    return ap

def test_check_status_request(api_test1, api_test2):
    assert ApiHhVacancy.check_status_request(api_test1) is True
    assert ApiHhVacancy.check_status_request(api_test2) is False