stack = []

def pushit():
	stack.append(input('Enter New String:').strip())

def popit():
	print('Removed [', stack.pop(), ']')

def view():
	print(stack)

CMDs = {'u':pushit, 'o':popit, 'v':view}

def showMenu():
	pr = """
p(U)sh
p(O)p
(V)iew
(Q)uit

Enter choice: """

	while True:
		while True:
			try:
				choice = input(pr).strip()[0].lower()
			except(EOFError, KeyboardInterrupt, IndexError):
				choice = 'q'

			print('\nYou picked: [%s]' % choice)

			if not choice in 'uovq':
				print('Invalid option, try again')
			else:
				break

		if choice == 'q':
			break

		CMDs[choice]()

if __name__ == '__main__':
	showMenu()