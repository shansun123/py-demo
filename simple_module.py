#/usr/bin/env python

"""this is a simple module"""

globalVar = "Hello Module"

class Person(object):
	"""docstring for SimpleClass"""

	def __init__(self, arg):
		super(Person, self).__init__() 
		# check if arg is type of list or tuple 
		if isinstance(arg, (list, tuple)) and len(arg) == 2:
			self.firstName = arg[0]
			self.lastName = arg[1]
		else:
			raise Exception('Illegal args')
	
	def sayHello(self):
		print("Hello,", self.firstName, self.lastName)

def sayGoodBye(name="Lanbo"):
	"""Say good bye to somebody"""
	print("Good bye,", name)

def test():
	per = Person(("Lanbo", "Xu"))
	per.sayHello()
	sayGoodBye()

# main body
if __name__ == '__main__':
	test()