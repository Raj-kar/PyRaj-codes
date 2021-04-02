# tuples and set
numbers = (1, 2, 3)
# print(numbers[1])
# numbers[0] = 121
# print(numbers)

first_tuple = (1, 2, 3, 3, 3)

print(first_tuple[1])  # 2
print(first_tuple[2])  # 3
print(first_tuple[-1])  # 3

second_tuple = tuple([5, 1, 2])

second_tuple[0] # 5
second_tuple[-1] # 2

name = ("raj", "pratik", "joy")
#for i in name:
 #   print(i.title())
 
print(name.index("joy"))




#Type your answer here.
dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict2 = { key : dict1[key] for key in dict1 if dict1[key]>2000}


print(dict2)