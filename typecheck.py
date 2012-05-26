def displayNumType(num):
	print(num, 'is', end=" ")
	if isinstance(num, (int, float, complex)):
		print('a number of type:', type(num).__name__)
	else:
		print('not a number at all')

displayNumType(123)