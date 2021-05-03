def cows_bulls(pc_num,player_num):
	results = {'cows':0,'bulls':0}

	aux = []

	for i in pc_num:
		aux.append(i)

	if player_num[0] in aux:
		if player_num[0] == aux[0]:
			aux[0] = 'C'
		elif player_num[0] == aux[1]:
			aux[1] = 'B'
		elif player_num[0] == aux[2]:
			aux[2] = 'B'
		elif player_num[0] == aux[3]:
			aux[3] = 'B'
	
	if player_num[1] in aux:
		if player_num[1] == aux[1]:
			aux[1] = 'C'
		elif player_num[1] == aux[0]:
			aux[0] = 'B'
		elif player_num[1] == aux[2]:
			aux[2] = 'B'
		elif player_num[1] == aux[3]:
			aux[3] = 'B'

	if player_num[2] in aux:
		if player_num[2] == aux[2]:
			aux[2] = 'C'
		elif player_num[2] == aux[0]:
			aux[0] = 'B'
		elif player_num[2] == aux[1]:
			aux[1] = 'B'
		elif player_num[2] == aux[3]:
			aux[3] = 'B'

	if player_num[3] in aux:
		if player_num[3] == aux[3]:
			aux[3] = 'C'
		elif player_num[3] == aux[0]:
			aux[0] = 'B'
		elif player_num[3] == aux[1]:
			aux[1] = 'B'
		elif player_num[3] == aux[3]:
			aux[3] = 'B'

	for i in aux:
		if i == 'C':
			results['cows'] += 1
		elif i == 'B':
			results['bulls'] += 1

	return results