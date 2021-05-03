model1 = ' ---'
model2 = '|   |'
model3 = '   |'

def draw_board(columns,lines):
	
	print(model1*columns)
	print(model2+model3*(columns-1))
	print(model1*columns)

	for i in range(lines-1):
		print(model2+model3*(columns-1))
		print(model1*columns)


draw_board(5,5)