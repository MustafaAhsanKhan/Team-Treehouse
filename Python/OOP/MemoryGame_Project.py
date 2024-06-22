import cards
import random

class Game:
    def __init__(self):
        self.size = 4
        self.grid = []
        self.card_options = ["Ham", "Egg", "Cat", "Dog", "Log", "Ice", "Bat", "Bag"]
        self.columns = ['A', 'B', 'C', 'D']
        self.locations = []

        for col in self.columns:
            for x in range(1, self.size + 1):
                self.locations.append(f"{col}{x}")  # This will create the locations eg. A1, B4

    def run(self):
        self.setCards()
        win = False
        while(win == False):
            self.displayBoard()
            # Taking input from the user
            choice1 = input("Enter the first card: ")
            choice2 = input("Enter the second card: ")

            # Finding the cards in the grid
            card1 = self.findCard(choice1)
            card2 = self.findCard(choice2)

            # Checking if the cards are equal
            if(card1 == card2):
                print("It's a match!")

            # Checking if all the cards are matched
            
            
        
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
        print("A1   A2   A3   A4")
        print("-----------------")
        print("B1   B2   B3   B4")
        print("-----------------")
        print("C1   C2   C3   C4")
        print("-----------------")
        print("D1   D2   D3   D4")
        print("-----------------")

if __name__ == "__main__":
    game = Game()
    game.run()
    for card in game.grid:
        print(f"Card: {card.word}, Location: {card.position}")
