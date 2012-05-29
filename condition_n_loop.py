#--------------------------------------------------------------

x, y = 4, 3

smaller = x if x < y else y	# 三元操作符 X if C else Y

print(smaller)

#--------------------------------------------------------------

def showMaxFactor(num):
	count = int(num / 2)
	while count > 1:
		if num % count == 0:
			print('largest factor of %d is %d' % (num, count))
			break;
		count -= 1
	else:
		print(num, 'is prime')

for eachNum in range(10, 21):
	showMaxFactor(eachNum)

#---------------------------------------------------------------

# 列表解析
seq = [11, 10, 9, 9, 10, 10, 9, 8, 23, 9, 7, 18, 12, 11, 12]
print([x for x in seq if x % 2])

#---------------------------------------------------------------

print([(x + 1, y + 1) for x in range(3) for y in range(5)]) # 生成器

#---------------------------------------------------------------

rows = [1, 2, 3, 17]

def cols():
	yield 56
	yield 1
	yield 2

x_product_pairs = ((i, j) for i in rows for j in cols())

print(list(x_product_pairs)