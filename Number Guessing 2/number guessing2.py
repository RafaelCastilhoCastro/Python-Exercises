print('Welcome to Number Guess Game 2!')
print('Try and guess the 3 digit number.')

import random

numbers = random.choices(population=range(0,9),k=3)

game_on = True

while game_on:
	answer = input('Whats your guess?')
	if int(answer[0]) == numbers[0] and int(answer[1]) == numbers[1] and int(answer[2]) == numbers[2]:
		print('Jackpot! You guessed!')
		break

	counter = 0
	for i in range(3):
		if int(answer[i]) == numbers[i]:
			print('Match')
			counter +=1
		elif int(answer[i]) in numbers:
			print('Close')
			counter +=1

	if counter == 0:
		print('Nope')
