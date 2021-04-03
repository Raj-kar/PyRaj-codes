# # def sum_odd_numbers(numbers):
# #     """return sum of odd numbers that passed in numbers list."""
# #     total = 0
# #     for num in numbers:
# #         if num % 2 != 0:
# #             total += num
            
# #     return total

# # ans = sum_odd_numbers([1, 2, 3, 4, 5])
# # print(ans) # 9

# # def is_odd_number(num):
# #     if num % 2 != 0:
# #         return True
# #     return False

# # print(is_odd_number(11))
# # print(is_odd_number(10))

# def print_full_name(f_name, l_name):
#     return(f"Your full name is {f_name} {l_name}")


# print(print_full_name("Pratik", "Sen"))


# def add(n1 = 6, n2 = 5):
#     return n1 + n2


# def add(n1=4, n2) wrong -> n1 has a default of 4, but it's useless.
# def add(n1, n2 = 5)
# def add(m1, m2)
# def add(n1 =4, n1 = 5)

# ans = add()
# print(ans)
# ans = add(1)
# print(ans)
# ans = add(1, 1)
# print(ans)

def add(a, b):
    return a+b


def math(a, b, fn=add):
    return add(a, b)


def subtract(a, b):
    return a-b


# print(math(2, 2))  # 4

# print(math(2, 2, subtract))



# def mul(n1, n2):
#     return n1 * n2

# fun = mul
# fun2 = mul
# def fun(n1, n2):
#     return n1 * n2

# print(fun2(5, 5))


def mul(n1, n2):
    return n1 * n2

def div(n1):
    return mul(n1, 10)

def add(n1, n2):
    return div(n2)

def math(n1, n2):
    return add(n1, n2)


print(math(5, 5))
