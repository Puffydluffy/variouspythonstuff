from random import randint
# Importing the random function for the board

board = []

for x in range(0, 5):
  board.append(["O"] * 5)
# Setting up board. O stands for ocean.

def print_board(board):
  for row in board:
    print " ".join(row)
# Making board look nicer

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)
# Functions define a random point on the board

ship_row = random_row(board)
ship_col = random_col(board)
# Sets ship row and column

for turn in range(4):
  print "Turn", turn
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))
# Allows user to guess the location

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
    break
# Player wins in this situation
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    # Handles guesses in exterior range
    
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    # Handles repeats
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    # Handles misses
    if turn == 3:
      print "Game Over"
      print "My ship was at row " + str(ship_row) + ", column " + str(ship_col) + "!"
      break
    # Player loses
    print_board(board)