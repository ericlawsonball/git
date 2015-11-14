# boardgame.py
# cd r:\sandbox\git
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
    name = "B04RDG4M3"
    
    def __init__(self):   
        # set up spaces
        # self.spaces = [self.players[0]*5 for sx in range(self.height * self.width)]
        
        # set up spaces with dictionary
        self.spaces = {}
        for r in range(self.height):
            for c in range(self.width):
                self.spaces[(c,r)] = self.players[0]
                # DEBUG
                print "c=%s, r=%s" % (c,r)
        # DEBUG
        self.printSpaceList()
    
    # prints board by making strings of rows
    def printBoardPlain(self):
        printString = ""
        for r in range(self.height):
            for c in range(self.width):
                printString+=str(self.spaces[(c,r)]) + " "
            printString += "\n"
        printString += "\n"        
        print printString
        
    # prints board with coordinates for making moves
    def printBoard(self):
        printString = "   "
        for x in range(self.width):
            printString += str(x) + " "
        printString += "\n\n"
        for r in range(self.height):
            printString += str(r) + "  "
            for c in range(self.width):
                printString+=str(self.spaces[(c,r)]) + " "
            printString += "\n"
        printString += "\n"        
        print printString
    
    # prints coordinates and values for all spaces
    def printSpaceList(self):
        print "-" * 17
        print "    %s" % self.name
        print "-" * 17
        
        for y in range(self.height):
            for x in range(self.width):
                print "(x,y) = (%s,%s) = %s" % (x,y,self.spaces[(x,y)])
            print ""
        print ""
    
    # defines rows based on spaces
    def getRows(self):
        self.rows = []
        self.row = []
        
        for c in range(self.height):
            for r in range(self.width):
                self.row.append(self.spaces[(c,r)])
            self.rows.append(self.row)
            self.row = []
            
    # defines columns based on spaces
    def getColumns(self):
        self.columns = []
        self.col = []
        
        for r in range(self.width):
            for c in range(self.height):
                self.col.append(self.spaces[(c,r)])
            self.columns.append(self.col)
            self.col = []
    
    # Gets all possible diagonals by going around perimeter
    # Simpler games like tic-tac-toe will need to use a different method
    # Starts in upper left corner and goes down the column, working up and right for every diagonal
    #   then moves to upper-right corner and does the reverse
    def getDiagonals(self):
        self.diagonals = []
        self.diag = []
        for x in range(self.height):
            
            for y in range(x,-1,-1):
                z = x-y
                self.diag.append(self.spaces[(y,z)])
                # Debug
                # print "X=%s  Y=%s  Z=%s (x-y)   Space = %s" % (x,y,z, self.spaces[(z,y)])
            self.diagonals.append(self.diag)
            self.diag = []
        print self.diagonals
    
    # gets diagonal given starting location
    # direction = 0 goes up-and-right
    # direction = 1 goes up-and-left
    def getDiag(self,i,j,direction):
        self.diag = []
        x = i
        y = j
        if direction == 1:
            # search up-and-left
            print "Searching up-and-left"
            for x in range(i,-1,-1):
                if y>=0:
                    print "(x,y) = (%s,%s) = %s" % (x,y,self.spaces[(x,y)])
                    self.diag.append(self.spaces[(x,y)])
                    y=y-1         
        else:
            # search up-and-right
            print "Searching up-and-right"
            for x in range(i,self.width,1):
                if y>=0:
                    print "(x,y) = (%s,%s) = %s" % (x,y,self.spaces[(x,y)])
                    self.diag.append(self.spaces[(x,y)])
                    y=y-1

        return self.diag
        

        
    def changeSpace(self,x,y,p):
        self.spaces[(x,y)] = self.players[p]
    
    # creates a random board
    # randomly assigns each space to a player
    def randomBoard(self):
        for r in range(self.height):
            for c in range(self.width):
                randP = random.randint(0,len(self.players)-1)
                self.spaces[(c,r)] = self.players[randP]
    
    def inputMove(self):
        self.coords = raw_input("\nMove? x,y >>").split(",")
        print self.coords[0]
        print self.coords[1]
        

class TicTacToe(Boardgame):
    width = 3
    height = 3
    players = ["-","X","O"]
    spaces = []
    name = "TicTacToe"
    
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
    name = "Connect4"
    
# ==============================
#             MAIN
# ==============================
print "\n" * 10
ttt = TicTacToe()
c4 = Connect4()

c4.randomBoard()
c4.printBoard()

ttt.randomBoard()
ttt.printBoard()

ttt.printSpaceList()
c4.printSpaceList()

print "C4.WIDTH = ", c4.width
print "C4.HEIGHT = ", c4.height

# ttt.getDiagonals()
# print ttt.diagonals

print ""
c4.printBoard()

print c4.getDiag(3,3,0)
print c4.getDiag(3,3,1)

print c4.getDiag(0,0,0)
print c4.getDiag(0,0,1)

print c4.getDiag(5,3,0)
print c4.getDiag(5,3,1)



