from src.vacancy_class import Vacancy
from src.function import start_request, communication_user

if __name__ == '__main__':

    i = 0

    vacancy_get = start_request()

    list_vacancy = Vacancy.create_vacancy(vacancy_get)  # создаем список экземпляров класса Vacancy
    print("сколько вакансий показать")
    top_n = int(input("введи число:"))

    salary = int(input("Введите желаемую зарплату : "))

    list_filtr_vacancy = Vacancy.filter_vacancy_salary(list_vacancy, salary)  # вильтруем список вакансий по желаемой зарплату
    sorted_vacancy = Vacancy.sort_vacansy_solary(list_filtr_vacancy)  # сортируем с писок вакансий по зарплате с ноибольшей

    while i < top_n:
        print(sorted_vacancy[i])  # выводим вакансии пользователю
        i += 1

    print(communication_user(top_n, i, sorted_vacancy))
