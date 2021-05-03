'''
TO DO:
- Double down

'''
player_cards = []
dealer_cards = []
deck = []

def deck_shuffle():
	global deck
	global player_cards
	global dealer_cards
	deck = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]*5
	import random
	random.shuffle(deck)
	player_cards = []
	dealer_cards = []

# DEALER HANDS
def dealer_show1():
	global dealer_cards
	global dealer_cards_count
	dealer_cards_count = 1
	dealer_cards.append(deck[0])
	check_sum_dealer()
	deck.pop(0)
	print()
	print(" << Dealer")
	print(" ____"+"  ____")
	print(f"|{dealer_cards[0]:2}  |"+"|    |")
	print("|    |"+"| ** |")
	print(f"|__{dealer_cards[0]:>2}|"+"|____|")
	print("Total: ",dealer_sumtotal)
	print()

def dealer_show2():
	global dealer_cards
	global dealer_cards_count
	dealer_cards_count = 2
	dealer_cards.append(deck[0])
	check_sum_dealer()
	deck.pop(0)
	print()
	print(" << Dealer")
	print(" ____"+"  ____")
	print(f"|{dealer_cards[0]:2}  |"+f"|{dealer_cards[1]:2}  |")
	print("|    |"+"|    |")
	print(f"|__{dealer_cards[0]:>2}|"+f"|__{dealer_cards[1]:>2}|")
	print("Total: ",dealer_sumtotal)
	print()

def dealer_show3():
	global dealer_cards
	global dealer_cards_count
	dealer_cards_count = 3
	dealer_cards.append(deck[0])
	check_sum_dealer()
	deck.pop(0)
	print()
	print(" << Dealer")
	print(" ____"+"  ____"+"  ____")
	print(f"|{dealer_cards[0]:2}  |"+f"|{dealer_cards[1]:2}  |"+f"|{dealer_cards[2]:2}  |")
	print("|    |"+"|    |"+"|    |")
	print(f"|__{dealer_cards[0]:>2}|"+f"|__{dealer_cards[1]:>2}|"+f"|__{dealer_cards[2]:>2}|")
	print("Total: ",dealer_sumtotal)
	print()

def dealer_show4():
	global dealer_cards
	global dealer_cards_count
	dealer_cards_count = 4
	dealer_cards.append(deck[0])
	check_sum_dealer()
	deck.pop(0)
	print()
	print(" << Dealer")
	print(" ____"+"  ____"+"  ____"+"  ____")
	print(f"|{dealer_cards[0]:2}  |"+f"|{dealer_cards[1]:2}  |"+f"|{dealer_cards[2]:2}  |"+f"|{dealer_cards[3]:2}  |")
	print("|    |"+"|    |"+"|    |"+"|    |")
	print(f"|__{dealer_cards[0]:>2}|"+f"|__{dealer_cards[1]:>2}|"+f"|__{dealer_cards[2]:>2}|"+f"|__{dealer_cards[3]:>2}|")
	print("Total: ",dealer_sumtotal)
	print()

def dealer_show5():
	global dealer_cards
	global dealer_cards_count
	dealer_cards_count = 5
	dealer_cards.append(deck[0])
	check_sum_dealer()
	deck.pop(0)
	print()
	print(" << Dealer")
	print(" ____"+"  ____"+"  ____"+"  ____"+"  ____")
	print(f"|{dealer_cards[0]:2}  |"+f"|{dealer_cards[1]:2}  |"+f"|{dealer_cards[2]:2}  |"+f"|{dealer_cards[3]:2}  |"+f"|{dealer_cards[4]:2}  |")
	print("|    |"+"|    |"+"|    |"+"|    |"+"|    |")
	print(f"|__{dealer_cards[0]:>2}|"+f"|__{dealer_cards[1]:>2}|"+f"|__{dealer_cards[2]:>2}|"+f"|__{dealer_cards[3]:>2}|"+f"|__{dealer_cards[4]:>2}|")
	print("Total: ",dealer_sumtotal)
	print()

def dealer_show6():
	global dealer_cards
	global dealer_cards_count
	dealer_cards_count = 6
	dealer_cards.append(deck[0])
	check_sum_dealer()
	deck.pop(0)
	print()
	print(" << Dealer")
	print(" ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____")
	print(f"|{dealer_cards[0]:2}  |"+f"|{dealer_cards[1]:2}  |"+f"|{dealer_cards[2]:2}  |"+f"|{dealer_cards[3]:2}  |"+f"|{dealer_cards[4]:2}  |"+f"|{dealer_cards[5]:2}  |")
	print("|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |")
	print(f"|__{dealer_cards[0]:>2}|"+f"|__{dealer_cards[1]:>2}|"+f"|__{dealer_cards[2]:>2}|"+f"|__{dealer_cards[3]:>2}|"+f"|__{dealer_cards[4]:>2}|"+f"|__{dealer_cards[5]:>2}|")
	print("Total: ",dealer_sumtotal)
	print()

def dealer_show7():
	global dealer_cards
	global dealer_cards_count
	dealer_cards_count = 7
	dealer_cards.append(deck[0])
	check_sum_dealer()
	deck.pop(0)
	print()
	print(" << Dealer")
	print(" ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____")
	print(f"|{dealer_cards[0]:2}  |"+f"|{dealer_cards[1]:2}  |"+f"|{dealer_cards[2]:2}  |"+f"|{dealer_cards[3]:2}  |"+f"|{dealer_cards[4]:2}  |"+f"|{dealer_cards[5]:2}  |"+f"|{dealer_cards[6]:2}  |")
	print("|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |")
	print(f"|__{dealer_cards[0]:>2}|"+f"|__{dealer_cards[1]:>2}|"+f"|__{dealer_cards[2]:>2}|"+f"|__{dealer_cards[3]:>2}|"+f"|__{dealer_cards[4]:>2}|"+f"|__{dealer_cards[5]:>2}|"+f"|__{dealer_cards[6]:>2}|")
	print("Total: ",dealer_sumtotal)
	print()

def dealer_show8():
	global dealer_cards
	global dealer_cards_count
	dealer_cards_count = 8
	dealer_cards.append(deck[0])
	check_sum_dealer()
	deck.pop(0)
	print()
	print(" << Dealer")
	print(" ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____")
	print(f"|{dealer_cards[0]:2}  |"+f"|{dealer_cards[1]:2}  |"+f"|{dealer_cards[2]:2}  |"+f"|{dealer_cards[3]:2}  |"+f"|{dealer_cards[4]:2}  |"+f"|{dealer_cards[5]:2}  |"+f"|{dealer_cards[6]:2}  |"+f"|{dealer_cards[7]:2}  |")
	print("|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |")
	print(f"|__{dealer_cards[0]:>2}|"+f"|__{dealer_cards[1]:>2}|"+f"|__{dealer_cards[2]:>2}|"+f"|__{dealer_cards[3]:>2}|"+f"|__{dealer_cards[4]:>2}|"+f"|__{dealer_cards[5]:>2}|"+f"|__{dealer_cards[6]:>2}|"+f"|__{dealer_cards[7]:>2}|")
	print("Total: ",dealer_sumtotal)
	print()

def dealer_show9():
	global dealer_cards
	global dealer_cards_count
	dealer_cards_count = 9
	dealer_cards.append(deck[0])
	check_sum_dealer()
	deck.pop(0)
	print()
	print(" << Dealer")
	print(" ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____")
	print(f"|{dealer_cards[0]:2}  |"+f"|{dealer_cards[1]:2}  |"+f"|{dealer_cards[2]:2}  |"+f"|{dealer_cards[3]:2}  |"+f"|{dealer_cards[4]:2}  |"+f"|{dealer_cards[5]:2}  |"+f"|{dealer_cards[6]:2}  |"+f"|{dealer_cards[7]:2}  |"+f"|{dealer_cards[8]:2}  |")
	print("|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |")
	print(f"|__{dealer_cards[0]:>2}|"+f"|__{dealer_cards[1]:>2}|"+f"|__{dealer_cards[2]:>2}|"+f"|__{dealer_cards[3]:>2}|"+f"|__{dealer_cards[4]:>2}|"+f"|__{dealer_cards[5]:>2}|"+f"|__{dealer_cards[6]:>2}|"+f"|__{dealer_cards[7]:>2}|"+f"|__{dealer_cards[8]:>2}|")
	print("Total: ",dealer_sumtotal)
	print()

def dealer_show10():
	global dealer_cards
	global dealer_cards_count
	dealer_cards_count = 10
	dealer_cards.append(deck[0])
	check_sum_dealer()
	deck.pop(0)
	print()
	print(" << Dealer")
	print(" ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____")
	print(f"|{dealer_cards[0]:2}  |"+f"|{dealer_cards[1]:2}  |"+f"|{dealer_cards[2]:2}  |"+f"|{dealer_cards[3]:2}  |"+f"|{dealer_cards[4]:2}  |"+f"|{dealer_cards[5]:2}  |"+f"|{dealer_cards[6]:2}  |"+f"|{dealer_cards[7]:2}  |"+f"|{dealer_cards[8]:2}  |"+f"|{dealer_cards[9]:2}  |")
	print("|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |")
	print(f"|__{dealer_cards[0]:>2}|"+f"|__{dealer_cards[1]:>2}|"+f"|__{dealer_cards[2]:>2}|"+f"|__{dealer_cards[3]:>2}|"+f"|__{dealer_cards[4]:>2}|"+f"|__{dealer_cards[5]:>2}|"+f"|__{dealer_cards[6]:>2}|"+f"|__{dealer_cards[7]:>2}|"+f"|__{dealer_cards[8]:>2}|"+f"|__{dealer_cards[9]:>2}|")
	print("Total: ",dealer_sumtotal)
	print()

def dealer_show11():
	global dealer_cards
	global dealer_cards_count
	dealer_cards_count = 11
	dealer_cards.append(deck[0])
	check_sum_dealer()
	deck.pop(0)
	print()
	print(" << Dealer")
	print(" ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____")
	print(f"|{dealer_cards[0]:2}  |"+f"|{dealer_cards[1]:2}  |"+f"|{dealer_cards[2]:2}  |"+f"|{dealer_cards[3]:2}  |"+f"|{dealer_cards[4]:2}  |"+f"|{dealer_cards[5]:2}  |"+f"|{dealer_cards[6]:2}  |"+f"|{dealer_cards[7]:2}  |"+f"|{dealer_cards[8]:2}  |"+f"|{dealer_cards[9]:2}  |"+f"|{dealer_cards[10]:2}  |")
	print("|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |")
	print(f"|__{dealer_cards[0]:>2}|"+f"|__{dealer_cards[1]:>2}|"+f"|__{dealer_cards[2]:>2}|"+f"|__{dealer_cards[3]:>2}|"+f"|__{dealer_cards[4]:>2}|"+f"|__{dealer_cards[5]:>2}|"+f"|__{dealer_cards[6]:>2}|"+f"|__{dealer_cards[7]:>2}|"+f"|__{dealer_cards[8]:>2}|"+f"|__{dealer_cards[9]:>2}|"+f"|__{dealer_cards[10]:>2}|")
	print("Total: ",dealer_sumtotal)
	print()

def dealer_show12():
	global dealer_cards
	global dealer_cards_count
	dealer_cards_count = 12
	dealer_cards.append(deck[0])
	check_sum_dealer()
	deck.pop(0)
	print()
	print(" << Dealer")
	print(" ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____")
	print(f"|{dealer_cards[0]:2}  |"+f"|{dealer_cards[1]:2}  |"+f"|{dealer_cards[2]:2}  |"+f"|{dealer_cards[3]:2}  |"+f"|{dealer_cards[4]:2}  |"+f"|{dealer_cards[5]:2}  |"+f"|{dealer_cards[6]:2}  |"+f"|{dealer_cards[7]:2}  |"+f"|{dealer_cards[8]:2}  |"+f"|{dealer_cards[9]:2}  |"+f"|{dealer_cards[10]:2}  |"+f"|{dealer_cards[11]:2}  |")
	print("|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |"+"|    |")
	print(f"|__{dealer_cards[0]:>2}|"+f"|__{dealer_cards[1]:>2}|"+f"|__{dealer_cards[2]:>2}|"+f"|__{dealer_cards[3]:>2}|"+f"|__{dealer_cards[4]:>2}|"+f"|__{dealer_cards[5]:>2}|"+f"|__{dealer_cards[6]:>2}|"+f"|__{dealer_cards[7]:>2}|"+f"|__{dealer_cards[8]:>2}|"+f"|__{dealer_cards[9]:>2}|"+f"|__{dealer_cards[10]:>2}|"+f"|__{dealer_cards[11]:>2}|")
	print("Total: ",dealer_sumtotal)
	print()

# PLAYER HANDS
def player_show2():
	global player_cards
	global player_cards_count
	player_cards_count = 2
	player_cards.append(deck[0])
	check_sum_player()
	deck.pop(0)
	player_cards.append(deck[0])
	check_sum_player()
	deck.pop(0)
	print()
	print(" >> Player")
	print(" ____"+"  ____")
	print(f"|{player_cards[0]:2}  |"+f"|{player_cards[1]:2}  |")
	print("Total: ",player_sumtotal)
	print()

def player_show3():
	global player_cards
	global player_cards_count
	player_cards_count = 3
	player_cards.append(deck[0])
	check_sum_player()
	deck.pop(0)
	print()
	print(" >> Player")
	print(" ____"+"  ____"+"  ____")
	print(f"|{player_cards[0]:2}  |"+f"|{player_cards[1]:2}  |"+f"|{player_cards[2]:2}  |")
	print("Total: ",player_sumtotal)
	print()

def player_show4():
	global player_cards
	global player_cards_count
	player_cards_count = 4
	player_cards.append(deck[0])
	check_sum_player()
	deck.pop(0)
	print()
	print(" >> Player")
	print(" ____"+"  ____"+"  ____"+"  ____")
	print(f"|{player_cards[0]:2}  |"+f"|{player_cards[1]:2}  |"+f"|{player_cards[2]:2}  |"+f"|{player_cards[3]:2}  |")
	print("Total: ",player_sumtotal)
	print()

def player_show5():
	global player_cards
	global player_cards_count
	player_cards_count = 5
	player_cards.append(deck[0])
	check_sum_player()
	deck.pop(0)
	print()
	print(" >> Player")
	print(" ____"+"  ____"+"  ____"+"  ____"+"  ____")
	print(f"|{player_cards[0]:2}  |"+f"|{player_cards[1]:2}  |"+f"|{player_cards[2]:2}  |"+f"|{player_cards[3]:2}  |"+f"|{player_cards[4]:2}  |")
	print("Total: ",player_sumtotal)
	print()

def player_show6():
	global player_cards
	global player_cards_count
	player_cards_count = 6
	player_cards.append(deck[0])
	check_sum_player()
	deck.pop(0)
	print()
	print(" >> Player")
	print(" ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____")
	print(f"|{player_cards[0]:2}  |"+f"|{player_cards[1]:2}  |"+f"|{player_cards[2]:2}  |"+f"|{player_cards[3]:2}  |"+f"|{player_cards[4]:2}  |"+f"|{player_cards[5]:2}  |")
	print("Total: ",player_sumtotal)
	print()

def player_show7():
	global player_cards
	global player_cards_count
	player_cards_count = 7
	player_cards.append(deck[0])
	check_sum_player()
	deck.pop(0)
	print()
	print(" >> Player")
	print(" ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____")
	print(f"|{player_cards[0]:2}  |"+f"|{player_cards[1]:2}  |"+f"|{player_cards[2]:2}  |"+f"|{player_cards[3]:2}  |"+f"|{player_cards[4]:2}  |"+f"|{player_cards[5]:2}  |"+f"|{player_cards[6]:2}  |")
	print("Total: ",player_sumtotal)
	print()

def player_show8():
	global player_cards
	global player_cards_count
	player_cards_count = 8
	player_cards.append(deck[0])
	check_sum_player()
	deck.pop(0)
	print()
	print(" >> Player")
	print(" ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____")
	print(f"|{player_cards[0]:2}  |"+f"|{player_cards[1]:2}  |"+f"|{player_cards[2]:2}  |"+f"|{player_cards[3]:2}  |"+f"|{player_cards[4]:2}  |"+f"|{player_cards[5]:2}  |"+f"|{player_cards[6]:2}  |"+f"|{player_cards[7]:2}  |")
	print("Total: ",player_sumtotal)
	print()

def player_show9():
	global player_cards
	global player_cards_count
	player_cards_count = 9
	player_cards.append(deck[0])
	check_sum_player()
	deck.pop(0)
	print()
	print(" >> Player")
	print(" ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____")
	print(f"|{player_cards[0]:2}  |"+f"|{player_cards[1]:2}  |"+f"|{player_cards[2]:2}  |"+f"|{player_cards[3]:2}  |"+f"|{player_cards[4]:2}  |"+f"|{player_cards[5]:2}  |"+f"|{player_cards[6]:2}  |"+f"|{player_cards[7]:2}  |"+f"|{player_cards[8]:2}  |")
	print("Total: ",player_sumtotal)
	print()

def player_show10():
	global player_cards
	global player_cards_count
	player_cards_count = 10
	player_cards.append(deck[0])
	check_sum_player()
	deck.pop(0)
	print()
	print(" >> Player")
	print(" ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____")
	print(f"|{player_cards[0]:2}  |"+f"|{player_cards[1]:2}  |"+f"|{player_cards[2]:2}  |"+f"|{player_cards[3]:2}  |"+f"|{player_cards[4]:2}  |"+f"|{player_cards[5]:2}  |"+f"|{player_cards[6]:2}  |"+f"|{player_cards[7]:2}  |"+f"|{player_cards[8]:2}  |"+f"|{player_cards[9]:2}  |")
	print("Total: ",player_sumtotal)
	print()

def player_show11():
	global player_cards
	global player_cards_count
	player_cards_count = 11
	player_cards.append(deck[0])
	check_sum_player()
	deck.pop(0)
	print()
	print(" >> Player")
	print(" ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____")
	print(f"|{player_cards[0]:2}  |"+f"|{player_cards[1]:2}  |"+f"|{player_cards[2]:2}  |"+f"|{player_cards[3]:2}  |"+f"|{player_cards[4]:2}  |"+f"|{player_cards[5]:2}  |"+f"|{player_cards[6]:2}  |"+f"|{player_cards[7]:2}  |"+f"|{player_cards[8]:2}  |"+f"|{player_cards[9]:2}  |"+f"|{player_cards[10]:2}  |")
	print("Total: ",player_sumtotal)
	print()

def player_show12():
	global player_cards
	global player_cards_count
	player_cards_count = 12
	player_cards.append(deck[0])
	check_sum_player()
	deck.pop(0)
	print()
	print(" >> Player")
	print(" ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____"+"  ____")
	print(f"|{player_cards[0]:2}  |"+f"|{player_cards[1]:2}  |"+f"|{player_cards[2]:2}  |"+f"|{player_cards[3]:2}  |"+f"|{player_cards[4]:2}  |"+f"|{player_cards[5]:2}  |"+f"|{player_cards[6]:2}  |"+f"|{player_cards[7]:2}  |"+f"|{player_cards[8]:2}  |"+f"|{player_cards[9]:2}  |"+f"|{player_cards[10]:2}  |"+f"|{player_cards[11]:2}  |")
	print("Total: ",player_sumtotal)
	print()

def opening():
	print("-+-  ****   **        *       **    **    **         ***     *       **    **    **")
	print("     **  *  **      ** **   **  **  **  **            **   ** **   **  **  **  **")
	print("     ****   **     *******  **      ****         **   **  *******  **      ****")
	print("     **  *  **     **   **  **  **  **  **       **   **  **   **  **  **  **  **    -+-")
	print("     ****   *****  **   **    **    **    **      ******  **   **    **    **    **")
	print("     ==============================================================================")
	print()
	input("						Digite qualquer tecla para começar.")
	print("\n"*5)
	new_round()

saldo = 1000
bet_aux = ""
bet = 0
bet_pool = 0

def bets():
	global saldo
	global bet_aux
	global bet
	global bet_pool
	print("	Seu saldo: $", saldo)
	print("																	Aposta mín: $10")
	print("																	Aposta máx: $100")
	print()
	while True:
		bet_aux = input("Defina sua aposta.")
		print()
		try:
			bet = int(bet_aux)
		except:
			print("Ops. Por favor digite novamente.")
			print()
		else:
			if bet < 10:
				print("Ops. A aposta mínima é de $10.")
				print()
				continue
			elif bet > 100:
				print("Ops. A aposta máxima é de $100.")
				print()
				continue
			else:
				saldo -= bet
				bet_pool += bet
				print("Aposta realizada.")
				print()
				print("	Saldo atual: $", saldo)
				print()
				break

dealer_sumA1 = 0
dealer_sumA11 = 0
dealer_sumtotal = 0

def check_sum_dealer():
	global dealer_sumA1
	global dealer_sumA11
	global dealer_sumtotal

	if dealer_cards[-1] == "A":
		dealer_sumA1 += 1
		dealer_sumA11 += 11
	elif dealer_cards[-1] in "JQK":
		dealer_sumA1 += 10
		dealer_sumA11 +=10
	else:
		dealer_sumA1 += int(dealer_cards[-1])
		dealer_sumA11 += int(dealer_cards[-1])

	if dealer_sumA11 < 22:
		dealer_sumtotal = dealer_sumA11
	else:
		dealer_sumtotal = dealer_sumA1

player_sumA1 = 0
player_sumA11 = 0
player_sumtotal = 0

def check_sum_player():
	global player_sumA1
	global player_sumA11
	global player_sumtotal

	if player_cards[-1] == "A":
		player_sumA1 += 1
		player_sumA11 += 11
	elif player_cards[-1] in "JQK":
		player_sumA1 += 10
		player_sumA11 +=10
	else:
		player_sumA1 += int(player_cards[-1])
		player_sumA11 += int(player_cards[-1])

	if player_sumA11 < 22:
		player_sumtotal = player_sumA11
	else:
		player_sumtotal = player_sumA1

player_blackjack = False
dealer_blackjack = False

def check_player_blackjack():
	global player_blackjack
	if (player_cards[0] in "JQK" and player_cards[1] == "A") or (player_cards[0] == "A" and player_cards[1] in "JQK"):
		player_blackjack = True

def check_dealer_blackjack():
	global dealer_blackjack
	if (dealer_cards[0] in "JQK" and dealer_cards[1] == "A") or (dealer_cards[0] == "A" and dealer_cards[1] in "JQK"):
		dealer_blackjack = True

def check_end_blackjack():
	global bet_pool
	global saldo
	if player_blackjack == True:
		dealer_show2()
		player_show2()
		check_dealer_blackjack()
		if dealer_blackjack == True:
			print("Empate.")
			print()
			input("Digite qualquer tecla para continuar.")
			print()
			saldo += bet_pool
			bet_pool = 0
			new_round()
		else:
			print("BLACKJACK! O jogador vence.")
			print()
			input("Digite qualquer tecla para continuar.")
			print()
			saldo += bet_pool*2.5
			bet_pool = 0
			new_round()
	elif dealer_blackjack == True:
		print()
		print("BLACKJACK! O dealer vence.")
		print()
		input("Digite qualquer tecla para continuar.")
		print()
		bet_pool = 0
		new_round()

choice = 0

def options():		#incompleto
	global choice
	print("1 - Hit")
	print("2 - Stand")
	print("3 - Double down")
	while True:
		try:
			choice = int(input("Digite a opção correspondente. (1-3)"))
		except:
			print("Opção inválida.")
		else:
			if choice < 1 or choice > 3:
				print("Opção inválida.")
				continue
			elif choice == 1:
				player_streak()
			elif choice == 2:
				dealer_streak()
			elif choice == 3:
				pass

player_cards_count = 0

def hit_player():
	if player_cards_count == 0:
		player_show2()
	elif player_cards_count == 2:
		player_show3()
	elif player_cards_count == 3:
		player_show4()
	elif player_cards_count == 4:
		player_show5()
	elif player_cards_count == 5:
		player_show6()
	elif player_cards_count == 6:
		player_show7()
	elif player_cards_count == 7:
		player_show8()
	elif player_cards_count == 8:
		player_show9()
	elif player_cards_count == 9:
		player_show10()
	elif player_cards_count == 10:
		player_show11()
	elif player_cards_count == 11:
		player_show12()

dealer_cards_count = 0

def hit_dealer():
	if dealer_cards_count == 0:
		dealer_show1()
	elif dealer_cards_count == 1:
		dealer_show2()
	elif dealer_cards_count == 2:
		dealer_show3()
	elif dealer_cards_count == 3:
		dealer_show4()
	elif dealer_cards_count == 4:
		dealer_show5()
	elif dealer_cards_count == 5:
		dealer_show6()
	elif dealer_cards_count == 6:
		dealer_show7()
	elif dealer_cards_count == 7:
		dealer_show8()
	elif dealer_cards_count == 8:
		dealer_show9()
	elif dealer_cards_count == 9:
		dealer_show10()
	elif dealer_cards_count == 10:
		dealer_show11()
	elif dealer_cards_count == 11:
		dealer_show12()


def check_end():
	global bet_pool
	global saldo
	if player_sumtotal > 21:
		print("O jogador estourou! O dealer vence.")
		print()
		input("Digite qualquer tecla para continuar.")
		print()
		bet_pool = 0
		new_round()
	elif dealer_sumtotal > 21:
		print("O dealer estourou! O jogador vence.")
		print()
		input("Digite qualquer tecla para continuar.")
		print()
		saldo += bet_pool*2
		bet_pool = 0
		new_round()
	elif dealer_sumtotal >= 17 and dealer_sumtotal > player_sumtotal:
		print("O dealer vence.")
		print()
		input("Digite qualquer tecla para continuar.")
		print()
		bet_pool = 0
		new_round()
	elif dealer_sumtotal >= 17 and dealer_sumtotal < player_sumtotal:
		print("O jogador vence.")
		print()
		input("Digite qualquer tecla para continuar.")
		print()
		saldo += bet_pool*2
		bet_pool = 0
		new_round()
	elif dealer_sumtotal >= 17 and dealer_sumtotal == player_sumtotal:
		print("Empate.")
		print()
		input("Digite qualquer tecla para continuar.")
		print()
		saldo += bet_pool
		bet_pool = 0
		new_round()

def zero():
	global player_cards_count
	player_cards_count = 0
	global dealer_cards_count
	dealer_cards_count = 0
	global dealer_sumtotal
	dealer_sumtotal = 0
	global player_sumtotal
	player_sumtotal = 0
	global player_sumA1
	player_sumA1 = 0
	global player_sumA11
	player_sumA11 = 0
	global dealer_sumA1
	dealer_sumA1 = 0
	global dealer_sumA11
	dealer_sumA11 = 0

def new_round():
	zero()
	deck_shuffle()
	bets()
	hit_dealer()
	hit_player()
	check_player_blackjack()
	check_end_blackjack()
	options()

def player_streak():
	hit_player()
	check_end()
	options()

def dealer_streak():
	hit_dealer()
	if dealer_cards_count == 2:
		check_dealer_blackjack()
		if dealer_blackjack == True:
			check_end_blackjack()
		check_end()
		print()
		input("Digite qualquer tecla para continuar.")
		print()
		dealer_streak()
	else:
		check_end()
		print()
		input("Digite qualquer tecla para continuar.")
		print()
		dealer_streak()



opening()