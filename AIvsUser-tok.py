from random import randint
from time import sleep
from termcolor import colored

board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']


def display_board():
    if board[0] == "x":
        print(colored(f'| { board[0]} ', "red"), end=" ")
    else:
        print(colored(f'| { board[0]} ', "green"), end=" ")
    if board[1] == "x":
        print(colored(f'| { board[1]} ', "red"), end=" ")
    else:
        print(colored(f'| { board[1]} ', "green"), end=" ")
    if board[2] == "x":
        print(colored(f'| { board[2]} |', "red"))
    else:
        print(colored(f'| { board[2]} |', "green"))
    if board[3] == "x":
        print(colored(f'| { board[3]} ', "red"), end=" ")
    else:
        print(colored(f'| { board[3]} ', "green"), end=" ")
    if board[4] == "x":
        print(colored(f'| { board[4]} ', "red"), end=" ")
    else:
        print(colored(f'| { board[4]} ', "green"), end=" ")
    if board[5] == "x":
        print(colored(f'| { board[5]} |', "red"))
    else:
        print(colored(f'| { board[5]} |', "green"))
    if board[6] == "x":
        print(colored(f'| { board[6]} ', "red"), end=" ")
    else:
        print(colored(f'| { board[6]} ', "green"), end=" ")
    if board[7] == "x":
        print(colored(f'| { board[7]} ', "red"), end=" ")
    else:
        print(colored(f'| { board[7]} ', "green"), end=" ")
    if board[8] == "x":
        print(colored(f'| { board[8]} |', "red"))
    else:
         print(colored(f'| { board[8]} |', "green"))

    # print(colored(f'| {board[0]} |  {board[1]} | {board[2]} |', 'green'))
    # print(colored(f'| {board[3]} |  {board[4]} | {board[5]} |', 'green'))
    # print(colored(f'| {board[6]} |  {board[7]} | {board[8]} |', 'green'))

def check_horizon(val1, val2, val3, sign):
    if board[val1] == board[val2] == board[val3] == sign:
        print(f"{sign} WINS !")
        return True

def check_vertical(val1, val2, val3, sign):
    if board[val1] == board[val2] == board[val3] == sign:
        print(f"{sign} WINS !")
        return True

def check_digonal(val1, val2, val3):
    if board[val1] == board[val2] == board[val3] == "x":
        print("X WINS !")
        return True
    elif board[val1] == board[val2] == board[val3] == "o":
        print("O WINS !")
        return True

def check_win():
    win = False
    for i in range(0, 9, 3):
        win = check_horizon(i, i+1, i+2, 'x')
        if win:
            return win
        win = check_horizon(i, i+1, i+2, 'o')
        if win:
            return win

    for i in range(3):
        win = check_vertical(i, i+3, i+6, 'x')
        if win:
            return win
        win = check_vertical(i, i+3, i+6, 'o')
        if win:
            return win

    win = check_digonal(0, 4, 8)
    if win:
        return win
    win = check_digonal(2, 4, 6)
    if win:
        return win


def handel_move(sign):
    if sign == "x":
        turn = int(input(f"choose a spot({sign}):  [1-9] "))

        if turn > 0 and turn < 10 and board[turn - 1] == "_" :
            board[turn - 1] = sign
        else:
            print("Invalid move !")
            handel_move(sign) # Recursion
    else:
        sleep(2)
        turn = randint(0, 8)

        if board[turn] == "_":
            print(f"Computer put at {turn + 1} .... !")
            board[turn] = "o"
        else:
            handel_move(sign)


def game():
    text = colored('Welcome to tik - tok - tea game !!', 'magenta')
    print(text)

    count = 0
    while True:

        display_board()
        if count > 2:
            if check_win():
                break

        handel_move("x")
        display_board()

        if count >= 2:
            if check_win():
                break

        if count == 4:
            print("DRAWSSS !!!")
            break

        handel_move("o")

        count += 1

game()