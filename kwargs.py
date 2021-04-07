# def greet(dict1):
# 	print(f"hey {dict1['name']}")

# greet({"name":"Pratik"})

def call(**kwargs):
	for key, value in kwargs.items():
		print(f"{key} is {value}")

call(name="Raj", roll=121, sec= "a", dept= "CSE")

# Scable code - Robust Code
def favorite_colors(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}'s favorite color is {value}")

favorite_colors(rusty='green', colt='blue', raj='black', pratik='purple')


# def func(n1, n2, n3, *args, name="raj", roll=0, id="E001", **kwargs)

# def display_info(a, b, *args, instructor="Colt", **kwargs):
#   return [a, b, args, instructor, kwargs]

# print(display_info(1, 2, 3, 4, last_name="Steele", job="Instructor"))

# [1, 2, (3,), 'Colt', {'last_name': 'Steele', 'job': 'Instructor'}]
# [1, 2, (3, 4), 'Colt', {'last_name': 'Steele', 'job': 'Instructor'}]
# (3, )

# Unpack

def add(lst):
	print(*lst)

add([1,2,3,4,5])