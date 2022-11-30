from utils import *

student_number = int(input("Введите номер студента \n"))
students = load_students()

student = get_student_by_pk(student_number, students) # студент по pk

# проверка существование такого пользователя
if student:
    print(f'Студент: {student["full_name"]}')
    knows = ', '.join(student["skills"])
    print(f'Знает: {knows}')
else:
    print("У нас нет такого студента")
    quit()


profession_name = input(f"Выберите специальность для оценки студента\n")
professions = load_professions()

profession = get_profession_by_title(profession_name, professions) # получение профессии

# проверка существования запрашиваемой профессии
if not profession:
    print("У нас нет такой специальности")
    quit()
# получение необходимфх параметров используя методы множеств
output_dict = (check_fitness(student, profession))

print(result_output(output_dict, student['full_name']))
