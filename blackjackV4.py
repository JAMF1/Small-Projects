import random
from time import sleep

symbols_list = ("Clubs (♣)","Diamonds (♦)","Hearts (♥)","Spades (♠)")
values_list = (1,2,3,4,5,6,7,8,9,10,"King","Queen","Ace")

def main():
    print("---Beginning game of blackjack---\n")
    player_1 = Player()
    dealer = Player()
    
    print(f"Handing out cards\nYour first card is the {player_1.card_description1}")
    sleep(3)
    print(f"Your second card is the {player_1.card_description2}\nCurrent value is {player_1.value}\n")
    sleep(4)

    print(f"The dealers first card is the {dealer.card_description1}\n")

    if blackjack(dealer.value):
        print("Checking for blackjack...")
        sleep(2)
        print("Dealer has Blackjack! You can still draw if you get 21")
    if blackjack(player_1.value):
        print("You got Blackjack! Congratulations you win!")
        quit()
    
    if can_double_down(player_1.value):
        while True:
            choice = input("It's your turn, what woud you like to do? \n1.Hit (Draw a card)\n2.Stand\n3.Double Down\n").lower()
            match choice:
            
                case "hit": 
                    card, description = draw_card()
                    player_1.cards_in_hand.append(card)
                    player_1.update_value()
                    print(f"You drew the {description}, current value is {player_1.value}")

                    if bust(player_1.value):
                        print(f"You've gone bust! Your cards ammounted to a value of {player_1.value}. Better luck next time")
                        quit()
                    if blackjack(player_1.value):
                        print("You got Blackjack! Congratulations you win!")
                        quit()

                    if dealer_hits():
                        card, description = draw_card()
                        dealer.cards_in_hand.append(card)
                        dealer.update_value()

                    if bust(dealer.value):
                        print("Dealer went bust! You won!")
                        quit()
                    break

                case "stand": 
                    if dealer_hits():
                        card, description = draw_card()
                        dealer.cards_in_hand.append(card)

                    if bust(dealer.value):
                        print("Dealer went bust! You won!")
                        quit()
                    show_down(player_1.value, dealer.value, dealer.card_description2)

                case "double down": 
                    card, description = draw_card()
                    player_1.cards_in_hand.append(card)
                    print(f"You drew the {description}")
                    player_1.update_value
                    if bust(player_1.value):
                        print(f"You've gone bust! Your cards ammounted to a value of {player_1.value}. Better luck next time")
                        quit()
                    if blackjack(player_1.value):
                        print("You got Blackjack! Congratulations you win!")
                        quit()

                    if dealer_hits():
                        card, description = draw_card()
                        dealer.cards_in_hand.append(card)
                        dealer.update_value()

                    if bust(dealer.value):
                        print("Dealer went bust! You won!")
                        quit()
                    show_down(player_1.value, dealer.value, dealer.card_description2)

                case _: 
                    print("Please type one of the given choices")
                    continue


    while True:
        choice = input("What woud you like to do? \n1.Hit (Draw a card)\n2.Stand\n").lower()
        match choice:
            
            case "hit": 
                card, description = draw_card()
                player_1.cards_in_hand.append(card)
                player_1.update_value()
                print(f"You drew the {description}, current value is {player_1.value}")

                if bust(player_1.value):
                    print(f"You've gone bust! Your cards ammounted to a value of {player_1.value}. Better luck next time")
                    quit()
                if blackjack(player_1.value):
                    print("You got Blackjack! Congratulations you win!")
                    quit()

                if dealer_hits():
                    card, description = draw_card()
                    dealer.cards_in_hand.append(card)
                    dealer.update_value()

                if bust(dealer.value):
                    print("Dealer went bust! You won!")
                    quit()

            case "stand": 
                if dealer_hits():
                    card, description = draw_card()
                    dealer.cards_in_hand.append(card)
                    dealer.update_value()

                if bust(dealer.value):
                    print("Dealer went bust! You won!")
                    quit()
                show_down(player_1.value, dealer.value, dealer.card_description2)
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
    print(f"The dealers second card is..\nthe {desc}! Bringing his value to {dealer}")
    if player > dealer:
        print("You won!")
        print(player, "vs", dealer)
        quit()
    if player < dealer:
        print("You lost")
        print(player, "vs", dealer)
        quit()

def dealer_hits(): 
    x = random.randint(0,1)
    if x == 1: 
        return True
    return False
    

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

def blackjack(value):
    if value == 21: return True
    return False

def bust(value):
    if value > 21: return True
    return False

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


#Player and dealer draw two cards
#Check if either has black jack
#Next round starts
#Draw a card