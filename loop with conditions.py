''' passcode = True
while passcode:
    val = input("tell me something  ")
    if val == "stop":
        passcode = False
    print(val) '''

# break
# if a number divided with 5 and 3, then exit the loop - range(1,20)


    
# if a number divided with 3, then skip the number - range(1,20)
# 1 2 4 5 6 7 8 10 11 13 14 16 17 18 19 20
for i in range(1, 21):
    if(i % 3 == 0):
        continue
    else:
        print(i, end=" ")

