#!/usr/bin/python

# Uncomment for Web Use!
# # enable debugging
# # import cgitb
# # cgitb.enable()

# # print('Content-type: text/html\r\n\r')



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
    players = []
    flagIsFull = False
    winner = 0

    def __init__(self):
        # set up spaces
        # self.spaces = [self.players[0]*5 for sx in range(self.height * self.width)]

        # set up spaces with dictionary
        self.spaces = {}
        for r in range(self.height):
            for c in range(self.width):
                self.spaces[(c, r)] = Space(0)
                # DEBUG
                # print "c=%s, r=%s" % (c, r)
        # DEBUG
        # self.printSpaceList()

    def __str__(self):
        return self.name
    
    # prints board by making string
    # Option 0 = No coordinates
    # Option 1 = With Coordinates
    def printBoard(self,option = 0):
        if option == 1:
            # print coordinates
            printString = "   "
            for x in range(self.width):
                printString += str(x) + " "
            printString += "\n\n"
        else:
            # don't print coordinates
            printString = ""
        for r in range(self.height):
            if option == 1:
                # print coordinates
                printString += str(r) + "  "
            for c in range(self.width):
                printString += str(self.spaces[(c, r)]) + " "
            printString += "\n"
        print printString

    # prints coordinates and values for all spaces
    def printSpaceList(self):
        print "-" * 17
        print "    %s" % self.name
        print "-" * 17

        for y in range(self.height):
            for x in range(self.width):
                print "(x, y) = (%s, %s) = %s" % (x, y, self.spaces[(x, y)])
            print ""
        print ""

    # defines rows based on spaces
    def getRows(self):
        self.rows = []
        self.row = []

        for c in range(self.height):
            for r in range(self.width):
                self.row.append(self.spaces[(c, r)])
            self.rows.append(self.row)
            self.row = []

    # defines columns based on spaces
    def getColumns(self):
        self.columns = []
        self.col = []

        for r in range(self.width):
            for c in range(self.height):
                self.col.append(self.spaces[(c, r)])
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

            for y in range(x, -1, -1):
                z = x-y
                self.diag.append(self.spaces[(y, z)])
                # Debug
                # print "X=%s  Y=%s  Z=%s (x-y)   Space = %s" % (x, y, z, self.spaces[(z, y)])
            self.diagonals.append(self.diag)
            self.diag = []
        # print self.diagonals

    # gets diagonal given starting location
    # direction = 0 goes up-and-right
    # direction = 1 goes up-and-left
    def getDiag(self, i, j, direction):
        self.diag = []
        x = i
        y = j
        if direction == 1:
            # search up-and-left
            # Debug
            # print "Searching up-and-left"
            for x in range(i, -1, -1):
                if y >= 0:
                    # Debug
                    # print "(x, y) = (%s, %s) = %s" % (x, y, self.spaces[(x, y)])
                    self.diag.append(self.spaces[(x, y)])
                    y = y-1
        else:
            # search up-and-right
            # Debug
            # print "Searching up-and-right"
            for x in range(i, self.width, 1):
                if y >= 0:
                    # Debug
                    # print "(x, y) = (%s, %s) = %s" % (x, y, self.spaces[(x, y)])
                    self.diag.append(self.spaces[(x, y)])
                    y = y-1
        return self.diag

    def changeSpace(self, x, y, p):
        self.spaces[(x, y)] = self.players[p.number]

    # creates a random board
    # randomly assigns each space to a player
    def randomBoard(self):
        for r in range(self.height):
            for c in range(self.width):
                randP = random.randint(0, len(self.players)-1)
                self.spaces[(c, r)] = self.players[randP]

    def inputMove(self):
        self.coords = raw_input("\nMove? x, y >>").split(",")
        print self.coords[0]
        print self.coords[1]
        
    def checkIfFull(self):
        self.flagIsFull = True
        for x in range(self.width):
            for y in range(self.height):
                if self.spaces[(x,y)] == self.players[0]:
                    self.flagIsFull = False
    
        

class Space(object):
    marker = "."
    player = 0
    winner = False
    x = 0
    y = 0
    num = 0

    def __init__(self, gb):
        # self.player = gb.players[0]
        # self.marker = gb.players[p].marker
        self.marker = "?"
        pass
        
    def __str__(self):
        return self.marker

class Player(object):
    marker = "."
    number = 0
    spaceCount = 0
    bestMoveX = 0
    bestMoveY = 0
    opportunityCount = 0
    
    def __init__(self, num = 0, m = "."):
        self.marker = m
        self.number = num
    
    def __str__(self):
        return self.marker

class TicTacToe(Boardgame):
    width = 3
    height = 3
    # players = ["-", "X", "O"]
    players = [Player(0, "."), Player(1, "X"), Player(2, "O")]
    spaces = []
    name = "TicTacToe"

    def getDiagonals(self):
        self.diagonals = []
        self.diag = []

        for x in range(self.height):
            self.diag.append(self.spaces[(x, x)])
        self.diagonals.append(self.diag)
        self.diag = []

        for x in xrange(self.height):
            self.diag.append(self.spaces[(self.height-x-1, x)])
        self.diagonals.append(self.diag)
        self.diag = []
    
    # checks to see if entire diagonal is full of non-zeroes
    # checks to see if entire 
    def checkForWin(self):
        w = 0
        p = 0
        self.getDiagonals()
        print self.diagonals
        self.checkSpaces(self.diagonals[0])

    # s = spaces to check
    # winCount = consequtive spaces for a win
    def checkSpaces(self, s):
        currentPlayer = s[0]
        winner = s[0]
        if currentPlayer != self.players[0]:
            for x in s:
                if x != self.players[0]:
                    currentPlayer = x
        else:
            winner = 0
        return winner
                
        

class Connect4(Boardgame):
    width = 6
    height = 4
    # players = [".", "#", "+"]
    players = [Player(0, "."), Player(1, "X"), Player(2, "O")]
    spaces = []
    name = "Connect4"
    
    # def randomBoard(self):
        # for r in range(self.height):
            # for c in range(self.width):
                # randP = random.randint(0, len(self.players)-1)
                # self.spaces[(c, r)] = self.players[randP]
                
    def randomMove(self):
        x = random.randint(0, self.width-1)
        print x
        print self.spaces[(x, 0)]
        if self.spaces[(x, 0)] == self.players[0]:
            self.spaces[(x, 0)] = self.players[random.randint(1,len(self.players)-1)]
        self.applyGravity()
        self.checkIfFull()
    
    def applyGravity(self):
        # DEBUG
        # self.printBoard(1)
        # print "---------------Applying gravity!-----------------\n"
        x = 0
        while x < self.width:
            y = 0
            while y < self.height - 1:
                # DEBUG
                # print "(%s,%s)" % (x, y)
                if self.spaces[(x, y)] != self.players[0] and \
                self.spaces[(x, y + 1)] == self.players[0]:
                    # DEBUG
                    # print "Gap found! @ (%s,%s)" % (x, y)
                    self.changeSpace(x, y + 1, self.spaces[(x, y)])
                    self.changeSpace(x, y, self.players[0])
                    y = -1
                    # DEBUG
                    # print "y = ", y
                    # self.printBoard()
                y += 1
            x += 1
        # self.printBoard(1)

# ==============================
#             MAIN
# ==============================
print "\n" * 10
ttt = TicTacToe()
c4 = Connect4()

c4.randomBoard()
ttt.randomBoard()

ttt.printBoard(1)
c4.printBoard(1)

# print ttt
# s1 = Space(ttt, 0)
# print s1

c4.applyGravity()
print "-----------------APPLY GRAVITY-------------------"

c4.printBoard(1)

# ttt.checkForWin()

# while c4.flagIsFull == False:
#    c4.randomMove()
#    c4.printBoard(1)

# ttt.printSpaceList()
# c4.printSpaceList()


