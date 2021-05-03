def repeat():
	print('1 - Yes')
	print('2 - No')
	while True:
		try:
			choice = int(input('Play again?'))
		except:
			print('Ops. Please try again.')
		else:
			if choice == 1:
				break
				game()
			elif choice == 2:
				print('See ya.')
				break
			else:
				print('Ops. Please try again.')
