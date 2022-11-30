import json
import  os


def load_students():
    """
    Загружает список студентов из файла
    :return:
    """
    with open("students.json") as file:
        sstudents_list = json.load(file)
    return sstudents_list


def load_professions():
    """
    Загружает список профессий из файла
    :return:
    """
    with open("professions.json") as file:
        list_of_professions = json.load(file)
    return  list_of_professions


def get_student_by_pk(pk, list_dictionaries):
    """
    Получает словарь с данными студента по его pk
    :param pk:
    :return:
    """
    for item in list_dictionaries:
        if pk == item["pk"]:
            return item


def get_profession_by_title(title, list_professions):
    """
    Получает словарь с инфо о профе по названию
    :param title:
    :return:
    """
    for item in list_professions:
        if title == item["title"]:
            return item


def check_fitness(student, profession):
    """
    функция которая получив студента и профессию, возвращает словарь типа:
    {
  "has": ["Python", "Linux"],
  "lacks": ["Docker, SQL"],
  "fit_percent": 50
    }
    :param student:
    :param profession:
    :return:
    """
    set_student = set(student["skills"])  # избавляемся от повторений
    set_profession = set(profession["skills"]) # скилы которые необходимы для данной прфессии

    has_an_intersection = set_student.intersection(set_profession) # скилы которыми обладает
    lack_of_skills = set_profession.difference(set_student) # не хватка скилов

    fitness_percentage = round(len(has_an_intersection) / len(set_profession) * 100) # процент пригодности к профессии

    result = {
        "has": has_an_intersection,
        "lacks": lack_of_skills,
        "fit_percent": fitness_percentage
    }

    return result


def result_output(output_dict, user_name):
    """
    функция вывода результата
    :return:
    """
    has = ', '.join(output_dict['has'])
    lacks = ', '.join(output_dict['lacks'])

    result_out = f'Пригодность: {output_dict["fit_percent"]} \n' \
                 f'{user_name} знает {has} \n' \
                 f'{user_name} не знает {lacks} \n'
    return  result_out
