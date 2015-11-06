import sys
from random import randint

class Gameboard(object):
    spaces = []
    rowCount = 0
    columnCount = 0
    length = 0

    def __init__(self, rowCount, columnCount):
        spaces = [Space(0) for x in range(rowCount*columnCount)]
        rowCount = rowCount
        columnCount = columnCount
        length = rowCount*columnCount

        curRow = 0
        curCol = 0
        rows = [Row() for x in range(rowCount)]
        columns = [Column() for x in range(columnCount)]
        print "Rows = ", rows, " length = ", len(rows)
        print "Cols = ", columns, " length = ", len(columns)       
        

        for sx, s in enumerate(spaces):
            rows[curRow].add(sx)
            columns[curCol].add(sx)
            print "Row #", str(curRow), " = ", rows[curRow]
            print "Col #", str(curCol), " = ", columns[curCol]
            print "sx = ", sx
            
                   
            if sx>0 and (sx+1)%columnCount == 0:
                curRow+=1
                curCol=0
                print "CurCol reset to ", curCol
            else:
                curCol = curCol + 1
            

    def __repr__(self):
       return "I am a Gameboard!"
       
    def __str__(self):
        boardstring = ""
        curRow = 0
        print "\n\n  ",
        for y in range(self.columnCount):
            sys.stdout.write("%s" % y)
        print "\n\n0 ",
        for sx, s in enumerate(spaces):
            # boardstring+=str(s)
            boardstring+=str(players[s.value])
            if (sx+1)%columnCount == 0:
                curRow+=1
                if curRow < rowCount:
                    boardstring += str("\n%s " % curRow)
                else:
                    boardstring += "\n"
        
        return boardstring
        
    def move(self,moveString):
        pass
    
    def checkForVictory(self,Spaces):
        pass
        
class Engine(object):
    def __init__(self, board):
        pass
    
    def startGame(self):
        print "Welcome to TicTacToe!"
        print a_board
        a_board.move(raw_input("\n\nMove? x,y >> "))

class Space(object):
    def __init__(self, player):
       value = player
       
    def __repr__(self):
        return "I am a Space!"
       
    def __str__(self):
        return str(value)
    
    def value(self):
        return value    
        
    def change(self, player):
        value = player
        
        
class Player(object):
    def __init__(self, marker):
        marker = marker
    
    def __str__(self):
        return marker
    
    def marker(self):
        return marker
    

class Spaces(object):
    def __init__(self):
        print "New unregistered Spaces() created!"
        
        
    def __repr__(self):
        return str(self.spacelist)
       
    def __str__(self):
        return str(self.spacelist)
    
    def countOpportunities(self):
        pass
    
    def countOpportunitiesByColor(self,color):
        pass
    
    def countOccupied(self):
        pass
    
    def countOccupiedByColor(self,color):
        pass
    
    def countEmpty(self,color):
        pass
        
    def add(self, space):
        self.spacelist.append(space)
        # print spacelist
    
class Row(Spaces):
    def __init__(self):
        print "New Row() created!"
        self.spacelist = []

class Column(Spaces):
    def __init__(self):
        print "New Column() created!"
        self.spacelist = []

class Diagonal(Spaces):
    def __init__(self):
        print "New Diagonal() created!"
        self.spacelist = []

players = [Player("-"),Player("X"),Player("O")] #Player 0 is Gaia (the board)
a_board = Gameboard(3,3)
a_game = Engine(a_board)
a_game.startGame()

for px, p in enumerate(players):
    print "Player %r's marker is %s" % (px, p)

for rx, r in enumerate(a_board.rows):
    print "Row #", str(rx), " = ", str(r)

for cx, c in enumerate(a_board.columns):
    print "Col #", str(cx), " = ", str(c)

#  python tictactoe.py

        
