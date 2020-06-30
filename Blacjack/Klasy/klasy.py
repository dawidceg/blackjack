import random

suits = ('Kier', 'Karo', 'Pik', 'Trefl')
ranks = ('Dwója', 'Trójka', 'Czwórka', 'Piątka', 'Szóstka', 'Siódemka', 'Ósemka', 'Dziewiątka', 'Dziesiątka', 'Walet', 'Dama', 'Król', 'As')
values = {'Dwója':2, 'Trójka':3, 'Czwórka':4, 'Piątka':5, 'Szóstka':6, 'Siódemka':7, 'Ósemka':8, 'Dziewiątka':9, 'Dziesiątka':10, 'Walet':10,
         'Dama':10, 'Król':10, 'Król':11}


##############################################################################
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank+ " "+self.suit


##############################################################################
class Deck:

    #funkcja w której jest pętla dodająca obiekty Card do listy self.deck. Pętla przechodzi przez wszyskie znaki i wartości tworząc pełną talie
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank)) #dodaje obiekt np. Serce 2 do listy, potem Serce 3 i tak dalej


    def __str__(self):
        deck_comp = '' #pusty string
        for card in self.deck:
            deck_comp += '\n' + card.__str__() #dodaj nazwe karty do zmiennej deck_comp
        return "The deck has: " + deck_comp    #wyświetl całą talie

    def shuffle(self):
        random.shuffle(self.deck)  #miesza karty w liscie

    def deal(self):
        single_card = self.deck.pop()   #wyrzuć z tali jedną kartę i przypisz ją do zmiennej single_card, nastepnie zwróć ją 'return'
        return single_card

##############################################################################
class Hand:

    #aktualne karty w ręce - zaczynamy od 0
    def __init__(self):
        self.cards = []  # start z pustą listą
        self.value = 0   # start z wartością 0
        self.aces = 0    # atrybut do śledzenia czy są asy

    def add_card(self,card):
        self.cards.append(card) #dodaj do cards [] obiekt card(suit, rank) z tali Deck.deal(), czyli single_card (pojedyncza karta)
        self.value += values[card.rank]

        #sprawdź czy są asy u playera
        if card.rank == 'As':
            self.aces +=1

    def adjust_for_ace(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

##############################################################################
class Chips:

    def __init__(self, total = 100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
