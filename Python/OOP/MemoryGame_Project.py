import cards
import random

class Game:
    def __init__(self):
        self.size = 4
        self.grid = []
        self.card_options = ["Ham", "Egg", "Cat", "Dog"
                      "Egg", "Dog", "Cat", "Ham"]
        self.columns = ['A', 'B', 'C', 'D']
        self.locations = []

        for col in self.columns:
            for x in range(1, self.size + 1):
                self.locations.append(f"{col}{x}")  # This will create the locations eg. A1, B4

    def setCards(self):
        for x in self.card_options:
            for y in range(2):
                


if __name__ == "__main__":
    game = Game()