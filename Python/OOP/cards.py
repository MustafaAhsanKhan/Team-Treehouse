class Card:
    def __init__(self, word, position):
        self.word = word
        self.position = position
        self.matched = False

    def __eq__(self, other):  # Checking if two cards are equal
        if(self.word == other.word):
            self.matched = True
            other.matched = True
            return True
        else:
            return False
        
    def __str__(self):
        return self.word
    
if __name__ == "__main__":  # Testing
    card1 = Card("egg", "A1")
    card2 = Card("egg", "A3")
    card3 = Card("ham", "A2")

    print(card1 == card2)
    print(card1 == card3)