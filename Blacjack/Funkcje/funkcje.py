##############################################################################
def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("Ile chcesz obstawić?: "))
        except:
            print("Proszę podać liczbę!")
        else:
            if chips.bet > chips.total:
                print("Przepraszam, ale nie masz tylu żetonów. Ty posiadasz tylko {} żetonów".format(chips.total))
            else:
                break

##############################################################################
def hit(deck,hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()

##############################################################################
def show_some(player,dealer):
    print("\nKarty Dealera:")
    print(" <karta ukryta>")
    print('',dealer.cards[1])
    print("\nKarty gracza:", *player.cards, sep='\n ')

##############################################################################
def show_all(player,dealer):
    print("\nKarty Dealera:", *dealer.cards, sep='\n ')
    print("Karty Dealerad =",dealer.value)
    print("\nKarty gracza:", *player.cards, sep='\n ')
    print("Karty gracza =",player.value)

##############################################################################
def player_busts(player, dealer, chips):
    print("---------------\n|Gracz przegrał|\n---------------\n")
    chips.lose_bet()

##############################################################################
def player_wins(player, dealer, chips):
    print("--------------\n|Gracz wygrał|\n--------------\n")
    chips.win_bet()

##############################################################################
def dealer_busts(player, dealer, chips):
    print("-------------------------------\n|Gracz wygrał. Dealer przegrał|\n-------------------------------\n")
    chips.win_bet()

##############################################################################
def dealer_wins(player, dealer, chips):
    print("---------------\n|Dealer wygrał|\n---------------\n")
    chips.lose_bet()

##############################################################################
def push(player, dealer):
    print("Gracz zremisował z Dealerem")
