import random

game_on = True

def new_round():
	global game_on
	answer = ''
	while answer != 'nao':
		answer = input('Jogar novamente? (Sim ou Nao)')
		if answer.lower() == 'nao' or answer.lower() == 'n':
			game_on = False
			print()
			print('Então tá então.')
			break
		elif answer.lower() == 'sim' or answer.lower() == 's':
			break
		else:
			print('Ops. Opção inválida.')

while game_on:
	adversary = random.sample(population=['rock','paper','scissors'],k=1)
	choice = input("Rock, paper or scissors?")
	
	if (choice.lower() == 'rock' and adversary[0] == 'scissors') or (
		choice.lower() == 'paper' and adversary[0] == 'rock') or (
		choice.lower() == 'scissors' and adversary[0] == 'paper'):
		print('Adversário: ',adversary[0])
		print('Jogador: ',choice)
		print()
		print('Máh ôe. Ganhou!!')
		print()
		new_round()

	elif (choice.lower() == 'rock' and adversary[0] == 'paper') or (
		choice.lower() == 'paper' and adversary[0] == 'scissors') or (
		choice.lower() == 'scissors' and adversary[0] == 'rock'):
		print('Adversário: ',adversary[0])
		print('Jogador: ',choice)
		print()
		print('Nope. Passa amanhã.')
		print()
		new_round()
	else:
		print('Adversário: ',adversary[0])
		print('Jogador: ',choice)
		print()
		print('Empatou.')
		print()
		new_round()

