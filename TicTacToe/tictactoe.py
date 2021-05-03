pos_dict = {"1":" ","2":" ","3":" ","4":" ","5":" ","6":" ","7":" ","8":" ","9":" "}

def board():
	a = pos_dict["1"]
	b = pos_dict["2"]
	c = pos_dict["3"]
	d = pos_dict["4"]
	e = pos_dict["5"]
	f = pos_dict["6"]
	g = pos_dict["7"]
	h = pos_dict["8"]
	i = pos_dict["9"]
	print(f"_{g}_|_{h}_|_{i}_\n_{d}_|_{e}_|_{f}_\n {a} | {b} | {c}")

def next_player():
	global player
	if player == "X":
		player = "O"
	else:
		player = "X"

def check_winner():
	global end
	if (pos_dict["1"] == pos_dict["2"] == pos_dict["3"] == player) or \
	(pos_dict["1"] == pos_dict["5"] == pos_dict["9"] == player) or \
	(pos_dict["1"] == pos_dict["4"] == pos_dict["7"] == player) or \
	(pos_dict["2"] == pos_dict["5"] == pos_dict["8"] == player) or \
	(pos_dict["3"] == pos_dict["5"] == pos_dict["7"] == player) or \
	(pos_dict["3"] == pos_dict["6"] == pos_dict["9"] == player) or \
	(pos_dict["4"] == pos_dict["5"] == pos_dict["6"] == player) or \
	(pos_dict["7"] == pos_dict["8"] == pos_dict["9"] == player):
		end = 1

def check_mode():
	mode = ""
	print("     * JOGO DA VELHA *")
	print("")
	print(" (1 jogador)  (2 jogadores)")
	print("")
	renew_board()
	global end
	end = 0
	mode = input("Escolha o modo de jogo. (1-2)")
	print("")
	if mode == "1":
		#FUNCAO 1P***********
		pass
	elif mode == "2":
		game2p()
	else:
		print("")
		print ("Opção inválida. Escolha 1 ou 2 jogadores.")
		print("")
		check_mode()

def guide():
	print("* Guia de jogo *")
	print("")
	print(f"_7_|_8_|_9_\n_4_|_5_|_6\t\t<-\tEscolha as posições de jogo digitando os\n 1 | 2 | 3\t\t\tnúmeros correspondentes conforme esse modelo.")
	print("")
	input("Digite qualquer tecla para começar.")
	print("")
	
def check_draw():
	global end
	if not " " in pos_dict.values():
		end = 2

def renew_board():
	for i in pos_dict:
		pos_dict[i] = " "

def which_symbol():
	global player
	which = input("Escolha 'X' ou 'O' para o primeiro jogador")
	if which.lower() == "x":
		player = "X"
	elif which.lower() == "o" or which == "0":
		player = "O"
	else:
		print("")
		print("Opção inválida.")
		which_symbol()
		print("")

def choise():
	num_control = "123456789"
	aux = input("Escolha a posição.(1-9)")
	if aux not in num_control or aux == '':
		print("")
		print("Opção inválida.")
		print("")
	else:
		if int(aux) in range(1,10):
			for i in pos_dict:
				if i == aux:
					if pos_dict[i] == " ":
						pos_dict[i] = player
					else:
						print("")
						print ("Ops! Essa posição já está ocupada.")
						print("")
						choise()			
		else:
			print ("Opção inválida.")
			print("")
			choise()

def game2p():
	guide()
	which_symbol()
	while end == 0:
		print("")
		print("Jogador ", player)
		board()
		print("")
		choise()
		check_winner()
		check_draw()
		next_player()
	if end == 1:
		next_player()
		board()
		print(player,"venceu. Parabéns!")
		print("")
		aux = input("Jogar novamente? ( S | N )")
		if aux.lower() == "s":
			check_mode()
		elif aux.lower() == "n":
			print("Até logo!")
		else:
			print("")
			print("Opção inválida.")
			print("")
			check_mode()
	if end == 2:
		board()
		print("")
		print("Empatou.")
		print("")
		aux = input("Jogar novamente? ( S | N )")
		if aux.lower() == "s":
			check_mode()
		elif aux.lower() == "n":
			print("Até logo!")
		else:
			print("")
			print("Opção inválida.")
			print("")
			check_mode()

player = "X"
end = 0

check_mode()