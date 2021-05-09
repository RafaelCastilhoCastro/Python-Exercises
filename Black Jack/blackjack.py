# --- OPENING ---
def opening():
	print("-+-  ****   **        *       **    **    **         ***     *       **    **    **")
	print("     **  *  **      ** **   **  **  **  **            **   ** **   **  **  **  **")
	print("     ****   **     *******  **      ****         **   **  *******  **      ****")
	print("     **  *  **     **   **  **  **  **  **       **   **  **   **  **  **  **  **    -+-")
	print("     ****   *****  **   **    **    **    **      ******  **   **    **    **    **")
	print("     ==============================================================================")
	print()
	input("						            Press any key to start.")
	print("\n"*5)


# --- BETS ---
balance = 1000

def bets():
	global balance
	if balance == 0:
		while True:
			newRound = input('No balance. Buy-in again?')
			if newRound.lower() == 'y' or newRound.lower() == 'yes':
				balance = 1000
				print()
				break
			else:
				print("Please try again.")
	global betPool
	betPool = 0
	print("	Your balance: $", balance)
	print("									Min bet: $10")
	print("									Max bet: $100")
	print()
	while True:
		betInput = input("Place your bet.")
		print()
		try:
			betInt = int(betInput)
		except:
			print("Please try again.")
			print()
		else:
			if betInt > balance:
				print('Insufficient balance.')
				print()
			elif betInt < 10:
				print("The min bet is $10.")
				print()
			elif betInt > 100:
				print("The max bet is $100.")
				print()
			else:
				balance -= betInt
				betPool += betInt
				print("Bet accepted.")
				print()
				print("	Current balance: $", balance)
				print()
				break


# --- DECK ---
def deck_shuffle():
	global deck
	deck = []
	cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
	for i in range(24):
		for j in cards:
			deck.append(j)
	import random
	random.shuffle(deck)


# --- HIT AND SHOW CARDS ---
def dealerHit():
	global dealerCards
	global dealerSums
	global dealerTotal
	global deck
	dealerCards.append(deck[-1])
	deck.pop()
	cardValues = checkSum(dealerCards)
	dealerSums[0] += cardValues[0]
	dealerSums[1] += cardValues[1]
	dealerTotal = cardsTotalSum(dealerSums)


def playerHit():
	global playerCards
	global playerSums
	global playerTotal
	global deck
	playerCards.append(deck[-1])
	deck.pop()
	cardValues = checkSum(playerCards)
	playerSums[0] += cardValues[0]
	playerSums[1] += cardValues[1]
	playerTotal = cardsTotalSum(playerSums)


def showCards():
	print("Dealer's cards:")
	print(dealerCards)
	print(f"Dealer's total: {dealerTotal}")
	print()
	print('Your cards:')
	print(playerCards)
	print(f'Your total: {playerTotal}')
	print()


# --- CARDS SUM WITH ACE=1 AND ACE=11 ---
def checkSum(cards):
	sumA1 = 0
	sumA11 = 0
	if cards[-1] == "A":
		sumA1 += 1
		sumA11 += 11
	elif cards[-1] in "JQK":
		sumA1 += 10
		sumA11 += 10
	else:
		sumA1 += int(cards[-1])
		sumA11 += int(cards[-1])
	return [sumA1, sumA11]


# --- ACE VALUE CHOICE ---
def cardsTotalSum(cards):
	if cards[1] < 22:
		return cards[1]
	else:
		return cards[0]


# --- CHECK FOR BLACKJACK ---
def checkEnd():
	if playerTotal == 21:
		print('BlackJack!')
		print()
		if len(dealerCards) < 2:
			dealerHit()
			showCards()
			if dealerTotal == 21:
				print('Dealer too has a Blackjack.')
				print('Push.')
				print()
				addToBalance(1)
				gameStart()
			else:
				print('Blackjack! Player wins.')
				print()
				addToBalance(2.5)
				gameStart()
		else:
			print('Blackjack! Player wins.')
			print()
			addToBalance(2.5)
			gameStart()
	elif dealerTotal == 21:
		print('BlackJack! Dealer wins!')
		print()
		gameStart()
	elif playerTotal > 21:
		print('Bust! Dealer wins.')
		print()
		gameStart()
	elif dealerTotal > 21:
		print('Bust! Player wins!')
		print()
		addToBalance(2)
		gameStart()
	elif playerStand and playerTotal > dealerTotal:
		print('PLayer wins.')
		print()
		addToBalance(2)
		gameStart()
	elif playerStand and dealerTotal > playerTotal:
		print('Dealer wins.')
		print()
		gameStart()


# --- ADD POOL TO BALANCE ---
def addToBalance(n):
	global balance
	balance += betPool*n


# --- SET UP AND RESET ---
def rinse():
	global playerCards
	global dealerCards
	global dealerTotal
	global playerTotal
	global playerSums
	global dealerSums
	global playerStand
	playerCards = []
	dealerCards = []
	playerTotal = 0
	dealerTotal = 0
	playerSums = [0, 0]
	dealerSums = [0, 0]
	playerStand = False


# --- GAME'S FIRST FASE ---
def gameStart():
	rinse()
	deck_shuffle()
	bets()
	dealerHit()
	playerHit()
	playerHit()
	showCards()
	checkEnd()
	choiceLoop()


# --- GAME LOOP ---
playerStand = False
def choiceLoop():
	global playerStand
	choice = 0
	print("1 - Hit")
	print("2 - Stand")
	while True:
		try:
			choice = int(input("Make your choice. (1-2)"))
		except:
			print("Please try again.")
		else:
			print()
			if choice < 1 or choice > 2:
				print("Please try again.")
			elif choice == 1:
				playerHit()
				showCards()
				checkEnd()
			elif choice == 2:
				playerStand = True
				while dealerTotal < 17:
					dealerHit()
					showCards()
					if dealerTotal > 16:
						checkEnd()


# --- CALLS ---
opening()
gameStart()
