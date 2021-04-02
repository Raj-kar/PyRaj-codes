# Dict

instructor = ["Colt", True, 4, "Python", False] #list

instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}

# print(instructor['num_courses'])
instructor['num_courses'] = instructor['num_courses'] + 1
# print(instructor['num_courses'])

new_ins = {}
new_ins.update(instructor)
# print(new_ins)

temp = {}.fromkeys(["fav_language"],"python") # {'a': [1, 2, 3, 4, 5]}
# print(temp)

# print(instructor.get("class"))
# print("now do this.....")

# instructor.pop('owns_dog')
instructor.popitem()
# print(instructor.items())


pratik_data = {
    "name" : "Pratik",
    "dept": "CSE",
    "Roll": 12,
    "marks": 9.5,
    "Sem" : "2nd sem",
    "Address": "PRL",
    "favourite_lang" : "Python",
    "favourite_books" : ["book1", "book2", "book3", "post4"],
    "ipl_team": {
        "name": "CSK",
        "captain" : "Dhoni",
        "jercy_color": "yellow"
    }
}

# print(pratik_data["name"], pratik_data["marks"])
# print(pratik_data["favourite_books"][3])


# dict comprehension

data  = {
    "name" : "Raj",
    "address" : "PRL"
    }

for key, value in data.items():
   #print(key, value)
   pass
    
for key in data.values():
    #print(key)
    pass

# {print(key, end=" "):print(value) for key, value in data.items()}

# {print(key) for key in data.keys()}
# {print(values) for values in data.values()}

numbers = dict(first=10, second=20, third=30)

square_dict = {}
for key, value in numbers.items():
    square_dict[key] = value * value * value

# dict compre
squared_numbers = {key: value ** 3 for key, value in numbers.items()}

# print(squared_numbers)  # {'first': 1, 'second': 4, 'third': 9}

# print(square_dict)

# print({num: num**2 for num in [1, 2, 3, 4, 5]})

# sq_dict = {}
# for num in [1, 2, 3, 4, 5]:
#     sq_dict[num] =  num**2
    
# print(sq_dict)

# str1 = "ABC"
# str2 = "123"
# combo = {str1[i]: str2[i] for i in range(0, len(str1))}
# print(combo)  # {'A': '1', 'B': '2', 'C': '3'}

# for i in range(0, 3):
#     print(str1[i], str2[i])
    
    
'''conditions with dict com'''
num_list = [1, 2, 3, 4]

# print({num: ("even" if num % 2 == 0 else "odd") for num in num_list})

# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}
# homework
# {'odd': 1, 'even': 2, 'odd': 3}

ex = {}
for num in range(1, 11):
    if(num % 2 == 0):
        ex[num] = "even"
    else:
        ex[num] = "odd"
        
# print(ex)

# str1 = "My Name is Raj"

# ans = {
#     "M": "cons",
#     "y": "cons",
#     "N": "cons",
#     "a": "vowel",
# }

