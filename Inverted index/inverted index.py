# Importar arquivos de texto
from Packages import prime_intro
from Packages import prime1
from Packages import prime2
from Packages import prime3

# Conjunto de stop word e pontuações a serem removidas dos textos
import string
stop_words = ["their","has","had","have","as","such","also","the","is","isn't","are","aren't","of","to","for","from","whom","whose","re","not","no","were","weren't","was","wasn't","will","won't","which","with","without","at","At","in","In","on","On","this","This","these","These","those","Those","that","That","his","His","her","Her","a","an","he","He","she","She","it","It","or","our","may","and","pp","by"]
punctuation = set(string.punctuation)
punctuation.add("’")
punctuation.add("…")

# Palavras do texto prime_intro.py - Removidas pontuações, stop words e com as palavras separadas em uma lista
p_intro_raw = prime_intro.prime_intro.replace("–"," ")
p_intro_raw = p_intro_raw.replace("-"," ")
p_intro_raw = "".join(i for i in p_intro_raw if i not in punctuation)
p_intro_raw = p_intro_raw.split()
intro_words = []
for i in p_intro_raw:
	if i.lower() not in stop_words:
		intro_words.append(i.lower())

# Criado default dict para armazenar a lista invertida do arquivo prime_intro
from collections import defaultdict
inv_ind_intro = defaultdict(list)

# Povoar a lista invertida do texto prime_intro
for i in intro_words:
	if i not in inv_ind_intro.keys():
		inv_ind_intro[i].append(["Intro",1])
	else:
		inv_ind_intro[i][0][1]+=1

# Palavras do texto prime1.py - Removidas pontuações, stop words e com as palavras separadas em uma lista
prime1_raw = prime1.prime1.replace("–"," ")
prime1_raw = prime1_raw.replace("-"," ")
prime1_raw = "".join(i for i in prime1_raw if i not in punctuation)
prime1_raw = prime1_raw.split()
prime1_words = []
for i in prime1_raw:
	if i.lower() not in stop_words:
		prime1_words.append(i.lower())

# Criado default dict para armazenar a lista invertida do arquivo prime1
inv_ind_prime1 = defaultdict(list)

# Povoar a lista invertida do texto prime1
for i in prime1_words:
	if i not in inv_ind_prime1.keys():
		inv_ind_prime1[i].append(["Pg 1",1])
	else:
		inv_ind_prime1[i][0][1]+=1

# Criado um dict que irá conter as listas invertidas unidas. Inserido nela o contendo da lista do prime_intro
import copy
merged_ind = copy.deepcopy(inv_ind_intro)

# Acrescentado o conteúdo da lista do prime1. Caso já exista a chave, acrescenta-se a ela o novo valor.
for k,v in inv_ind_prime1.items():
	if k in merged_ind:
		merged_ind[k].append(v)
		aux = merged_ind[k][0]					# Remove a camada de lista		#
		merged_ind[k][0] = merged_ind[k][-1]	# extra que é colateralmente	#
		merged_ind[k][-1] = aux					# criada na introdução			#
		merged_ind[k][0] = merged_ind[k][0][0]	# da nova lista 				#
	else:
		merged_ind[k] = v

# Palavras do texto prime2 - Removidas pontuações, stop words e com as palavras separadas em uma lista
prime2_raw = prime2.prime2.replace("–"," ")
prime2_raw = prime2_raw.replace("-"," ")
prime2_raw = "".join(i for i in prime2_raw if i not in punctuation)
prime2_raw = prime2_raw.split()
prime2_words = []
for i in prime2_raw:
	if i.lower() not in stop_words:
		prime2_words.append(i.lower())

# Criado default dict para armazenar a lista invertida do arquivo prime2
inv_ind_prime2 = defaultdict(list)

# Povoar a lista invertida do texto prime2
for i in prime2_words:
	if i not in inv_ind_prime2.keys():
		inv_ind_prime2[i].append(["Pg 2",1])
	else:
		inv_ind_prime2[i][0][1]+=1

# Acrescentado o conteúdo da lista do prime2. Caso já exista a chave, acrescenta-se a ela o novo valor.
for k,v in inv_ind_prime2.items():
	if k in merged_ind:
		merged_ind[k].append(v)
		aux = merged_ind[k][0]					# Remove a camada de lista		#
		merged_ind[k][0] = merged_ind[k][-1]	# extra que é colateralmente	#
		merged_ind[k][-1] = aux					# criada na introdução			#
		merged_ind[k][0] = merged_ind[k][0][0]	# da nova lista					#
	else:
		merged_ind[k] = v

# Palavras do texto prime3 - Removidas pontuações, stop words e com as palavras separadas em uma lista
prime3_raw = prime3.prime3.replace("–"," ")
prime3_raw = prime3_raw.replace("-"," ")
prime3_raw = "".join(i for i in prime3_raw if i not in punctuation)
prime3_raw = prime3_raw.split()
prime3_words = []
for i in prime3_raw:
	if i.lower() not in stop_words:
		prime3_words.append(i.lower())

# Criado default dict para armazenar a lista invertida do arquivo prime3
inv_ind_prime3 = defaultdict(list)

# Povoar a lista invertida do texto prime3
for i in prime3_words:
	if i not in inv_ind_prime3.keys():
		inv_ind_prime3[i].append(["Pg 3",1])
	else:
		inv_ind_prime3[i][0][1]+=1

# Acrescentado o conteúdo da lista do prime3. Caso já exista a chave, acrescenta-se a ela o novo valor.
for k,v in inv_ind_prime3.items():
	if k in merged_ind:
		merged_ind[k].append(v)
		aux = merged_ind[k][0]					# Remove a camada de lista		#
		merged_ind[k][0] = merged_ind[k][-1]	# extra que é colateralmente	#
		merged_ind[k][-1] = aux					# criada na introdução			#
		merged_ind[k][0] = merged_ind[k][0][0]	# da nova lista					#
	else:
		merged_ind[k] = v

#for k,v in inv_ind_intro.items():
#for k,v in inv_ind_prime1.items():
#for k,v in inv_ind_prime2.items():
#for k,v in inv_ind_prime3.items():
#for k,v in merged_ind.items():
#	print (k,v)


def search():
	word = input("Qual palavra deseja buscar?")
	if word.lower() in merged_ind:
		print("Termo localizado.")
		print("Termo buscado: ",word)
		aux = merged_ind[word]
		for k,v in aux:
			print("Local: ",k)
			print("Ocorrências: ",v)
	else:
		print("Termo não localizado.")

search()