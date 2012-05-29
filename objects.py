#-----------------TYPED-OBJECT-----------------------

print(type(43), type(type(43)), type(None), type([]), type(()), type({}))

# slice object
fooStr = 'abcde'
print(fooStr[::-1], fooStr[::-2])

import simple_module
print(type(simple_module.Person))
p = simple_module.Person
print(type(p))

# 数字和字符串类型值不可以变
x = 'Hello World'
print(id(x))
x = 'Hello Lanbo'
print(id(x))

#-------------------IS--IS NOT-----------------------

a = 4.3
b = 3.3 + 1.0
print(a is not b)

c = a
print(c is a)

print(id(c) == id(a))

#--------------------BUILD-IN METHODS-----------------

# not available in Python 3
# print(cmp(12, 34))

print(str(c))

print(repr([0, 1, 2, 3, 4]))

eval("print('Hello Wordl!')")

