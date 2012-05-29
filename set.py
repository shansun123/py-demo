s = set('cheeseshop')
t = frozenset('bookshop')	# read-only

print(type(s), type(t))

print(len(s) == len(t), s == t)

print('k' in s)

for i in s:
	print(i)

s.add('z') # {'c', 'e', 'h', 'o', 'p', 's', 'z'}

print(s) 

s.update('pypi') # {'c', 'e', 'i', 'h', 'o', 'p', 's', 'y', 'z'}

print(s)

s.remove('z')

print(s)

s -= set('pypi')

print(s)

t.add('z') # AttributeError: 'frozenset' object has no attribute 'add'