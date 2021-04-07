def reverseNum(num):
	res = 0
	while num > 0:
		res = res * 10 + (num % 10)
		num //= 10
	return res

def isPalin(num):
	return num == reverseNum(num)

def getNum(start, stop):
	for i in range(start, stop + 1):
		if isPalin(i):
			print(i, end=" ")

def takeInput():
	start = int(input())
	stop = int(input())

	getNum(start, stop)

takeInput()
