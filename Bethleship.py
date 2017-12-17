from random import randint
import time

board = []
board_size = 0

def build_board():
  global board_size
  board_size = int(input("What size board do you want? (5-10): "))
  if board_size >= 5 and board_size <= 10:
    for x in range(0, board_size):
      board.append(["O"] * board_size)
  elif board_size > 10:
    print("That\'s too big!")
    time.sleep(1.3)
    print("That\'s what she said...\n")
    time.sleep(1)
    build_board()

def print_board(board):
  for row in board:
    print(" ".join(row))

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

build_board()
print_board(board)
ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
  print("\nTurn", turn + 1)
  turn += 1
  guess_row = int(input("\nGuess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print("\nCongratulations! You sank my battleship!")
    break
  else:
    if guess_row not in range(board_size) or guess_col not in range(board_size):
      print("\nOops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print( "\nYou guessed that one already." )
    else:
      print( "\nYou missed my battleship!")
      board[guess_row][guess_col] = "X"
  if turn == 4:
    print("\nGame Over")
    break
  print('\n')
  print_board(board)