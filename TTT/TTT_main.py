#!/usr/bin/python
import sys
import TTT

#User 1
global Player_1
global Player_1_symbol
Player_1 = TTT.createUser()
Player_1_symbol = "O"

#User 2
global Player_2
global Player_2_symbol
Player_2 = TTT.createUser()
Player_1_symbol = "X"


print "########################################"
print " Start playing Tic Tac Toe "
print "  [1 2 3 ]		      " 	   	
print "  [4 5 6 ] 		      "
print "  [7 8 9 ]                 "  
print "########################################"
print " Insertion - 1"
print " Display Board - 2"
print " Is Winner - 3"
print " Is Draw - 4"
print " clear board - 5"
print " End Game - 6"
print "########################################"


global turn
turn = 0

while True:

    # Player's turn message
    if (turn == 0):
      print Player_1+"'s turn"
    else:
      print Player_2+"'s turn"

    # Get User choice
    choice = input ("Choice: ")
    if (choice == 6):
	break

    # Displays the board
    if (choice == 2):
    	print TTT.displayBoard()

    # Checks if the match is drawn
    if (choice == 4):
    	print TTT.isDraw()
	

    # Checks if Player won the game
    if (choice == 3):
    	print TTT.isWinner(Player_1)
	

    # Inserts Piece
    if (choice == 1):
       print "  [1 2 3 ]		      " 	   	
       print "  [4 5 6 ] 		      "
       print "  [7 8 9 ]                 "  
       location = input ("Please enter your location: ")

       # Set Player's turn
       if ( turn == 0):
          TTT.insertPiece("X",location)
          turn = 1
       else:
          turn = 0
	  TTT.insertPiece("Y",location)
       
       #display new board post insert
       print TTT.displayBoard()
       
	
    # Clears Board
    if (choice == 5):
    	print TTT.clearBoard()	
