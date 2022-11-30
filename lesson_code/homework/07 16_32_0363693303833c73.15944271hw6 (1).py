# Импорт модулей random и os

import os
import random




def load_words_from_file(words_data):
    """
    Функция считывает данные из файла
    :param words_data: 'list_words.txt'
    :return: records
    """
    with open(os.path.join(words_data), encoding='utf-8') as f:
        records = f.read().splitlines()

    return records


def write_users_history(us_name, us_point):
    """
    Функция создает файл history_game_file.txt
    :param us_name: user_name
    :param us_point: str(count_points)
    :return: users_history
    """
    with open('history_game_file.txt', 'a+', encoding='utf-8') as f:
        f.write(f"{us_name}:{us_point}\n")


def shuffle_word(word):
    letter_word = list(word)
    random.shuffle(letter_word)
    return ''.join(letter_word)


def get_play(words):
    """
    Основная функция игры
    :param words: word_file
    :return: print(f'Угадайте слово: {mix_word}')
             user_variant = input()
             print(f'Верно! Вы получаете {count_points} очков.')
             print(f'Неверно! Верный ответ – {normal_word}')
        get_users_history(user_name, str(count_points))
    """
    count_points = 0
    for word in words:
        normal_word = word.strip()
        mix_word = shuffle_word(normal_word)
        user_variant = input(f'Угадайте слово: {mix_word}\n')
        if user_variant.lower() == word:
            count_points += 10
            print(f'Верно! Вы получаете {count_points} очков.')
        else:
            print(f'Неверно! Верный ответ – {word}')
    return count_points


def get_statistics(history):
    """
    Функция статистики игры
    :param history:
    :return:
    """
    with open(os.path.join(history), encoding='utf-8') as f:
        recs = [word for word in f.read().splitlines() if word]
    print(f'Всего игр сыграно: {len(recs)}\nМаксимальный рекорд: {max([int(_.split(":")[1]) for _ in recs])}')


# Ввод имени пользователя
user_name = input('Введите ваше имя:\n')

# вложение функции чтения файла со списком слов в переменную
word_file = load_words_from_file('list_words.txt')
# Вызов функций
user_result = get_play(word_file)
write_users_history(user_name, user_result)
get_statistics('history_game_file.txt')
