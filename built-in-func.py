# # names = ["Raj", "Pratik", "Joy", "Akash", "Suraj", "Prasenjit"]	

# # print(sorted(names, key=lambda n: len(n))) 
# # print(min(names, key=lambda n: len(n))) #


# # ABS
# # print(abs(-5)) # 5
# # print(abs(5)) # 5

# # amount = int(input("How much money you want to deposit : "))

# # if 0 > amount:
# # 	amount = abs(amount)  # amount*-1

# # print(amount)

# #sum

# # print(sum([1, 2, 3, 4, 5], -10))

# # Round up

# # 5 >= previous num + 1
# # 5 < same

# # num = 4.51926171

# # print(round(num, 1))

# # Zip 

# first_zip = zip([1,2,3], [4,5,6])
# print(list(first_zip))

# first_zip = zip([1,2,3], [4,5,6])
# print(dict(first_zip))


# five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

# print(list(zip(*five_by_two)))

# [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]


# import pyfiglet
# from termcolor import colored, cprint
# from random import choice
# from time import sleep
# from string import ascii_letters

# ava_colors = ("red", "blue", "green", "yellow", "blue", "magenta", "cyan")
# arr = "HOW ARE YOU ??"

# for i in range(len(arr)):
# 	text = pyfiglet.figlet_format(arr[i])
# 	cprint(colored(text, choice(ava_colors)))       # print ascii_art with color
# 	sleep(1)



# lst = [1, 2, 44, 452, 4, 41, -1, 37, 55, 129, -987] 
# print(max(lst), min(lst))

list1 = [1, 5, 33, 4, 88, 178, 0, 76, 11, 35]
res = count = 0
for i in list1:
	if i % 2 == 0:
		res += i
		count += 1

print(res / count) 