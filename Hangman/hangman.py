import random

word = ''
tip = ''
board = []
hang_counter = 1

def get_word():
	global word
	global tip
	with open('words.txt','r') as f:
		x = random.choice(f.readlines())
		x = x.split()
	word = x[0]
	tip = x[1]

def draw_noose():
	print()
	print('  |')
	print('  @')
	print(' / \\')
	print(' \\_/')
	print()

def man():
	global hang_counter
	if hang_counter == 1:
		print()
		print()
		print('_/')
		hang_counter +=1
	elif hang_counter == 2:
		print()
		print()
		print('_/ \\_')
		hang_counter +=1
	elif hang_counter == 3:
		print()
		print('  |')
		print('_/ \\_')
		hang_counter +=1
	elif hang_counter == 4:
		print()
		print(' /|')
		print('_/ \\_')
		hang_counter +=1
	elif hang_counter == 5:
		print()
		print(' /|\\')
		print('_/ \\_')
		hang_counter +=1
	elif hang_counter == 6:
		print(' (++)  _ Hanged!')
		print(' /|\\')
		print('_/ \\_')
		game_on = False

def initial_board(word1):
	global board
	for letter in word1:
		board.append('_')
	print(board)

def final_board(word1):
	global board
	board = []
	for letter in word1:
		board.append(letter)
	print(board)

print('WELCOME TO HANGMAN!')
get_word()
draw_noose()
initial_board(word)
print()

print(word)
print("Here's your tip:",tip)
print()

game_on = True
match_counter = 0

while game_on:

	choice = input('Pick a letter or try and guess the word.')
	if choice.upper() == word:
		print()
		print('Jackpot!')
		final_board(word)
		game_on = False
	elif choice.upper() in word:
		for i in range(len(word)):
			if choice.upper() == word[i]:
				board[i] = choice.upper()
				
				print("You got it!")
				print()
				draw_noose()
				print(board)
				print("Here's your tip:",tip)
	else:
		print("Nope. No cookie.")
		draw_noose()
		man()
		print(board)
		print("Here's your tip:",tip)
		
		


# repeated wrong letter
# same right letter on word
# finish game when complete word