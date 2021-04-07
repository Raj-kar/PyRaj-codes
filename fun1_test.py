nums = [1, 2, 3, 4, 5]

doubles = map(lambda num: num*num, nums)
print(list(doubles))

peoples = ["Raj", "Rahul", "Rai", "Monai", "Babai"]

x = list(map(lambda people:people.upper(), peoples))
print(x)

new = list(filter(lambda name: name[0] == "R", peoples))

print(new)