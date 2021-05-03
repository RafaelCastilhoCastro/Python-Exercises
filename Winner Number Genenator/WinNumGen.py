print('WINNER NUMBERS GENERATOR')

nums = int(input('Generate how many numbers?'))
minNum = int(input("What should be the minimum number?"))
maxNum = int(input("What should be the maximum number?"))

import random

while True:
	x = random.sample(population=range(minNum,maxNum+1),k=nums)
	print(x)
	answer = input('Create more? (y|n)')
	if answer == 'y':
		continue
	else:
		print("See ya.")
		break

