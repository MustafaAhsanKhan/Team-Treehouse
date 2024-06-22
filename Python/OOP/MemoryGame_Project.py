import cards
import random

class Game:
    def __init__(self):
        self.size = 4
        self.grid = []
        self.card_options = ["Ham", "Egg", "Cat", "Dog", "Log", "Ice", "Bat", "Bag"]
        self.columns = ['A', 'B', 'C', 'D']
        self.locations = []
        self.revealed = {}  # To track revealed cards

        for col in self.columns:
            for x in range(1, self.size + 1):
                self.locations.append(f"{col}{x}")  # This will create the locations eg. A1, B4

    def run(self):
        self.setCards()
        win = False
        while not win:
            self.displayBoard()
            # Taking input from the user
            choice1 = input("Enter the first card (e.g., A1): ")
            choice2 = input("Enter the second card (e.g., B2): ")

            # Finding the cards in the grid
            card1 = self.findCard(choice1)
            card2 = self.findCard(choice2)

            # Checking if the cards are equal
            if card1.word == card2.word:
                print(f"It's a match! You selected {card1.word} and {card2.word}.")
                self.revealed[choice1] = card1.word
                self.revealed[choice2] = card2.word
            else:
                print(f"Not a match. You selected {card1.word} and {card2.word}. Try again.")

            # Checking if all the cards are matched
            if len(self.revealed) == len(self.card_options) * 2:
                win = True
                print("Congratulations! You've matched all the cards!")
                
    def setCards(self):
        for x in self.card_options:
            for y in range(2):
                random_location = random.choice(self.locations)
                self.locations.remove(random_location)  # Remove the chosen location
                self.grid.append(cards.Card(x, random_location))

    def findCard(self, location):
        for card in self.grid:
            if card.position == location:
                return card
                
    def displayBoard(self):
        for col in self.columns:
            row = []
            for x in range(1, self.size + 1):
                loc = f"{col}{x}"
                if loc in self.revealed:
                    row.append(self.revealed[loc])
                else:
                    row.append(loc)
            print("   ".join(row))
            print("-----------------")

if __name__ == "__main__":
    game = Game()
    game.run()
    for card in game.grid:
        print(f"Card: {card.word}, Location: {card.position}")