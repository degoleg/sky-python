import random

from utils import load_quest, build_statistics


filename = "questions.json"

questions = load_quest(filename) # вызов функции по загрузке вопросов

random.shuffle(questions) # перемешивание вопросов

for question in questions:
    print(question.build_question()) # задаем пользователю вопрос
    user_response = input("Ваш ответ: ") # считываем ответ
    question.user_response = user_response
    print(question.build_feedback())

build_statistics(questions) # получение статистики


