model1 = ' ---'
model2 = '|   |'
model3 = '   |'

def draw_board(columns,lines):

	print(model1*columns)

	for i in range(lines):
		print(model2+model3*(columns-1))
		print(model1*columns)


nColumns = int(input("How many columns?"))
nLines = int(input("How many lines?"))

draw_board(nColumns, nLines)
