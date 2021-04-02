color ="['Red', 'Green', 'White']"

color = color.replace("[", "")
color = color.replace("]", "")

new_list = []
for i in color.split(","):
    new_list.append(i.replace("'", ""))
    
# print(new_list)

lst = "xxxxxxxxxx"
lst = lst.replace("x", "1", 3)
print(lst)