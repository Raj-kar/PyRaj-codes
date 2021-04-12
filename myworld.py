capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"

def rever_num(num):
	res = 0

	while num != 0:
		rem = num % 10
		res = res * 10 + rem
		num //= 10

	return res