from api_class import ApiHhVacancy
from vacancy_class import Vacancy
from process_vacancy_class import ProcessVacancy


name = input("Введите название вакансии : ")

vacansy_cls = ApiHhVacancy(name)
vacancy_get = ApiHhVacancy.get_answer(vacansy_cls)
ProcessVacancy.add_vacancy(vacancy_get)
print(f'Получено 50 вокансий из{vacancy_get["found"]}')
list_vacancy = Vacancy.create_vacancy(vacancy_get)
print("сколько вакансий показать")
top_n = int(input("введи число:"))

salary = int(input("Введите желаемую зарплату : "))

list_filtr_vacancy = Vacancy.filter_vacancy_salary(list_vacancy, salary)
sorted_vacancy = Vacancy.sort_vacansy_solary(list_filtr_vacancy)

i = 0
while i < top_n:
    print(sorted_vacancy[i])
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
