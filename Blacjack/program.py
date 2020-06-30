from Funkcje import funkcje
from Klasy.klasy import Deck, Hand, Card, Chips


##############################################################################
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input("\nHit czy Czekasz? Podaj h lub c\n-------------------------------\n")


        if x[0].lower() == 'h':
            funkcje.hit(deck, hand)

        elif x[0].lower() == 'c':
            print("Czekasz, kolej Dealera")

            playing = False

        else:
            print("Przepraszam, musisz podac h lub c!")
            continue
        break
##############################################################################

playing = True
# Ustaw żetony gracza
player_chips = Chips()  # ustawiono 100 żetonów na start

##############################################################################
while True:
    # Start gry
    print('Witam w grze BlackJack!\n')

    # Stwórz i potasuj Decka
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())



    # Przyjmij zakład gracza
    funkcje.take_bet(player_chips)

    # Pokaż karty (jednocześnie ukrywając jedną karte dealera)
    funkcje.show_some(player_hand,dealer_hand)

    while playing:  # pętla zależna od funkcji hit_or_deck

        # Grasz czy czekasz?
        hit_or_stand(deck,player_hand)


        # Pokaż karty (jednocześnie ukrywając jedną karte dealera)
        funkcje.show_some(player_hand,dealer_hand)

        # Jeżeli gracz przekroczył 21 włącz funkcję player_busts() i przerwij pętle
        if player_hand.value > 21:
            funkcje.player_busts(player_hand,dealer_hand,player_chips)
            break


    # Jeżeli gracz nie przekroczył 21, dealer gra dalej dopóki nie osiągnie 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            funkcje.hit(deck,dealer_hand)

        # Pokaż wszystkie karty
        funkcje.show_all(player_hand,dealer_hand)

        # Uruchom funkcję pokazującą kto wygrał
        if dealer_hand.value > 21:
            funkcje.dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            funkcje.dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            funkcje.player_wins(player_hand,dealer_hand,player_chips)

        else:
            funkcje.push(player_hand,dealer_hand)

    # Poinformuj gracza o ilości żetonów
    print("\nAktualne żetony gracza wynoszą: ",player_chips.total)

    if player_chips.total == 0:
        print("Nie posiadasz już żetonów! Koniec gry :(")
        break
    # Zapytaj czy gracz chcę zagrać ponownie
    new_game = input("Czy chcesz zagrać ponownie? Wpisz 't' lub 'n' ")

    if new_game[0].lower()=='t':
        playing=True
        continue
    else:
        print("Dzięki za gre!")
        break
