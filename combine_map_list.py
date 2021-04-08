names = ['Raj', 'Pratik', 'Anurag', 'Joy']

# if instructor name lenght is < 4

inst_list = []
for name in names:
	if len(name) < 4:
		inst_list.append(f"Your instructor is {name}")

print(inst_list)
# Your instructor is Raj
# Your instructor is Pratik
# Your instructor is Joy

inst_list2 = list(map(lambda name: "Your instructor is " + name,
	filter(lambda name: len(name) < 4, names)))
print(inst_list2)


inst_list3 = [f"Your instructor is {name}" for name in names if len(name) < 4]

print(inst_list3)