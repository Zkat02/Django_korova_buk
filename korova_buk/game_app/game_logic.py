from random import randint

from django.core.exceptions import ObjectDoesNotExist

from .models import BaseWords

class Computer_word:
    def __init__(self):
        "достаем слово из базы данных слов"
        self.computer_word = 'лиса'

    def get(self):
        return self.computer_word

    def change(self):
        n = BaseWords.objects.count()
        id_word = randint(1,n)


        self.computer_word = BaseWords.objects.get(pk=id_word).base_word



class User_Attempt():
    def __init__(self, word, computer_word):
        self.word = word
        self.bulls = self.count_bulls_in(computer_word)
        self.cows = self.count_cows_in(computer_word)

    def count_bulls_in(self, computer_word):
        amount_bulls = 0
        for i, ch in enumerate(self.word):
            if ch == computer_word[i]:
                amount_bulls += 1
        return amount_bulls

    def count_cows_in(self, computer_word):
        amount_cows = 0 - self.bulls  # коровы не считая быков
        for ch in self.word:
            if ch in computer_word:
                amount_cows += 1
        return amount_cows


class Game:
    all_attempts = []  # список попыток угадать слово

    def __init__(self):
        self.computer_word = Computer_word()
        print(self.computer_word)
        print(self.computer_word.get())
        self.win = False

    def check_win(self, user_atempt):
        return self.computer_word.get() == user_atempt

    def User_attempt(self, user_input):
        "добавляет введеное игроком слово в список попыток"
        user_attempt = User_Attempt(user_input, self.computer_word.get())
        self.win = self.check_win(user_input)
        self.all_attempts.append(user_attempt)
        print('computer_word', self.computer_word.get() )

    def get_context(self):
        context = {'all_attempts': self.all_attempts, 'win': self.win}
        return context

    def restart(self):
        self.computer_word.change()
        self.all_attempts.clear()
        self.win = False
