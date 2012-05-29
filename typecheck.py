def displayNumType(num):
	print(num, 'is', end=" ")
	if isinstance(num, (int, float, complex)):
		print('a number of type:', type(num).__name__)
	else:
		print('not a number at all')

displayNumType(123)
 
print(456.0, 'is', end=" ")
if type(456.0) is int:
	print('a int number')
else:
	print('not a int number')