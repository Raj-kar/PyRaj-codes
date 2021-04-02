# Write a Python program to get the maximum and minimum value in a dictionary.

my_dict = {'x': 500, 'y': 5874, 'z': 560}

_min = my_dict['x'] # 500
_max = my_dict['x'] # 500

for i in my_dict.values():
    if i < _min:
        _min = i
    if i > _max:
        _max = i
        
print(f"Maximum Value: {_max}")
print(f"Minimum Value:  {_min}")
