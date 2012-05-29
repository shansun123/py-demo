#----------------------NUMBER TYPES-------------------
anInt = 1
aLong = -99999999999999999
aFloat = 3.1415926535
aComplex = 1.23+4.56J

print(anInt, aLong, aFloat, aComplex)

del anInt

# 删除已经删过的对象时，会抛NameError: name 'anInt' is not defined
# del anInt

#----------------------DIVISION---------------------

print(3 / 6)

# 地板除
print(1 // 2)
print(1.0 // 2.0)
print(-1 // 2)

#----------------------CALC-------------------------

print(abs(-1))

print(divmod(10, 3)) # return (3, 1)
	
print(round(3.4999))

import math
for eachNum in range(10):
	print(round(math.pi, eachNum))

print(hex(255)) # 0xff

print(oct(255))	# 0o377

print(ord('a'), chr(97))	# 97 a

print(bool(1), bool('1'), bool(0), bool('0'), bool([]), bool((1,))) # True True False True False True

