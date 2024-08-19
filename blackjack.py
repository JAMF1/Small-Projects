import random
from time import sleep


symbols_list = ("Clubs (♣)","Diamonds (♦)","Hearts (♥)","Spades (♠)")
values_list = (1,2,3,4,5,6,7,8,9,10,"King","Queen","Ace")


#Classes
class Game:
    #Sets up deck and players
    def __init__(self): 
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Player("Dealer")

    #Handles flow of game, turns, actions, winning conditions like blackjack and bust
    def start_game(self): 
        ...


class Player:
    #Store and manage players hand, calculates value of hands, player actions like hit stand and double down
    def __init__(self, name): 
        self.name = name
        self.hand = []
        self.value = 0
        self.double_down = False
        
    def draw_card(self):
        self.card = Deck.deal_card()

    def update_hand_value(self):
        ...

class Deck:
    #Creating and shuffling the deck, provides card to players, no repeated cards
    def __init__(self): 
        self.cards = [Card(value, suit) for suit in symbols_list for value in values_list]
        random.shuffle(self.cards)

    def deal_card(self): 
        ...


class Card:
    def __init__(self, value, suit): 
        self.value = value
        self.suit = suit

    def determine_value(self): 
        ...

    def __str__(self):
        return f"{self.value} of {self.suit}"