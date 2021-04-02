names = ["Raj", "Pratik", "Akash", "Suraj", "joy", "Anurag"]
address = ["PRL", "Bankura", "Kol", "Burnpur", "DGP", "ASNL"]

# print(len(address)) # len - Many Elements Exist

# create a list from number 1 - 100
num_list = [1,2,3,4,5,6,7,8,9,10] # 0-9, -1,-10
num_list = list(range(1, 101)) # 0-100, -1, -100 

# print(num_list[-100])

num_list = [1,2,3,4,5,6,7,8,9,10]

#for loop
for i in num_list:
    print(i, end=" ")
    
print()
# while loop
i = 0
while i < len(num_list):
    print(num_list[i], end=" ")
    i += 1
    
first_list = [1, 2, 3, 4, 5]

# Dry - Run
# first_list.append(5)
# first_list.extend([5,6,7,8,9])
# first_list.insert(-1, 100)
# first_list.clear()

#print(f"\n{first_list}")



print()
first_list = [1, 2, 3, 4, 5, 3, 6, 3]
# print(first_list.count(10))
first_list.reverse()
# print(first_list)
# first_list.append(6)
# print(first_list) 
# first_list.pop(3)
# print(first_list)

# first_list.remove(3)
#print(first_list)

# name = ["Raj", "Rk", "Rai"]
# print(name.index("Rahul"))


print(first_list)
first_list.sort()
print(first_list)

lst = [1,2,3]
lst . reverse ()
print(lst)