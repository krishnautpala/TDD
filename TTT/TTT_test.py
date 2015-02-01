#!/usr/bin/python
import sys
import TTT

#User 1
Player_1 = TTT.createUser()

#User 2
Player_2 = TTT.createUser()

print TTT.displayBoard()
print TTT.isDraw()
print TTT.isWinner(Player_1)
print TTT.insertPiece("O")
print TTT.clearBoard()

