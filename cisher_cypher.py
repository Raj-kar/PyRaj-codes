# encrypt -
# Input - how are you ?
# Output - GNV ZQD XNT ?

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

user_word = input("Enter your message : ").upper()
result = ''

for letter in user_word:
	if letter in alpha:
		curr_indx = alpha.index(letter)
		prev_indx = curr_indx - 1
		result += alpha[prev_indx]
	else:
		result += letter

print(result)

# decrypt the text - homework .
# Input - GNV ZQD XNT ?
# Output - how are you ?

