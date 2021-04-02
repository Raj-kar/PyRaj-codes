list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

for name in list1:
    if name == "":
        list1.remove("")
        
print(list1)