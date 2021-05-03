import random
import cows_bulls_check
import cows_bulls_repeat

def game():
	rand_num = random.choices(population=range(10),k=4)
	pc_num = [str(int) for int in rand_num]

	game_on = True
	attempts = 0
	while game_on:
		print()
		validator1 = True
		while validator1:
			player_num = input("Guess a 4-digit number.")
			if player_num.isdigit() and len(player_num) == 4:
				validator1 = False
				player_num = list(player_num)
			else: 
				print('Please inform a 4-digit number.')

		if pc_num == player_num:
			print('Jackpot! You won!')
			game_on = False
			attempts += 1
			print('Attempts: ',attempts)
			cows_bulls_repeat.repeat()
		else:
			results = cows_bulls_check.cows_bulls(pc_num,player_num)
			attempts += 1
			print()
			print('Cows: ',results['cows'])
			print('Bulls: ',results['bulls'])
			print('Attempts: ',attempts)

game()

#Sair?