import json

from question import Question

def load_quest(filename): # функция для работы с файлом
    questions = []
    with open(filename, "r", encoding="utf-8") as file:
        list_quest = json.load(file)
    for item in list_quest:
        question_text = item["q"]
        complexity = int(item["d"])
        correct_answer = item["a"]
        question = Question(question_text, complexity, correct_answer) # вопросы считываются и раскладываются в экземпляры класса Question
        questions.append(question)
    return questions

def build_statistics(questions): # выводится статистика на основе списка questions
    score = 0 # текущий счет
    count = 0 # количество правильных ответов

    for question in questions:
        if question.is_correct(): # использование метода is_correct
            score = score + question.score # увеличиваем score на количество баллов которые даются за этот вопрос
            count += 1

    return f'Вот и всё! \n' \
           f'Отвечено {count} вопроса из 10 \n' \
           f'Набрано баллов: {score}'
