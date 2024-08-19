import random
from time import sleep

symbols_list = ("Clubs (♣)","Diamonds (♦)","Hearts (♥)","Spades (♠)")
values_list = (1,2,3,4,5,6,7,8,9,10,"King","Queen","Ace")


def main(): 
    print("---Beginning game of blackjack---\n")
    player = Player()
    dealer = Player()
    
    #Initial Round
    print("Handing out cards\n")
    sleep(3)
    print(f"Your first card is the {player.card_description1}")
    sleep(3)
    print(f"Your second card is the {player.card_description2}\nCurrent value is --{player.value}--\n")
    sleep(3)
    print(f"The dealers first card is the {dealer.card_description1}\n") 
    sleep(2)

    blackjack("dealer", dealer.value)
    blackjack("player", player.value)

    #Next Rounds
    while True:
        if can_double_down(player.value): 
            choice = input("It's your turn, what woud you like to do? \n1.Hit (Draw a card)\n2.Stand\n3.Double Down\n").lower()
        else:   
            choice = input("What woud you like to do? \n1.Hit (Draw a card)\n2.Stand\n").lower()

        match choice:
            case "hit": 
                card, description = draw_card()
                player.cards_in_hand.append(card)
                player.update_value()

                bust("player", player.value)
                print(f"\nYou drew the {description}, current value is {player.value}\n")
                blackjack("player", player.value)

                if dealer_hits(dealer.value):
                    card, description = draw_card()
                    dealer.cards_in_hand.append(card)
                    dealer.update_value()
                    bust("dealer", dealer.value)
                    print(f"Dealer drew the {description}")
                    blackjack("dealer", dealer.value)

            case "stand": 
                if dealer_hits(dealer.value):
                    card, description = draw_card()
                    dealer.cards_in_hand.append(card)
                    dealer.update_value()
                    bust("dealer",dealer.value)
                    print(f"Dealer drew the {description}")
                    blackjack("dealer", dealer.value)
                show_down(player.value, dealer.value, dealer.card_description2)

            case "double down": 
                card, description = draw_card()
                player.cards_in_hand.append(card)
                player.update_value()

                bust("player", player.value)
                print(f"You drew the {description}, current value is {player.value}")
                blackjack("player", player.value)

                if dealer_hits(dealer.value):
                    card, description = draw_card()
                    dealer.cards_in_hand.append(card)
                    dealer.update_value()
                    bust("dealer", dealer.value)
                    print(f"Dealer drew the {description}")
                    blackjack("dealer", dealer.value)
                show_down(player.value, dealer.value, dealer.card_description2)

            case _: 
                print("Please type one of the given choices")
                continue



#Actions
def draw_card(): 
    card_value = random.choice(values_list)
    card_suite = random.choice(symbols_list)
    card_description = f"{card_value} of {card_suite}"
    return card_value, card_description

def show_down(player, dealer, desc):
    print("Beggining show down!")
    sleep(4)
    print(f"Revealing dealers second card... {desc}! Bringing his value to {dealer}")
    if player > dealer:
        print("You won!")
        print(player, "vs", dealer)
        quit()
    if player < dealer:
        print("You lost")
        print(player, "vs", dealer)
        quit()

def dealer_hits(value: int): 
    if value >= 17:
        return False
    print("Dealer is drawing a card")
    sleep(2)
    return True


#Rules and Checks
def get_value(hand: list):
    value = 0
    test = 0
    for card in hand:
        if is_ace(card):
            card_value = convert(card)
            test += card_value
            if test > 21:
                card_value = 1
                value += card_value
            else: 
                value += card_value
        card_value = convert(card)
        value += card_value
        test += card_value
    return value

def is_ace(card):
    if card == "Ace": return True
    return False

def convert(card): 
    if card == "Ace":
        return 11
    if card == "King" or card == "Queen":
        return 10
    return card

def blackjack(name: str, value: int): 
    if value == 21:
        print("Checking for blackjack...")
        sleep(3)
        print(f"{name} has blackjack!")
        if name == "player": 
            print("You win congratulations!")
            quit()
        print("You can still get 21 and draw!\n")
        sleep(2)
    return

def bust(name: str, value: int):
    if value > 21 and name == "player": 
        print(f"You went bust! Better luck next time. Card value: {value}")
        quit()
    if value > 21 and name == "dealer": 
        print(f"Dealer went bust! You've won as a result, congratulations!")
        quit()
    return

def can_double_down(value): 
    if value == 9 or value == 10:
        return True
    return False


#Classes
class Player:
    def __init__(self) -> None:
        c1, cd1 = draw_card()
        c2, cd2 = draw_card()
        self.cards_in_hand = []
        self.card_description1 = cd1
        self.card_description2 = cd2
        self.cards_in_hand.append(c1)
        self.cards_in_hand.append(c2)
        self.value = get_value(self.cards_in_hand)

    def update_value(self):
        self.value = get_value(self.cards_in_hand)

if __name__ == "__main__":
    main()