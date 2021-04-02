# Print numbers 1 through 7 - Loop
# when we have to do certain work on a repetative basis, we uses loop.

# 1 = lower limit
# 8 - upper limit - 1
# range - one type of iterator [1,2,3,4]

# 4 = lower limit
# 0 = upper limit + 1
# 4 - 1
# 2 = steps

# -1 0 1 2 3 4 5 6 7 

for i in range(-1, 9, 3): # 1 4 7
    #print(i, end=" ")
    pass

# 10 9 8 7 6 5 4 3 2 1
for i in range(10, 0, -2):
    pass
    # print(i, end=" ")
    
# name = input("Enter your name")

'''for i in "suraj":
    if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        print(f"VOWWEL {i}")'''

# for - while ->
# if we know the number of iteration then we used *for* otherwise *while*

for i in range(2, 20, 2):
    pass
    #print(i, end = " ")

count = 2
while count <= 20:
    if(count % 2 == 0):
        print(count, end=" ")
    count = count + 1
    
    
