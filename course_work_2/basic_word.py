# класс слова
class BasicWord:
    """
    Класс использует методы проверки исходного слова в списке допустимых
    подслов и подсчет количества подслов.

    """
    def __init__(self, rnd_word, set_of_subwords=[]): # поля исходное слово и набор допустимых подслов
        self.word = ' '
        self.rnd_word = rnd_word # исходное слово
        self.set_of_subwords = set_of_subwords # набор допустимых подслов

    def checking_the_entered_word(self, word): # проверка введенного слова (вернет bool)
        if self.set_of_subwords == word: # ??????????????
            return True
        return False

    def counting_the_number_of_subwords(self): # подсчет количества подслов (вернет int)
        return len(self.set_of_subwords)

    def __repr__(self):
        return f'BasicWord {self.rnd_word} {self.set_of_subwords}'



