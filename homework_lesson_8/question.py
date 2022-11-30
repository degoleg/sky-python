class Question:
    def __init__(self, question_text, complexity, correct_answer):
        self.question_text = question_text # текст вопроса
        self.complexity = complexity # сложность вопроса
        self.correct_answer = correct_answer # верный вариант ответа

        self.is_asked = False # задан ли вопрос (по умолчанию False)
        self.user_response = None # ответ пользователя (по умолчанию None)
        self.score = self.complexity * 10 # сложность умноженное на 10

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.score


    def is_correct(self):
        """
        Возвращает True, если ответ пользователя совпадает
        с верным ответом иначе False.
        """
        return self.correct_answer == self.user_response # возвращает результат сравнения


    def build_question(self):
        """
        Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f'Вопрос: {self.question_text} \n' \
               f'Сложность: {self.complexity}/5'

    def build_feedback(self):
        """
        Возвращает :
        Ответ верный, получено __ баллов
        Возвращает :
        Ответ неверный, верный ответ __
        """
        if self.is_correct():
            return f'Ответ верный, получено {self.score} баллов'
        return f'Ответ неверный. Верный ответ – {self.correct_answer}'
