# neno number -
# what is a neon number ? - 9 is a neon number
# why ? - factors of 9, are added to 9.

# 9 * 5 = 4+5 = 9
# 9 * 3 = 2+7 = 9
# 9 * 7 = 6+3 = 9

num = int(input("Enter a num :: "))
temp = num * 3
_sum = 0

while temp > 0:
    rem = temp % 10
    _sum += rem
    temp = temp // 10
    
if _sum == num:
    print("neon")
else:
    print("not neon")
