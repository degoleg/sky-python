if __name__ == '__main__':

    from utils import *
    from basic_word import  BasicWord
    import requests
    import json

    response = requests.get('https://www.jsonkeeper.com/b/8FGG')
    data = response.json()

    random_word = load_random_word(data)

    print(random_word) # потом надо удалить !!!
    basicword = BasicWord(random_word['subwords'], random_word['subwords'])  # инициализация экземпляра класса BasicWord

    player_name = input("Ведите имя игрока\n")

    print(f"Привет, {player_name}\n"
          f"Составьте {len(random_word['subwords'])} слов из слова: {random_word['word']}\n"
          f"Слова должны быть не короче 3 букв\n"
          f"Чтобы закончить игру, угадайте все слова или напишите stop")

    user_word = input("Поехали, ваше первое слово?\n")













