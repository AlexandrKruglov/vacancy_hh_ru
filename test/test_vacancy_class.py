import pytest

from src.vacancy_class import Vacancy


@pytest.fixture()
def vacancy_test1():
    return Vacancy(123, "повар", "http://povar.ru", "варить",
                                  "варить", 100, 200, " ")


@pytest.fixture()
def vacancy_test2():
    return Vacancy(321, "popvar", "http://povar.ru", "test",
                                  "варить", 200, 300, " ")


def test_filter_vacancy_salary(vacancy_test1, vacancy_test2):
    list_vacancy = [vacancy_test1, vacancy_test2]
    assert Vacancy.filter_vacancy_salary(list_vacancy, 250) == [vacancy_test2]


def test_sort_vacansy_solary(vacancy_test1, vacancy_test2):
    list_vacancy = [vacancy_test1, vacancy_test2]
    assert Vacancy.sort_vacansy_solary(list_vacancy) == [vacancy_test2, vacancy_test1]
    assert Vacancy.sort_vacansy_solary(list_vacancy) != [vacancy_test1, vacancy_test2]
