import random
from time import sleep

symbols_list = ("Clubs (♣)","Diamonds (♦)","Hearts (♥)","Spades (♠)")
values_list = (1,2,3,4,5,6,7,8,9,10,"King","Queen","Ace")

def main(): 
    game = Game()
    #Player draws first two cards
    game.player.draw(bool2=False)
    game.player.draw()
    #Dealer draws first two cards
    game.dealer.draw()
    game.dealer.draw(bool1=False, bool2=False)
    game.bust_or_blackjack()

    while True:
        game.round()

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
        return int(self.value)

    def __str__(self) -> str:
        return f"{self.value} of {self.suite} "
    
class Player:
    def __init__(self,name,deck): 
        self.name = name
        self.hand = []
        self.value = 0
        self.deck = deck
        self.count = 0
        self.doubledown = False

    #Draws a card, returns a card CLASS, appends it to the hand
    def draw(self, bool1=True, bool2=True): 
        card = self.deck.draw_card()
        self.hand.append(card)
        self.hand_value()
        self.count += 1
        self.can_double_down()

        if bool1:
            print(f"{self.name} drew the {card}")
        if bool2:
            print(f"Current Hand Value: {self.value}")
        sleep(2)
        
    def hand_value(self): 
        self.value = 0
        for card in self.hand: 
            x = card.card_value()
            self.value += x

        #Turns Aces into 1 if necessary
        while self.value > 21:
            for card in self.hand:
                x = card.card_value()
                if x == 11:
                    self.value -= 10
            break

    def can_double_down(self): 
        allowed = [9,10,11]
        if self.count == 2 and self.value in allowed: 
            self.doubledown = True

class Game:
    def __init__(self): 
        print("---Beggining game of blackjack!---\n")
        self.deck = Deck()
        self.player = Player("You",self.deck)
        self.dealer = Player("Dealer",self.deck)

    def bust_or_blackjack(self):
        if self.dealer.value == 21: 
            print("Dealer has blackjack!\nYou still have a chance to draw")
        if self.dealer.value > 21: 
            print("Dealer went bust!\n---You win!!!---")
            quit()
        if self.player.value == 21:
            print("You have blackjack!\n---You win!!!---")
            quit()
        if self.player.value > 21:
            print("You went bust. Better luck next time")
            quit()

    def show_down(self):
        print("---Beginning Showdown!---\n")
        print(f"Your current value is: {self.player.value}")
        print(f"Dealers current value is: {self.dealer.value}")
        sleep(3)
        self.dealer_hits()
        self.bust_or_blackjack()
        if self.dealer.value < self.player.value: 
            print(f"\n---YOU WIN!---\nPlayer: {self.player.value} Dealer: {self.dealer.value}")
            quit()
        if self.dealer.value == self.player.value: 
            print(f"\n---DRAW! NO ONE WINS RETURNING ALL BETS---\nPlayer: {self.player.value} Dealer: {self.dealer.value}")
            quit()
        print(f"\n---YOU LOSE! Better luck next time!---\nPlayer: {self.player.value} Dealer: {self.dealer.value}")
        quit()

    def dealer_hits(self):
        if self.dealer.value < 17:
            print("Dealer has decided to draw a card\n")
            self.dealer.draw()
    
    def round(self):
        print("It's your turn what would you like to do?\n1. Hit\n2. Stand")
        if self.player.doubledown:
            print("3. Double Down")
        try:
            choice = int(input("Please enter your choice(Number): "))
            match choice:
                case 1: 
                    self.player.draw()
                    self.bust_or_blackjack()
                case 2: 
                    self.show_down()
                case 3: 
                    self.player.draw()
                    self.bust_or_blackjack()
                    self.show_down()
                case _: raise ValueError
        except ValueError:
            print("\n--------->Please type in a valid number choice<---------\n")

if __name__ == "__main__": 
    main()