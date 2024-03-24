from config import VACANCY_TXT


class Vacancy:
    id_vacancy: int
    name: str
    link: str
    requirement: str
    responsibility: str

    def __init__(self, id_vacancy, name, link, requirement, responsibility, salary_from, salary_to, schedule):
        self.id_vacancy = id_vacancy
        self.name = name
        self.link = link
        self.requirement = requirement
        self.responsibility = responsibility
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.schedule = schedule

    def __str__(self):
        if self.salary_from == 0:
            return (f'id: {self.id_vacancy}, {self.name} зарплата до {self.salary_to}\n'
                    f'{self.link}')
        if self.salary_to - self.salary_from == 1:
            return (f'id: {self.id_vacancy}, {self.name} зарплата от {self.salary_from} \n'
                    f'{self.link}')
        return (f'id: {self.id_vacancy}, {self.name} зарплата от {self.salary_from} до {self.salary_to}\n'
                f'{self.link} , {self.schedule}')

    @classmethod
    def create_vacancy(cls, list_answer):
        """создает список объектов класса Vacancy"""
        list_vacancy = []
        list_answer_item = list_answer["items"]
        for i in list_answer_item:
            new_obj_vacancy = cls(i["id"], i["name"], i['alternate_url'], i["snippet"]["requirement"],
                                  i["snippet"]["responsibility"], i["salary"]["from"], i["salary"]["to"], i["schedule"]["name"])
            list_vacancy.append(new_obj_vacancy)
        return list_vacancy

    @staticmethod
    def filter_vacancy_salary(list_vacancy, salary):
        """фильтрует список вакансий по заданной зарплате"""
        new_list_vacancy = []
        for i in list_vacancy:
            if i.salary_from is None:  # если нет значения присваивает 0
                i.salary_from = 0
            if i.salary_to is None and i.salary_from >= salary:  # если нет значения временно присваивает значение
                i.salary_to = i.salary_from + 1
                new_list_vacancy.append(i)
                continue
            if i.salary_to is None and i.salary_from < salary:
                continue
            if i.salary_from <= salary <= i.salary_to:
                new_list_vacancy.append(i)
        return new_list_vacancy

    @staticmethod
    def sort_vacansy_solary(list_vacancy):
        """сортирует список вакансий по уменьшению зарплаты"""
        sort_list = sorted(list_vacancy, key=lambda x: x.salary_from, reverse=True)
        new_sort_list = sorted(sort_list, key=lambda x: x.salary_to, reverse=True)
        return new_sort_list

    def add_vacancy_txt(self):
        """записывает выбраную вакансию в текстовый файл"""
        with open(VACANCY_TXT, 'a', encoding="utf-8") as f:
            f.write(self.__str__()+"\n")
