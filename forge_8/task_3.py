# Задача 3
# Создайте класс Word. У него есть одно поле – value. Добавьте методы: get_value() - возвращает значение
# , set_value(new_value) - задает новое слово, get_letters() –  метод возвращает уникальный сет букв текущего слова.
# has_letter(letter) – возвращает есть ли переданная буква в текущем слове. – Не забудьте про repr!


class Word:
    def __init__(self, value):
        self.vaue = value


