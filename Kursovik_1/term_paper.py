import random

MORSE_ENCODE_DICT = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}

WORDS_TO_PLAY = ["code", "bit", "list", "soul", "next"]




def get_random_word_from_list(words):
    """ Получает случайное слово из списка, слова могут повторяться"""
    random_word = random.choice(words)
    return random_word


def morse_encode(word, encoding_dict):
    """
    Кодирует букву морзянкой, возвращает строку через пробел
    """
    symbols_in_morse = []
    for symbol in word:
        symbols_in_morse.append(encoding_dict.get(symbol, "?"))

    return " ".join(symbols_in_morse)


def get_statistics(answers):
    """
    Собирает статистику в словаре формата {"total": , correct": , "incorrect": }
    """
    total = len(answers)
    correct = answers.count(True)
    incorrect = total - correct

    return {"total": total, "correct": correct, "incorrect": incorrect}


def print_statistics(statistics):
    """ Распечатывает статистику """
    print()
    print(f"Всего задачек:{statistics['total']}")
    print(f"Отвечено верно:{statistics['correct']}")
    print(f"Отвечено неверно:{statistics['incorrect']}")


def main():

    user_answers = []

    print("Сегодня мы потренируемся расшифровывать морзянку.")
    print("Нажмите Enter и начнем")
    input()

    for _ in range(len(WORDS_TO_PLAY)):

        word = get_random_word_from_list(WORDS_TO_PLAY)
        word_encoded = morse_encode(word, MORSE_ENCODE_DICT)
        print(word_encoded)

        print("Введите ваш ответ")
        user_input = input()

        if user_input == word:
            print(f"Верно, {word}!")
            user_answers.append(True)
        else:
            print(f"Неверно, {word}!")
            user_answers.append(False)

    # Разделим ответственность:
    # Сперва отдельно получим статистику
    game_statistics = get_statistics(user_answers)
    # Затем отдельно выведем
    print_statistics(game_statistics)


if __name__ == '__main__':
    main()