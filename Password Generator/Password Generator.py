import string
import random

alphabet_lower = string.ascii_lowercase
alphabet_uppercase = string.ascii_uppercase
special = string.punctuation
numeric = string.digits

print("Password Generator")

complex_type = ''
num_characters = 0

def menu():
	global complex_type
	global num_characters
	validator1 = True
	while validator1:
		print()
		print('1 - Only alphabetic')
		print('2 - Alphabetic and special characters')
		print('3 - Only numeric')
		print('4 - Numeric and special characters')
		print('5 - Alphanumeric')
		print('6 - Alphanumeric with special characters')
		print()
		try:
			complex_type = int(input('Choose the complexity for the Password.'))
		except:
			print("Ops. Please try again.")
		else:
			if complex_type < 1 or complex_type > 6:
				print('Ops. Please choose one of the options. (1 - 6)')
				continue
			else:
				validator1 = False

	validator2 = True
	while validator2:
		try:
			num_characters = int(input('How many digits? (4 to 50)'))
		except:
			print("Ops. Try again please.")
		else:
			if num_characters < 4 or num_characters > 50:
				print("Ops. Please choose between 4 and 50 characters.")
				continue
			else:
				validator2 = False
	generation()

def check_case():
	validator3 = True
	while validator3:
		print()
		print('1 - Yes')
		print('2 - No')
		print()
		try:
			case_sens = int(input('Mix uppercase and lowercase letters?'))
		except:
			print('Ops. Try again please.')
		else:
			if case_sens < 1 or case_sens > 2:
				print('Ops. Please choose 1 or 2.')
				continue
			else:
				validator3 = False
	return case_sens

mixed_elements = ''
def generation():
	global mixed_elements
	if complex_type == 1:
		case_sens = check_case()
		if case_sens == 1:
			alpha_case = alphabet_lower + alphabet_uppercase
			mixed_elements = random.sample(population=alpha_case,k=len(alpha_case))
			show_results()
		else:
			mixed_elements = random.sample(population=alphabet_lower,k=len(alphabet_lower))
			show_results()
	elif complex_type == 2:
		case_sens = check_case()
		if case_sens == 1:
			alpha_casespecial = alphabet_lower + alphabet_uppercase + special
			mixed_elements = random.sample(population=alpha_casespecial,k=len(alpha_casespecial))
			show_results()
		else:
			alpha_ncasespecial = alphabet_lower + special
			mixed_elements = random.sample(population=alpha_ncasespecial,k=len(alpha_ncasespecial))
			show_results()
	elif complex_type == 3:
		mixed_elements = random.sample(population=numeric,k=len(numeric))
		show_results()
	elif complex_type == 4:
		numeric_special = numeric + special
		mixed_elements = random.sample(population=numeric_special,k=len(numeric_special))
		show_results()
	elif complex_type == 5:
		case_sens = check_case()
		if case_sens == 1:
			alpha_casenumeric = alphabet_uppercase + alphabet_lower + numeric
			mixed_elements = random.sample(population=alpha_casenumeric,k=len(alpha_casenumeric))
			show_results()
		else:
			alpha_ncasenumeric = alphabet_lower + numeric
			mixed_elements = random.sample(population=alpha_ncasenumeric,k=len(alpha_ncasenumeric))
			show_results()
	elif complex_type == 6:
		case_sens = check_case()
		if case_sens == 1:
			alphanum_casespecial = alphabet_lower + alphabet_uppercase + numeric + special
			mixed_elements = random.sample(population=alphanum_casespecial,k=len(alphanum_casespecial))
			show_results()
		else:
			alphanum_ncasespecial = alphabet_lower + numeric + special
			mixed_elements = random.sample(population=alphanum_ncasespecial,k=len(alphanum_ncasespecial))
			show_results()

def show_results():
	print()
	print('These are the generated passwords:')
	for i,j in enumerate(range(5),start=1):
		sample = random.choices(population=mixed_elements,k=num_characters)
		pass_created = ''.join(sample)
		print (i, pass_created)
	repeat()

def repeat():
	repeat_on = True
	while repeat_on:
		print()
		print('1 - Generate others')
		print('2 - Start over')
		print('3 - Finish')
		print()
		validator4 = True
		while validator4:
			try:
				choice = int(input('How do you want to proceed?'))
			except:
				print('Ops. Please try again.')
			else:
				if choice == 1:
					validator4 = False
					repeat_on = False
					show_results()
				elif choice == 2:
					validator4 = False
					repeat_on = False
					menu()
				elif choice == 3:
					validator4 = False
					repeat_on = False
					print('See ya.')
				else:
					print('Ops. Please try again.')
					continue

menu()