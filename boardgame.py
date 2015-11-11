# boardgame.py
# cd C:\sandbox\gif
# python boardgame.py

# import numpy
import sys
import random


class Boardgame(object):
    width = 0
    height = 0
    rows = []
    columns = []
    diagonals = []
    
    def __init__(self):   
        # set up spaces
        # self.spaces = [self.players[0]*5 for sx in range(self.height * self.width)]
        
        # set up spaces with dictionary
        self.spaces = {}
        for r in range(self.height):
            for c in range(self.width):
                self.spaces[(r,c)] = self.players[0]
        
    def printBoard(self):
        printString = ""
        for r in range(self.height):
            for c in range(self.width):
                printString+=str(self.spaces[(r,c)])
            printString += "\n"
        printString += "\n"
        
        print printString
    
    # defines rows based on spaces
    def getRows(self):
        self.rows = []
        self.row = []
        
        for r in range(self.height):
            for c in range(self.width):
                self.row.append(self.spaces[(r,c)])
            self.rows.append(self.row)
            self.row = []
            
    # defines columns based on spaces
    def getColumns(self):
        self.columns = []
        self.col = []
        
        for c in range(self.width):
            for r in range(self.height):
                self.col.append(self.spaces[(r,c)])
            self.columns.append(self.col)
            self.col = []
    
    # gets all possible diagonals by going around perimeter
    # simpler games like tic-tac-toe will need to use a different method
    def getDiagonals(self):
        pass
        
    def changeSpace(self,x,y,p):
        self.spaces[(x,y)] = self.players[p]
        
    def randomBoard(self):
        for r in range(self.height):
            for c in range(self.width):
                randP = random.randint(0,len(self.players)-1)
                self.spaces[(r,c)] = self.players[randP]
    
    def inputMove(self):
        self.coords = raw_input("\nMove? x,y >>").split(",")
        print self.coords[0]
        print self.coords[1]
        

class TicTacToe(Boardgame):
    width = 3
    height = 3
    players = ["-","X","O"]
    spaces = []
    
    def getDiagonals(self):
        self.diagonals = []
        self.diag = []
        
        for x in range(self.height):
            self.diag.append(self.spaces[(x,x)])
        self.diagonals.append(self.diag)
        self.diag = []
        
        for x in xrange(self.height):
            self.diag.append(self.spaces[(self.height-x-1,x)])
        self.diagonals.append(self.diag)
        self.diag = []

class Connect4(Boardgame):
    width = 6
    height = 4
    players = [".","#","+"]
    spaces = []
    
    
# Main Prpython boardgame.pyogram
print "\n" * 10
ttt = TicTacToe()
c4 = Connect4()

c4.randomBoard()
c4.printBoard()

ttt.randomBoard()
ttt.printBoard()

ttt.getDiagonals()
print ttt.diagonals

