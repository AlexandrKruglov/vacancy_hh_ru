from api_class import ApiHhVacancy
from vacancy_class import Vacancy
from process_vacancy_class import ProcessVacancy


i = 0

while True:
    name = input("Введите название вакансии : ")

    vacansy_cls = ApiHhVacancy(name)  # создаем экземрляр класса ApiHhVacancy

    if vacansy_cls.check_status_request is False:  # проверяем статус запроса
        raise "ошибка запроса"
    vacancy_get = ApiHhVacancy.get_answer(vacansy_cls)  # получаем ответ  с hh.ru по заданной вакансии
    ProcessVacancy.add_vacancy(vacancy_get)  # записываем ответ с сайта в json файл

    if vacancy_get["found"] == 0:  # проверяем есть ли вакансии по данному запросу
        print("вакансий нет повторите запрос")
        continue
    print(f'Получено 50 вокансий из{vacancy_get["found"]}')
    break

list_vacancy = Vacancy.create_vacancy(vacancy_get)  # создаем список экземпляров класса Vacancy
print("сколько вакансий показать")
top_n = int(input("введи число:"))

salary = int(input("Введите желаемую зарплату : "))

list_filtr_vacancy = Vacancy.filter_vacancy_salary(list_vacancy, salary)  # вильтруем список вакансий по желаемой зарплату
sorted_vacancy = Vacancy.sort_vacansy_solary(list_filtr_vacancy)  # сортируем с писок вакансий по зарплате с ноибольшей

while i < top_n:
    print(sorted_vacancy[i])  # выводим вакансии пользователю
    i += 1
while True:
    print("вы можете вывести еще 5 вакансии написав -- more\n"
          "добавить вакансию в текстовый док. написав + её id -- +123456\n"
          "удалить вакансию написав - id -- -123456\n"
          "выйти написав --end")
    n = input(" : ")
    if n == "more":
        top_n += 5
        while i < top_n:
            print(sorted_vacancy[i])
            i += 1
        continue
    if n[0] == "+":
        for item in sorted_vacancy:
            if item.id_vacancy == n[1:]:
                item.add_vacancy_txt()
        continue
    if n[0] == "-":
        c = int(n[1:])
        ProcessVacancy.del_vacancy(c)
        continue
    if n == "end":
        break
    else:
        print("вы ввели не верное значение")
        continue
