# program to login as admin

ID = int(input("Enter your ID :: "))
password = input("Enter your password :: ")

if ID == 1 and password == "0000":
    print("Welcome Raj")
elif ID == 2 and password == "0011":
    print("Welcome Prarik")
else:
    print("You are noot a valid USER")