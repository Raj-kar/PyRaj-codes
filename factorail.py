# factorial -
# 5 - 120 - 1 * 2 * 3 * 4 * 5
# 4 - 24 - 1 * 2 * 3 * 4

#fact = 1
#for i in range(5, 0, -1):
#    fact = fact * i
    
#print(fact)

# Recursion - a function calling itself, called recursion.
# Recursion function always have an end condition.

# Interview - Print 1 to 10 without using loop.

# def print_num(n):
#     if n > 10:
#         return
#     else:
#         print(n, end = " ")
#         print_num(n + 1)
        
# print_num(1)


def fact(n):
	if n == 0:
		return 1
	else:
		return n * fact(n-1)

print(fact(4))


