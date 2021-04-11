# encrypt -
# Input - how are you ?
# Output - GNV ZQD XNT ?



# decrypt the text - homework .
# Input - GNV ZQD XNT ?
# Output - how are you ?

# def encrypt(user_word):
# 	alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# 	result = ''

# 	for letter in user_word:
# 		if letter in alpha:
# 			curr_indx = alpha.index(letter)
# 			prev_indx = curr_indx - 1
# 			result += alpha[prev_indx]
# 		else:
# 			result += letter

# 	print(result)


# def decrypt(user_word):
# 	alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
# 	result = ''

# 	for letter in user_word:
# 		if letter in alpha:
# 			curr_indx = alpha.index(letter)
# 			aftr_indx = curr_indx + 1
# 			result += alpha[aftr_indx]
# 		else:
# 			result += letter

# 	print(result)

def enc_dec(user_word, choice):
	alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
	result = ''

	for letter in user_word:
		if letter in alpha:
			curr_indx = alpha.index(letter)
			if choice == "e":
				aftr_indx = curr_indx - 1
			elif choice == "d":
				aftr_indx = curr_indx + 1
			result += alpha[aftr_indx]
		else:
			result += letter

	print(result)

choice = input("Enter e for encrypt and d for decrypt : ")
user_word = input("Enter your text :: ").upper()

if choice == "e" or choice == "d":
	enc_dec(user_word, choice)
else:
	print("Wrong choice !!")