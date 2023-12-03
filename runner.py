from code2048.game2048 import Game2048
from translator.translator2048.translator2048 import Translator2048


class Runner:
    def __init__(self):
        self.game = Game2048()
        self.translator = Translator2048(self.game)

    def reset(self):
        print("Resetting game")
        self.translator.start_game()