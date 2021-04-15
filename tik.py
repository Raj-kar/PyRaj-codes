board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

def display_board():
	print(f"{board[0]} | {board[1]} | {board[2]}")
	print(f"{board[3]} | {board[4]} | {board[5]}")
	print(f"{board[6]} | {board[7]} | {board[8]}")

display_board()

u_1 = int(input("In which cell you want to put X "))

board[u_1 - 1] = 'X'

display_board()

u_2 = int(input("In which cell you want to put O "))

board[u_2 - 1] = 'O'

display_board()