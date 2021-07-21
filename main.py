from random import randint

board = [
	[' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
	[' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
	[' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
	['-', '-', '-', '+', '-', '-', '-', '+', '-', '-', '-'],
	[' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
	[' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
	[' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
	['-', '-', '-', '+', '-', '-', '-', '+', '-', '-', '-'],
	[' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
	[' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
	[' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
]

def print_board():
	for row in board:
		for c in row:
			print(c,end = "")
		print()

def check_empty(row, piece):
	if board[row][piece] == ' ':
		return True
	return False

def check_winner(board, user):
	piece = ''
	if user != 'cpu':
		piece = 'X'
	elif user == 'cpu':
		piece = 'O'

	if board[1][1] == piece and board[1][5] == piece and board[1][9] == piece:
		print(f"\n{user} Won!!")
		quit()

	elif board[5][1] == piece and board[5][5] == piece and board[5][9] == piece:
		print(f"\n{user} Won!!")
		quit()

	elif board[9][1] == piece and board[9][5] == piece and board[9][9] == piece:
		print(f"\n{user} Won!!")
		quit()

	elif board[1][1] == piece and board[5][1] == piece and board[9][1] == piece:
		print(f"\n{user} Won!!")
		quit()

	elif board[1][5] == piece and board[5][5] == piece and board[9][5] == piece:
		print(f"\n{user} Won!!")
		quit()

	elif board[1][9] == piece and board[5][9] == piece and board[9][9] == piece:
		print(f"\n{user} Won!!")
		quit()

	elif board[1][1] == piece and board[5][5] == piece and board[9][9] == piece:
		print(f"\n{user} Won!!")
		quit()

	elif board[1][9] == piece and board[5][5] == piece and board[9][1] == piece:
		print(f"\n{user} Won!!")
		quit()


def place_piece(user,pos, board):
	if user == "player":
		piece = 'X'
	elif user == "cpu":
		piece = 'O'
	if pos == 1:
		if check_empty(1,1):
			board[1][1] = piece
		elif user == "player":
			print("Not an empty space. Please Try again!!!")
		elif user == 'cpu':
			pos = randint(1, 9)
			place_piece("cpu",pos,board)
	elif pos == 2:
		if check_empty(1,5):
			board[1][5] = piece
		elif user == "player":
			print("Not an empty space. Please Try again!!!")
		elif user == 'cpu':
			pos = randint(1, 9)
			place_piece("cpu",pos,board)
	elif pos == 3:
		if check_empty(1,9):
			board[1][9] = piece
		elif user == "player":
			print("Not an empty space. Please Try again!!!")
		elif user == 'cpu':
			pos = randint(1, 9)
			place_piece("cpu",pos,board)
	elif pos == 4:
		if check_empty(5,1):
			board[5][1] = piece
		elif user == "player":
			print("Not an empty space. Please Try again!!!")
		elif user == 'cpu':
			pos = randint(1, 9)
			place_piece("cpu",pos,board)
	elif pos == 5:
		if check_empty(5,5):
			board[5][5] = piece
		elif user == "player":
			print("Not an empty space. Please Try again!!!")
		elif user == 'cpu':
			pos = randint(1, 9)
			place_piece("cpu",pos,board)
	elif pos == 6:
		if check_empty(5,9):
			board[5][9] = piece
		elif user == "player":
			print("Not an empty space. Please Try again!!!")
		elif user == 'cpu':
			pos = randint(1, 9)
			place_piece("cpu",pos,board)
	elif pos == 7:
		if check_empty(9,1):
			board[9][1] = piece
		elif user == "player":
			print("Not an empty space. Please Try again!!!")
		elif user == 'cpu':
			pos = randint(1, 9)
			place_piece("cpu",pos,board)
	elif pos == 8:
		if check_empty(9,5):
			board[9][5] = piece
		elif user == "player":
			print("Not an empty space. Please Try again!!!")
		elif user == 'cpu':
			pos = randint(1, 9)
			place_piece("cpu",pos,board)
	elif pos == 9:
		if check_empty(9,9):
			board[9][9] = piece
		elif user == "player":
			print("Not an empty space. Please Try again!!!")
		elif user == 'cpu':
			pos = randint(1, 9)
			place_piece("cpu",pos,board)


def main():
	print("Welcome To Tic Tac Toe!!")
	name = input("Enter your name: ")
	while True:
		player_pos = int(input("Enter a position (1-9): "))
		if player_pos <= 9 and player_pos > 0:
			place_piece("player", player_pos, board)
			cpu_pos = randint(1,9)
			place_piece("cpu", cpu_pos, board)
			print_board()
			check_winner(board, name)
			check_winner(board, 'cpu')
		else:
			print("Invalid move.. Please try again!!")
			continue


if __name__ == '__main__':
	print_board()
	main()
