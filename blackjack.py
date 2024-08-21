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


class Card:
    def __init__(self, value, suite):
        self.value = value
        self.suite = suite
    

    def __str__(self) -> str:
        return f"{self.value} of {self.suite} "
    
class Player:
    def __init__(self,name): 
        self.name = name
        self.hand = []
        self.value = 0
        self.can_doubledown = False

    #Draws a card and updates value
    def draw(self): 
        ...

class Game:
    def __init__(self) -> None:
        player = Player(input("Player name: "))
        dealer = Player("Dealer")
        deck = Deck()

#TODO Implement draw feature 


s = Game()