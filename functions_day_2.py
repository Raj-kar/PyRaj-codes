# def add(a, b):
#     return a+b


# def math(a, b, fn=add):
#     return fn(a, b)


# def subtract(a, b):
#     return a-b


# # print(math(4, 1, subtract))


# def func(n1=1, n2=2, n3=3):
#     return n1 + n2 + n3


# print(func(5, 5, 5))

''' SCOPE OF A VAR '''
# name = "Raj" # global scope (global variable)

# def greet():
#     return f"Welcome sir {name}"


# # print(greet())
# print(name)

# def greet():
#     name = 'Raj' # local scope

#     if 10 > 11:
#         if 8 > 6:
#             if 3 > 4:
#                 name = 'pratik'
#             else:
#                 name = 'joy'
#         else:
#             name = 'Raj'
#     else:
#         name = "anurag"

#     return f"Welcome sir {name}"

# print(greet())
# def say_hello():
#     instructor = 'Colt' #scope, only in function
#     return f'Hello {instructor}'


# print(say_hello())

# print(instructor)  # NameError

# total = 0

# def increment():
#     global total    # global var declare
#     total += 1
#     return total
# print(increment()) # Error!

# gear = 0
# def car_gear():
#     global gear
#     gear += 5
#     return gear

# print(car_gear())
# print(car_gear())
# print(car_gear())
# print(car_gear())


# def outer():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner()

# print(outer())


# def math(n1, n2):
#     def add():
#         return n1 + n2
#     return add()

# print(math(5, 5))

# def f1():
#     def f2():
#         def f3():
#             return 5
#         return f3()
#     return f2()

# print(f1())

# def math(n1, n2, op):
#     if op == "+":
#         def add():
#             return n1 + n2
#         return add()
#     if op == "-":
#         def sub():
#             return n1 - n2
#         return sub()
#     if op == "*":
#         def mul():
#             return n1 * n2
#         return mul()
#     if op == "/":
#         def div():
#             return n1 // n2
#         return div()
#     else:
#         return "Invalid Operator"

# print(math(1, 2, "+"))
# print(math(1, 2, "-"))
# print(math(5, 2, "*"))
# print(math(10, 2, "/"))
# print(math(1, 2, "@"))

# keyword arg

# def details(name, password, email, add):
#     return f"SAVED SUCCSSFULL !! {name}={email}={add}={password}"


# # print(details("Raj","rk@gmail.com","1212", "PRL")) # wrong
# print(details(name="Raj", email="rk@gmail.com", password="1212", add="PRL"))


# # default para vs keyword arg

# def add(n=0 , n2=0):
#     """return sum of two number. if no values passes, then return zero."""
#     return n + n2

# print(add(4, 5))


# Functions types -> " 4 types of function. "
# >> No argument no return
# >> No argument with return
# >> With argumant no return
# >> With argumant with return

# >> No argument no return
def hello(): #parameter
    print("hello")
    
hello() # argg

# >> No argument with return
def hello():
    return "hello"

print(hello())

# >> With argumant no return
def add(n1, n2):
    print(n1 + n2)

add(5, 6) # argument

# >> With argumant with return
def add(n1, n2):
    return n1 + n2

print(add(5, 6))
