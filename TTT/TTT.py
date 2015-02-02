#!/usr/bin/python
import sys

# Initialize a 3x3 table with -1
global table
table = [ [ 0 for i in range(3) ] for j in range(3) ]


# Displays current board
def displayBoard():
    pass
    return table

# Checks if the match is drawn
def isDraw():    
    # Check if board is full
    for row in range(3):
	for column in range(3):
	    if (table[row][column] == 0):
	    	return 1
    # Check if Player1 has matrix complete
    isPlayer1_won = isWinner(Player)
    # Check if Player2 has matrix complete
    isPlayer2_won = isWinner(Player)
    # If both have complete return match drawn
    if  isPlayer1_won == '0' and isPlayer2_won == '0':
	return "Match Drawn"

    return 1

# Checks if a player is won
def isWinner(Player):
    global table
    # Check if row is complete
    # [x][x][x]
    # [0][0][x]
    # [x][x][0]
    # Is row 1 complete
    if (table[0][0] == ""  and table[0][1] == "" and table[0][2] ==""):
	    return 1
	# Is row 2 complete
    if (table[1][0] == ""  and table[1][1] == "" and table[1][2] == ""):
	    return 1
	# Is row 3 complete
    if (table[2][0] == ""  and table[2][1] == "" and table[2][2] == ""):
	    return 1

    # Check if column is complete
    # [0][x][0]
    # [0][x][x]
    # [x][x][0]

    # Is column 1 complete
    if (table[0][0] == ""  and table[1][0] == "" and table[2][0] == ""):
	    return 1
    # Is column 2 complete
    if (table[0][1] == ""  and table[1][1] == "" and table[2][1] == ""):
	    return 1
    # Is column 3 complete
    if (table[0][2] == ""  and table[1][2] == "" and table[2][2] == ""):
	    return 1

    # Check if diagonal is complete
    # [0][0][x]
    # [0][x][x]
    # [x][x][0]
    # Is diagonal complete
    if (table[0][0] == ""  and table[1][1] == "" and table[2][2] == ""):
	    return 1
	# Is diagonal complete
    if (table[0][2] == ""  and table[1][1] == "" and table[2][0] == ""):
	    return 1

    return 0

# Inserts  a piece
def insertPiece(Piece,location):

    # Insert the piece onto location
    global table
    if ( location == 1 ):
	if (table[0][0] == "0"):
	    table[0][0] = Piece
    if ( location == 2 ):
	if (table[0][1] == "0"):
	    table[0][1] = Piece
    if ( location == 3 ):
	if (table[0][2] == "0"):
	    table[0][2] = Piece
    if ( location == 4 ):
	if (table[1][0] == "0"):
	    table[1][0] = Piece
    if ( location == 5 ):
	if (table[1][1] == "0"):
	    table[1][1] = Piece
    if ( location == 6 ):
	if (table[1][2] == "0"):
	    table[1][2] = Piece
    if ( location == 7 ):
	if (table[2][0] == "0"):
	    table[2][0] = Piece
    if ( location == 8 ):
	if (table[2][1] == "0"):
	    table[2][1] = Piece
    if ( location == 9 ):
	if (table[2][2] == "0"):
	    table[2][2] = Piece

    return 0

# Clear the board
def clearBoard():
    global table
    table = []
    return table

# User account creation
def createUser():
    Player_Name = raw_input ("Please Enter you name: ")
    return Player_Name




