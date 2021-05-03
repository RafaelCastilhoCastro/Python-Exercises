from random import shuffle

SUITE = 'of Hearts-of Diamonds-of Spades-of Clubs'.split('-')
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    full_deck = []
    def __init__(self,suit,rank):
        for i in SUITE:
            for j in RANKS:
                self.full_deck.append(j+' '+i)
        
    def shuf(self):
        shuffle(self.full_deck)

    def splitting(self):
        pl1.hand_pl.half_deck = self.full_deck[::2]
        pl2.hand_pl.half_deck = self.full_deck[1::2]


class Hand:
    def __init__(self):
        self.half_deck = []

    def add_pool(self):
        global pool
        self.half_deck.extend(pool)
        pool = []

    def remove_3(self):
        for i in range(3):
            pool.append(self.half_deck.pop(0))


class Player:
    def __init__(self,name):
        self.name = name
        self.hand_pl = Hand()

    def play_card(self):
        picked_card = self.hand_pl.half_deck.pop(0)
        pool.append(picked_card)
        print(self.name+' draws')
        print(picked_card)
        print()
        
    def check_cards(self):
        return len(self.hand_pl.half_deck) <= 0


def card_ranking(card):
    if card[0] == 'A':
        return 14
    elif card[0] == 'K':
        return 13
    elif card[0] == 'Q':
        return 12
    elif card[0] == 'J':
        return 11
    elif card[0] == '1':
        return 10
    else:
        return int(card[0])


#GAME PLAY

print("Welcome to War, let's begin...")

pool=[]

deck1 = Deck(SUITE,RANKS)
deck1.shuf()

name = input("Player one inform your name.")

pl1 = Player(name)
pl2 = Player("Player 2")

deck1.splitting()

input('Press Enter to pick a card from your deck.')

game_on = True

while game_on:

    pl1.play_card()
    pl2.play_card()
    
    if card_ranking(pool[-1]) < card_ranking(pool[-2]):
        pl1.hand_pl.add_pool()
        print(pl1.name+"'s card is higher.")
    elif card_ranking(pool[-1]) > card_ranking(pool[-2]):
        pl2.hand_pl.add_pool()
        print(pl2.name+"'s card is higher.")
    else:
        try:     
            pl1.hand_pl.remove_3()
        except:
            print(pl1.name+" doesn't have enough cards for WAR!")
            print(pl2.name+" wins.")
            game_on = False
            break

        try:
            pl2.hand_pl.remove_3()
        except:
            print(pl2.name+" doesn't have enough cards for WAR!")
            print(pl1.name+" wins.")
            game_on = False
            break

        print('WAR! both players added 3 cards to the pool.')

    if pl1.check_cards():
        print(pl1.name+' is out of cards.')
        print(pl2.name+' wins.')
        game_on = False
        break
    elif pl2.check_cards():
        print(pl2.name+' is out of cards.')
        print(pl1.name+' wins.')
        game_on = False
        break

    print()
    print(pl1.name+' deck: '+str(len(pl1.hand_pl.half_deck))+' cards.')
    print(pl2.name+' deck: '+str(len(pl2.hand_pl.half_deck))+' cards.')
    input("Press Enter to continue.")





