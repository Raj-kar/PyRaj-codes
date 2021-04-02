# def add(num1, num2):
#     print(num1 + num2)
    
# add(10, 20)
# add(20, 20)
# add(50, 21)

# def greet(name):
#     print(f"Hello {name}, welcome again, Good to see you !")
    
# greet("Raj")
# greet("Akash")

# def sum_of_num(ls):
#     add = 0
#     for i in ls:
#         add += i
#     print(add)
    
# sum_of_num([1, 2, 3, 4, 5])
# sum_of_num([1, 2, 3])
# sum_of_num(list(range(1, 11)))


# Prime number - range 1, 20

# def prime(num):
#     for i in range(2, num):
#         if(num % i == 0):
#             return False
#     return True

# for i in range(10, 21):
#     if prime(i) == True:
#         print(i, end=" ")

# def fun1():
#     print("YESSS")
    
# for i in range(5):
#     fun1()

n1 = 10
n2 = 20

n3 = n1 + n2 # 30
n4 = n3 + n1 # 40
# print(n4)

def add(n1, n2):
    return n1 + n2

n3 = add(10, 20)
n4 = add(n3, 10)
# print(n4)

def returnfunc(name):  # fprmal parameter
    val =  f"Hi {name}"
    if name == "akash":
        return val
    else:
        return "I AM BOSS"

val = returnfunc("raj") # actual para
print(val)

def f1(x):
    print(x + 10 - 2)
    if x == 10:
        print(x)
        if x == 5:
            print(x)
    
num = 10
f1(num)
print(num)
