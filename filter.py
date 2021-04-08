lst = [1, 2, 3, 4, 5, 6, 7, 8]

''' even_lst = []
odd_lst = []
for i in lst:
	if i % 2 == 0:
		even_lst.append(i)
	else:
		odd_lst.append(i)

print(odd_lst)
print(even_lst) '''

odd_list = list(filter(lambda x: x % 2 != 0, lst))
even_list = list(filter(lambda x: x % 2 == 0, lst))
print(odd_list)
print(even_list)
