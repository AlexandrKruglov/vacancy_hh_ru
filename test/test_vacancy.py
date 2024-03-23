import pytest

from src.api_class import ApiHhVacancy
from src.vacancy_class import Vacancy


@pytest.fixture()
def api_test1():
    return ApiHhVacancy("повар")


@pytest.fixture()
def api_test2():
    ap = ApiHhVacancy("повар")
    ap.url_get = "https://api.hh.ru/bed"
    return ap


@pytest.fixture()
def vacancy_test1():
    return Vacancy(123, "повар", "http://povar.ru", "варить",
                                  "варить", 100, 200, " ")


@pytest.fixture()
def vacancy_test2():
    return Vacancy(321, "popvar", "http://povar.ru", "test",
                                  "варить", 200, 300, " ")



def test_check_status_request(api_test1, api_test2):
    assert ApiHhVacancy.check_status_request(api_test1) is True
    assert ApiHhVacancy.check_status_request(api_test2) is False


def test_filter_vacancy_salary(vacancy_test1, vacancy_test2):
    list_vacancy = [vacancy_test1, vacancy_test2]
    assert Vacancy.filter_vacancy_salary(list_vacancy, 250) == [vacancy_test2]
