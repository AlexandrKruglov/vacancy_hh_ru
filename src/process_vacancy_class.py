from abc import ABC, abstractmethod
import json
from config import VACANCY_JSON


class Processing(ABC):
    @abstractmethod
    def add_vacancy(self, dict_vacancy):
        pass

    @abstractmethod
    def get_vacancy(self):
        pass

    @abstractmethod
    def del_vacancy(self, id_vacancy):
        pass


class ProcessVacancy(Processing):

    @classmethod
    def add_vacancy(cls, dict_vacancy):
        """записываем вакансии в json файл"""
        with open(VACANCY_JSON, 'w', encoding="utf-8") as f:
            json.dump(dict_vacancy, f)

    @classmethod
    def get_vacancy(cls):
        """получаем вакансии из json файла"""
        with open(VACANCY_JSON, 'r', encoding="utf-8") as f:
            vacancy_list = json.load(f)
            return vacancy_list

    @classmethod
    def del_vacancy(cls, id_vacancy):
        """удаляем выбраную вакансию из файла"""
        data_temp = ProcessVacancy.get_vacancy()
        j = 0
        for i in data_temp["items"]:
            if id_vacancy == int(i["id"]):
                data_temp["items"].pop(j)
                ProcessVacancy.add_vacancy(data_temp)
                return "вакансия удалена"
            else:
                j += 1
        return "нет такой вакансии"
