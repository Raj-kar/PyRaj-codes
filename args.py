# def add(n1, n2, n3=0, n4=0):
# 	return n1 + n2 + n3 + n4

# print(add(1, 1, 2, 2))

# *args

def add(*args):
	res = 0
	for i in (args):
		res += i
	return res

print(add(1, 2, 2, 3, 8, 9))
