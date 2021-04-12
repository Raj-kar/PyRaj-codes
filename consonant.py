char = input("Enter a char : ").lower()

if char >= 'a' and char <= 'z':
	if char not in "aeiou":
		print("Consonant")
	else:
		print(None)
else:
	print(None)



# crytography -->

# b = (letter - 1) --> ASCII value --> ASCII Value % 26 --> new letter
# b = (b - 1) = 
# a -> ASCII VALUE --> 97
# 97 -> ASCII VALUE --> 57 + 55 = 112
# 112 % 26 = 8
# 8 = i
