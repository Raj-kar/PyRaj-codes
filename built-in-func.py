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

first_zip = zip([1,2,3], [4,5,6])
print(list(first_zip))

first_zip = zip([1,2,3], [4,5,6])
print(dict(first_zip))


five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

print(list(zip(*five_by_two)))

[(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]
