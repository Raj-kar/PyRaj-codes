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

def encrypt(user_word, output):
	alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	result = ''

	for letter in user_word:
		if letter in alpha:
			curr_indx = alpha.index(letter)
			aftr_indx = (curr_indx + 5) % 26
			result += alpha[aftr_indx]
	
	if sorted(result) == sorted(output):
		return "Yes"
	else:
		return "No"

print(encrypt("PYTHON", "TDMSUY"))
print(encrypt("JOCPNPTEL", "JQYVSUTHO"))