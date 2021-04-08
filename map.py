lst = [1, 2, 3, 4]

''' (for) your code

new_lst = []
for i in lst:
	new_lst.append(i * i)

print(new_lst) '''

'''using in-built func map'''

lst = [1, 2, 3, 4]

# def square(num):
# 	return num ** 2
# new_list = list(map(square, lst))

# new_list = list(map(lambda x:x*x, lst))
# print(new_list)


# Expected output -
# [1, 4, 9, 16]


names = [
    {'first':'Rusty', 'last': 'Steele'}, 
    {'first':'Colt', 'last': 'Steele', }, 
    {'first':'Blue', 'last': 'Steele', }
]

first_names = list(map(lambda name: name['first'], names))
print(first_names) # ['Rusty', 'Colt', 'Blue']

first_names = list(map(lambda name: name['first'].upper(), names))
print(first_names) # ['RUSTY', 'COLT', 'BLUE']