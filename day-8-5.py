# Write a Python program to find the length of a given dictionary values.

dict1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'magenta'}
dict2 = {'1': 'Austin Little', '2': 'Natasha Howard',
          '3': 'Alfred Mullins', '4': 'Jamie Rowe'}

print({value:  len(value) for value in dict1.values()})
print({value:  len(value) for value in dict2.values()})
