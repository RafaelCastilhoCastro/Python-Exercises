pc_guess = 50

print('WELCOME TO GUESSING GAME')
print()
print("I'll try and guess the number you're thinking.")
print()
print('Pick a number between 0 and 100.')
print()
input('Press any key to continue')
print()

min_max = [0,100]
pc_guess = 50
game_on = True

def guess():
	global min_max
	global pc_guess
	global game_on
	print('Is it',pc_guess,'?')
	print('1 - Higher')
	print('2 - Lower')
	print("3 - That's my number!")
	user_tip = int(input())
	while True:
		if user_tip == 1:
			min_max[0] = pc_guess+1
			break
		elif user_tip == 2:
			min_max[1] = pc_guess-1
			break
		elif user_tip == 3:
			print('Jackpot!')
			game_on = False
			break
		else:
			print('Ops. Please choose 1, 2 or 3.')
	pc_guess = int( (abs(min_max[1]-min_max[0])/2)+min_max[0])


while game_on:
	guess()


# play again function
# exit