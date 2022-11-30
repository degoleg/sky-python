# Импорт модулей os и random
import os

import random


def word_reading(word_guess):
    """
    Функция считывает данные из файла
    words.txt
    return: records
    """
    with open(os.path.join(word_guess), encoding='utf-8') as file:
        records = file.read().splitlines()

    return records


def user_history(name, user_score):
    """
    Функция записи статистики игр
    """
    with open('history.txt', 'a+', encoding='utf-8') as file:

        username = file.write(name + ':')
        score = file.write(user_score + '\n')
        users_history = username + score

        return users_history


def word_guessing(words):
    """
    Функция игры по разгадыванию слова

    """
    count_score = 0

    count = 0

    for word in words:
        normal_word = word.strip().strip(' ')
        letter_word = list(normal_word)
        random.shuffle(letter_word)
        mix_word = ''.join(letter_word)
        print(f'Угадайте слово: {mix_word}')
        user_variant = input()

        if user_variant.lower() == word:
            count_score += 10
            count += 1
            print(f'Верно! Вы получаете {count_score} очков.')
        else:
            print(f'Неверно! Верный ответ – {normal_word}')
            count += 1

    user_history(user_name, str(count_score))


def user_statistics(history):
    """
    Функция статистики игры
    Всего сыграно игр и max рекорд
    """
    total_games = 0
    all_score = ''
    with open(os.path.join(history), encoding='utf-8') as file:
        for item_data in file:
            if item_data.count(':') < 1:
                continue
            user, score = item_data.strip().split(':')
            total_games += 1
            all_score += score + ' '
            list_score = all_score.strip().split(' ')
            max_record = max(list_score)

    print(f'Всего игр сыграно: {total_games}\nМаксимальный рекорд: {max_record}')


# Ввод имени пользователя
user_name = input('Введите ваше имя' + '\n')

# чтение слова из файла
text_file = word_reading('words.txt')

# Функция вызова игры угадывания слова
word_guessing(text_file)

# Вывод статистики
print()
user_statistics('history.txt')

