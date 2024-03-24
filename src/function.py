from src.api_class import ApiHhVacancy
from src.process_vacancy_class import ProcessJsonVacancy


def start_request():
    while True:
        name = input("Введите название вакансии : ")

        vacansy_cls = ApiHhVacancy(name)  # создаем экземрляр класса ApiHhVacancy

        if vacansy_cls.check_status_request is False:  # проверяем статус запроса
            raise "ошибка запроса"
        vacancy_get = ApiHhVacancy.get_answer(vacansy_cls)  # получаем ответ  с hh.ru по заданной вакансии
        ProcessJsonVacancy.add_vacancy(vacancy_get)  # записываем ответ с сайта в json файл

        if vacancy_get["found"] == 0:  # проверяем есть ли вакансии по данному запросу
            print("вакансий нет повторите запрос")
            continue
        print(f'Получено 50 вокансий из {vacancy_get["found"]}')
        break
    return vacancy_get


def communication_user(top_n, i, sorted_vacancy):
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
            print(ProcessJsonVacancy.del_vacancy(c))
            continue
        if n == "end":
            break
        else:
            print("вы ввели не верное значение")
            continue
    return 'досвидания'
