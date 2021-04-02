list1 = [5, 20, 15, 20, 25, 50, 20, 15]

number = list1.count(20) # 3
for i in range(number):
    list1.remove(20)

print(list1)