Checklist

1. desenvolver modo player 1
2. acrescentar informação "player 1" e "player 2" 

Done:

1. Vitoria de X
2. Vitoria de O
3. input de '' na escolha das posições
4. input de letras na escolha das posições
5. input de dois ou mais numeros na escolha das posições


'''
print("* Jogo da velha *")
print("   1  2  3")
print("A __|__|__\nB __|__|__\nC   |  |  ")
escolha = input("Digite a coordenada da posição para iniciar.")

if escolha == "1a" or escolha == "a1" or escolha == "1A" or escolha == "A1":
	print("Você escolheu 1A")
	print("   1  2  3")
	print("A  X|__|__\nB __|__|__\nC   |  |  ")
	print("Eu escolho 3C")
	print("   1  2  3")
	print("A  X|__|__\nB __|__|__\nC   |  |O ")
	
V12 = "__|"
V3 = "__"
V12C = "  |"
V3C = "  "
X1 = "X |"
O1 = "O |"
X2 = "X |"
X3 = "X"
O2 = "O |"
O3 = "O"

escolha = []

def jogada():
	return input("Digite a coordenada da posição.")

print("* Jogo da velha *")
print("   1  2  3")
print("A", V12, V12, V3)
print("B", V12, V12, V3)
print("C", V12C, V12C, V3C)
print("\n")
escolha = jogada()

if escolha == "1a" or escolha == "a1" or escolha == "1A" or escolha == "A1":
	print("Você escolheu",escolha)
	print("   1  2  3")
	print("A", X1, V12, V3)
	print("B", V12, V12, V3)
	print("C", V12C, V12C, V3C)
	print("\n")
	print("Eu escolho 3C")
	print("   1  2  3")
	print("A", X1, V12, V3)
	print("B", V12, V12, V3)
	print("C", V12C, V12C, O3)
	print("\n")
	escolha = jogada()
	if escolha == "2a" or escolha == "a2" or escolha == "2A" or escolha == "A2":
		print("Você escolheu", escolha)
		print("   1  2  3")
		print("A", X1, X2, V3)
		print("B", V12, V12, V3)
		print("C", V12C, V12C, O3)
		print("\n")
		print("Eu escolho 3A")
		print("   1  2  3")
		print("A", X1, X2, O3)
		print("B", V12, V12, V3)
		print("C", V12C, V12C, O3)
		print("\n")
		escolha = jogada()
		if escolha == "3b" or escolha == "b3" or escolha == "3B" or escolha == "B3":
			print("Você escolheu", escolha)
			print("   1  2  3")
			print("A", X1, X2, O3)
			print("B", V12, V12, X3)
			print("C", V12C, V12C, O3)
			print("\n")
			print("Eu escolho 1C")
			print("   1  2  3")
			print("A", X1, X2, O3)
			print("B", V12, V12, X3)
			print("C", O1, V12C, O3)
			print("\n")
			escolha = jogada()
'''