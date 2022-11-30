# лежат функции
import random
from basic_word import  BasicWord

def load_random_word(list_of_words):
    """
    Функция получает список слов с внешнего ресурса, выберает случайное слово,
    создаст экземпляр класса BasicWord и вернет этот экземпляр.
    :param list_of_words:
    :return:
    """
    return random.choice(list_of_words)

