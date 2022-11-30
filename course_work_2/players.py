# класс игрока
class Player:
    """
    Класс одержит в себе имя пользователя и использованные слова пользователя.
    Методы получение количества использованных слов, добавление слова в использованные
    слова и проверка использования данного слова до этого.
    """
    def __init__(self, username, user_words_used=[]):
        self.username = username  # имя пользователя
        self.user_words_used = user_words_used  # использованные слова пользователя

    def get_the_number_of_words_used(self): # получение количества использованных слов (возвращает int)
        return len(self.user_words_used)

    def add_a_word_to_used_words(self, word): # добавление слова в использованные слова (ничего не возвращает)
        self.user_words_used.append(word)

    def check_earlier_word_usage(self): # проверка использования данного слова до этого (возвращает bool)
        if word in user_words_used:
            return True
        return False

    def __repr__(self):
        return f'Player {self.username} {self.user_words_used}'



