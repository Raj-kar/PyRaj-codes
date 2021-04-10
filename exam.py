'''
The alphabets are enumerated as A = 0, B = 1, C = 2, ... , Z = 25. Consider an encryption scheme where a
character with value Ci in the plaintext is replaced by another character with value Cj using the formula
Cj = (Ci + 5) % 26. After replacement, the resulting string is shuffled (permuted) at random to obtain the
cipher text.
Given a plain text and a possible cipher text, your task is to determine whether the cipher text can be formed
from the plain text using the above mentioned scheme.
*(Assume that all the strings are in uppercase)*

Input Format:
The first line of the input contains a string indicating the plain text.
The second line of the input a string indicating a possible cipher text

Output Format:
Display Yes or No (no newline after the output)

Example:

Input:
PYTHON
TDMSUY

Output: Yes

Input:
JOCPNPTEL
JQYVSUTHO

Output: No
'''

from string import ascii_uppercase as uc

alpha = {uc[i]:i for i in range(len(uc))}
print(alpha)

plain_text = input().upper()
cypher_text = input().upper()
text = ''

for letter in plain_text:
	ci = alpha[letter]
	cj = (ci + 5) % 26
	text += chr(cj + 65)

if sorted(text) == sorted(cypher_text):
	print("Yes", end='')
else:
	print("No", end='')