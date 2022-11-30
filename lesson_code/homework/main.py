import random


def reading_top_players(user):
    """
    функция записывает игрока в топ

    """
    with open("history.txt", "w", encoding="utf-8") as file:
        user_name = file.write(user)
        return user_name


def reading_words_from_a_function():
    """
    Функция читает и перемешивает поочередно слова файла words.txt

    """
    with open('words.txt') as files:
        score = 0
        for item in files:

            word_from_the_list = item.strip()
            new_list = list(word_from_the_list)
            random.shuffle(new_list)
            mixed_word = "".join(new_list)
            print(f"Угадайте слово : {mixed_word}")
            user_response = input()
            if user_response == word_from_the_list:
                print("Верно! Вы получаете 10 очков")
                score += 10
            else:
                print(f"Неверно! Верный ответ – {word_from_the_list} ")

        return score


username = input("Введите ваше имя\n")


reading_top_players(username)


result = reading_words_from_a_function()











