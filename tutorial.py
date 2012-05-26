#-------------------Hello World---------------------

str = 'Hello %s, By %s' % ('World', 'Lanbo')

print(str)

# Sublime不支持input
#user = input('Enter login name: ')
# print('Your login is: ', user)

#------------------------IO------------------------

import sys

# IN python 2.* 
#sys.stderr, 'Fatal error: invalid input'

# IN python 3.*
print('Fatal error: invalid input', file=sys.stderr)

logfile = open('D:/tmp/py-log.txt', 'w')

# IN python 2.*
# logfile, 'Fatal error: invalid input'
print('Fatal error: invalid input', file=logfile)

logfile.close()

#------------------------FUNC-----------------------

def foo():
	"This is a doc String."
	return True

print("call foo() returns ", foo())

#-------------------------OPERATOR------------------

print(-2 * 4 + 3 * 2)

print(2 < 4 and 2 == 4)

print(2 < 5 or 2 > 5)

print(not 6.2 <= 6)

# 在其他语言中不允许，这里意为 3 < 4 and 4 < 5
print(3 < 4 < 5)

#----------------------VARIABLES------------------

counter = 0
miles = 1000.0
name = 'Bob'
counter = counter + 1
kilometers = 1.609 * miles

print("%f miles is the same as %f km" %(miles, kilometers))

counter *= 10

print(counter)
 
#------------------------STRING---------------------

pystr = 'Python'

iscool = 'is cool!'

print(pystr[0])

print(pystr[2:5])

print(iscool[:2])

print(pystr + ' ' + iscool)

print(pystr * 3)

print('-' * 20)

pystr = '''python
is cool '''

print(pystr)

#----------------LIST-------------------

aList = [1, 2, 3, 4]

print(aList[0])

print(aList[2:])

print(aList[:3])

aList[3] = 5

print(aList[3:])

#------------------TUPLE-------------------

aTuple = ('robots', 77, 93.2, 'try')

print(aTuple)

print(aTuple[:3])

# does not support: read only!
# aTuple[1] = 4
# print(aTuple)

#-----------------DIRECOTRY---------------

aDict = {'host': 'earth'}   

aDict['port'] = 80

print(aDict)

print(aDict.keys())

print(aDict['host'])

for key in aDict:
	print(key, aDict[key])

#-------------------IF-----------------

x = 4

if x > 5:
	print('x larger than 5')
elif x > 3:
	print('x larger than 3')
else:
	print('x less than 3')

#-----------------WHILE----------------

counter = 0
while counter < 3:
	print('loop %d' % (counter))
	counter += 1

#------------------FOR-----------------

for item in ['email', 'net-surfing', 'homework', 'chat']:
	print(item, )

for c in "abc":
	print(c)

#------------------RANGE---------------

for eachNum in range(3):
	print(eachNum)

foo = 'abc'
for i in range(len(foo)):
	print(foo[i], '(%d)' % i)

# python 2.3 推出enumerate，等同于上
for i, ch in enumerate(foo):
	print(ch, '(%d)' % i)

#-------------------LIST-PARSE-----------

# 0到3，数的三次方
squared = [x ** 3 for x in range(4)]
for i in squared:
	print(i)

sqdEvens = [x ** 2 for x in range(8) if not x % 2]
for i in sqdEvens:
	print(i)

#-------------------FILE---------------

aFile = open('D:/tmp/py-log.txt', 'rt')
aFile.seek(10)
aChar = aFile.read(1)
print(aChar)
aFile.close()

with open('D:/tmp/py-log.txt', 'rt') as bFile:
	for aLine in bFile:
		print(aLine)

#---------------EXCEPTION--------------

try:
	cFile = open('D:/tmp/py-log.txt', 'r')
	for eachLine in cFile:
		print(eachLine)
except IOError as e:
	print('file open io error:', e)
else :
	pass
finally:
	print('finally end of try-catch')

#--------------FUNCTION----------------

def addMe2Me(x):
	'apply + operation to argument'
	return x + x

print(addMe2Me(3))
print(addMe2Me('Python'))
print(addMe2Me([-1, 'abc']))

def foo(debug=True):
	if(debug):
		print('is debug')
	else:
		print('is not debug')

foo()
foo(False)

#--------------CLASS--------------------

class FooClass(object):
	"""my very first class: FooClass"""

	version = 0.1 # class (data) attribute

	def __init__(self, nm='Jone Doe'):
		"""constructor"""
		self.name = nm # class instance (data) attribute
		print('Created a class instance for', nm)

	def showName(self):
		"""display instance attribute and class name"""
		print('Your name is ', self.name)
		print('My name is ', self.__class__.__name__)

	def showVersion(self):
		"""display class(static) attribute"""
		print(self.version)

	def addMe2Me(self, x):
		"""apply + operation to argument"""
		return x + x

foo1 = FooClass()
foo1.showName()
foo1.showVersion()
print(foo1.addMe2Me(4))

foo2 = FooClass('Chris Xu')
foo2.showName()
foo2.showVersion()
print(foo2.addMe2Me(10))

help(foo1.addMe2Me)