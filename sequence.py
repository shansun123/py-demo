#--------------------OPERATORS-------------------

aList = [1, 3, 'Hello', 23.3, (23, 12)]
print(aList[2])
print(aList[1:3])
print(aList * 2)
print(aList + [1, 2, 3])
print(3 in aList)
print(12 not in aList)

aStr = 'abcdefg'
print(aStr[::-1]) # 可是做我为翻转
print(aStr[::2])  # 隔一个取一个，aceg

for i in range(-1, -len(aStr), -1):
	print(aStr[:i])

# 加上None后，就从展示完整列表
for i in [None] + list(range(-1, -len(aStr), -1)):
	print(aStr[:i])

print("MAX:", max(aStr))

print("SUM:", sum([1, 2, 3, 4, 5]))

print("ZIP:", dict(zip(('x', 'y'), (1, 2))))

#----------------STRINGS--------------------

import string

print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)

# do not used like this
string.digits = 'sffdgf'
print(string.digits)

s = ' '.join(('Hello', 'world', 'By', 'Lanbo'))
print(s)

print(s.lower(), '\r\n', s.upper())

# Python允许如下拼接字符串：编译时字符串连接
print('http://'
	'baidu.com'
	':8080'
	'/index.html')

#----------------------TEMPLATE----------------------------

from string import Template

s = Template('There are ${howmany} ${lang} Quatation Symbols.')
print(s.substitute(lang='Python', howmany=3))

# print(s.substitute(lang='Python')) # KeyError: 'howmany'

print(s.safe_substitute(lang='Python'))

#---------------------FUNCTION OF STRINGS-------------------

quest = 'what is your favorite color?'
print(quest.capitalize())
print(quest.center(40))
print(':'.join(quest.split()))
print(quest.upper())

#----------------------------LIST-----------------------------

aList = [1, 2, 3, 'Hello', [12, 34, 56], (1, 3, 5), {32:'', 2:'fs'}]

print(aList)

del aList[4]

print(aList)

aList.remove(1)

print(aList)

del aList

#---------------------------------------------------------------

