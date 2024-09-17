import random



class Card:
    def __init__(self, suit, value, comparing_value, suit_value):
        self.suit = suit
        self.value = value
        self.comparing_value = comparing_value
        self.suit_value = suit_value

    def __str__(self):
        return f"{self.suit}{self.value}"
    
class Deck:
    def __init__(self, cards=None):
        if cards:
            self.cards = cards
        else:
            self.cards = []
        
    def show_cards(self):
        for card in self.cards:
            print(f"{card.suit}{card.value}")



    def view_card(self):
       rand_card = random.randint(0, (len(cards)-1))
       random_card = self.cards[rand_card]
       cards.remove(random_card)
       return random_card
    
    
    def compare_card_value(self):
        higher_card = 0
        lower_card = 0

        rand_card = random.randint(0, (len(cards)-1))
        compare_card1 = self.cards[rand_card]


        rand_card = random.randint(0, (len(cards)-1))
        compare_card2 = self.cards[rand_card]

 
        while compare_card1 == compare_card2:
            compare_card2 = random.randint(0, len(cards))
            compare_card2 = self.cards[rand_card]
        
        if compare_card1.comparing_value == compare_card2.comparing_value:
            if compare_card1.suit_value >= compare_card2.suit_value:
                higher_card = compare_card1
                lower_card = compare_card2
            else:
                higher_card = compare_card2
                lower_card = compare_card1
        elif compare_card1.comparing_value >= compare_card2.comparing_value:
            higher_card = compare_card1
            lower_card = compare_card2
        else:
            higher_card = compare_card2
            lower_card = compare_card1
        return (f"\nKort 1 är {compare_card1} och kort 2 är {compare_card2}\n\nDen större av de är {higher_card}, det är högre än {lower_card}\n")



    @staticmethod
    def make_deck():
        suits = ["♥","♠","♦","♣"]

        values = [" K", " Q", " J", " 10", " 9", " 8", " 7", " 6", " 5", " 4", " 3", " 2", " A"]

        cards = []


        for i in range(4):
            current_suit = suits[i]
            for j in range(13):

                cards.append(Card(current_suit, values[j], 12-j, 3-i)) 

        return cards

cards = Deck.make_deck()

deck = Deck(cards)

while True:
    answer = int(input("\n\nVad vill du göra? \n\nVisa alla kort: 1\n\nTa ut ett slumpmässigt kort från kortleken: 2\n\nBlanda kortleken: 3\n\nDra två slumpmässiga kort och jämför värden: 4\n\nAvsluta: 5\n\nSkriv: "))

    if answer == 1:
        deck.show_cards()
    elif answer == 2:
        print (f"\n{deck.view_card()}")
    elif answer == 3:
        random.shuffle(cards)
    elif answer == 4:
        print(f"\n{deck.compare_card_value()}")
    elif answer == 5:
        break
    else: 
        print("\n\nInte giltigt svar\n")