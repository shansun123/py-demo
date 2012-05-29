db = {}

def newUser():
	prompt = 'login desired: '

	while True:
		name = input(prompt)
		if name in db:
			prompt = 'name taken, try annother: '
			continue
		else:
			break

	pwd = input('password: ')
	db[name] = pwd

def oldUser():
	name = input('login: ')
	pwd = input('password: ')
	passwd = db.get(name)
	if passwd == pwd:
		print('welcome back', name)
	else:
		print('login incorrect')

def showMenu():
	prompt = """(N)ew User Login
(E)xisting User Login
(Q)uit

Enter choice: """
	
	done = False

	while not done:
		chosen = False

		while not chosen:
			try:
				choice = input(prompt).strip()[0].lower()
			except(EOFError, KeyboardInterrupt):
				choice = 'q'

			print('\nYou picked: [%s]' % choice)

			if choice not in 'neq':
				print('invalid option, try again')
			else:
				chosen = True

		if choice == 'q':
			done = True
		elif choice == 'n':
			newUser()
		elif choice == 'e':
			oldUser()

if __name__ == '__main__':
	showMenu()