# SETS in python 

l1 = [1, 2, 1, 2]
t1 = (1, 2, 1, 2, 1)
s1 = {1, 2, 1, 2, 1, 5, 6, 7, 7, 7, 7, 7}
s = set({1, 2, 3, 4, 5, 5, 5})

# print(11 in s) 

# for each in s:
#     print(each, end=" ")

# print(l1)
# print(t1)
# print(s1)

str1 = 'thisismynameisraj.iamacoder'  # thismynaerj.cod #.jeamihdytrscno

'''
using list 
l1 = []
for letter in str1:
    if letter not in l1:
        l1.append(letter)

print(''.join(l1)) '''

# print(''.join(set(str1)))

s1 = {1, 2, 3, 4}
print(s1)
s1.add(10)
print(s1)
s1.add(3)
print(s1)
s1.remove(3)
s1.discard(3)
print(s1)

s2 = s1.copy()
print(s2)

s1 = {1, 2, 4}
s2 = {2, 5, 6, 4}

s3 = s1.union(s2)
print(s3)

s1 = {x*x for x in range(1, 10)}
print(s1)

s1 = {letter for letter in "mynameisrajkar"}
print(s1)