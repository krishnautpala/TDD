#!/usr/bin/python
import sys
import TTT

#User 1
Player_1 = TTT.createUser()

#User 2
Player_2 = TTT.createUser()

# Displays the board
print TTT.displayBoard()

# Checks if the match is drawn
print TTT.isDraw()

# Checks if Player won the game
print TTT.isWinner(Player_1)

# Inserts Piece
print TTT.insertPiece("O")

# Clears Board
print TTT.clearBoard()

