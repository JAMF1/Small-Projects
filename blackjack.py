import random
from time import sleep

symbols_list = ("Clubs (♣)","Diamonds (♦)","Hearts (♥)","Spades (♠)")
values_list = (1,2,3,4,5,6,7,8,9,10,"King","Queen","Ace")


class Deck:
    def __init__(self): 
        #Creates a list of CARD objects for each combination of cards and shuffles them
        self.cards = [Card(value,suite) for value in values_list for suite in symbols_list]
        random.shuffle(self.cards)

    def draw_card(self):
        #Draws ONE card by calling on the POP function, pop function deletes and returns the last item in the list 
        return self.cards.pop()
    
    def cards_remaining(self): 
        return len(self.cards)


class Card:
    def __init__(self, value, suite):
        self.value = value
        self.suite = suite

    def card_value(self):
        if self.value == "Ace": 
            return 11
        if self.value == "King" or self.value == "Queen": 
            return 10
        return self.value

    def __str__(self) -> str:
        return f"{self.value} of {self.suite} "
    
class Player:
    def __init__(self): 
        self.hand = []
        self.value = 0
        self.can_doubledown = False

    #Draws a card, returns a card CLASS, appends it to the hand, and updates value
    def draw(self, deck): 
        self.card = deck.draw_card()
        self.hand.append(self.card)
        print(f"You got the {self.card}")
        self.hand_value()

    def hand_value(self): 
        for card in self.hand: 
            x = card.card_value 
            



class Game:
    def __init__(self): 
        self.player = Player()
        self.dealer = Player()
        self.deck = Deck()


def main(): 
    game = Game()
    game.player.draw(game.deck)




if __name__ == "__main__": 
    main()