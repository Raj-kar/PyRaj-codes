from random import choice

from hangman_art import logo, stages
from hangman_words import word_list

print(logo)
rand_word = choice(word_list)  # Choose a Random word
# print(rand_word)  # TODO-1 - remove print statement
word_len = len(rand_word)   # get length of word

display = ["_" for _ in range(word_len)]

life = 6  # hangman gets only 6 lifes

print(stages[0])  # print hangman
while life:
    char = input("Guess a char : ").lower() # take input from user

    # If user_char is in rand_word
    if char in rand_word:
        # check the number of presences of char
        if rand_word.count(char) > 1:
            # If the char presences more then 1
            for i in range(word_len):
                letter = rand_word[i]
                if letter == char:
                    display[i] = letter
        else: # If only one char presence
            indx = rand_word.index(char)
            display[indx] = char
    else:
        # If user char doesn't present in rand_word
        print(stages[7 - life]) # print hangman current stage
        life = life - 1 # hangman life drecesed by 1
        print(f"{char} not present in the word !")

    # check if user get the currect word !
    if "_" not in display:
        print("WINNN !!!")
        break
    
    print(*display) # print the current stage of word
    # if life ends !
    if life == 0: 
        print(f"The correct word is {rand_word}") # print the correct word