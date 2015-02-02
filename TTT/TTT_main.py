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

while True:
	
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
    print " Insert Piece - 5"
    print " clear board - 6"
    print " End Game - 7"
    print "########################################"

    # Get User input
    input = raw_input ("Choice: ")
    
    if (input <> 7):
	break

    break
