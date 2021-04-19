import random
# print('''
#  _                                             
# | |                                            
# | |_   _ _ _ _   _ _ _ _ __   _ _ _ _  
# | '_ \ / ` | ' \ / ` | ' ` _ \ / ` | ' \ 
# | | | | (| | | | | (| | | | | | | (_| | | | |
# || ||\_,|| ||\_, || || ||\_,|| ||
#                     __/ |                      
#                    |_/    

# ''')
words_list = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom',
              'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz',
              'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon',
              'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb', 'cockiness', 'croquet']
word = random.choice(words_list)
print(word)
print("Guess the characters : ")
guesses = ''
turns = 6
while turns > 0:
    failed = 0
    for letter in word:
        if letter in guesses:
            print(letter)
        else:
            print("_")

            failed += 1

    if failed == 0:
        print("Congratulations! You Win.")
        print("The word is: ", word)
        break

    guess = input("\nguess a character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print(
            f"Oops! this letter doesn't belong to our dictionary. \nYou have {+ turns} more guesses")

        if turns == 0:
            print(f"The correct word is {word}")
            print("Sorry! You Loose")
