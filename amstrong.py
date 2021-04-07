# Amstrong

# 153 -  3^3 + 5^3 + 1^3 = 27 + 125 + 1 = 153
# 121 -  1^3 + 2^3 + 1^3 = 10
# 1634 - 1^4 + 6^4 + 3^4 + 4^4 = 1634

# 1 - find how many digit 
# def getDigit(num):
# 	count = 0
# 	while num > 0:
# 		num //= 10
# 		count += 1
# 	return count

# 2 - get value after multiply by power
# def getValue(num, power):
# 	return num ** power

# 3 - sum all the digit after geting power
def isAms(num):
	_sum = 0
	power = len(str(num))
	temp = num
	while num != 0:
		_sum += (num % 10) ** power
		num //= 10

	return _sum == temp

print(isAms(153))
print(isAms(123))
print(isAms(1634))