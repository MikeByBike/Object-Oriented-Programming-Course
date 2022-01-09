# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 23:05:27 2021

Authors: Michalis Iona, Ayush Pradhan

This is a battleship game, where computer and the player have their own board(ocean) where we place 10 ships in random position.
The player searches for the ships of the computer and the vice versa. Who ever destroys all the ship is declared as the winner.
modes-
1. Classic mode : both computer get one by one change
2. Chain mode : both computer and player gets 10 chances

If the player or the computer strickes one part of the ship, they get one more point to attack.

fleet size
1. Big fleet - 10
2. small fleet - 6

"""


import tkinter as tk
import random
import copy # copy operation


# dimension of the gaming board
squeareWidth = 30 # length value
squareHeigth = 30 # breadth value
squareNumber = 10 

root = tk.Tk(className="BattleshipsOOP")
button1_text = tk.StringVar()
button2_text = tk.StringVar()
button3_text = tk.StringVar()
button4_text = tk.StringVar()


""" Number of boats on the board """
class Player(object):
    # One battleship with length of 5
    battleshippositionX = None
    battleshippositionY = None
    # Two cruiser with length of 4
    cruiserpositionX = [None] * 2
    cruiserpositionY = [None] * 2 
    # Three destroyer with length of 3
    destroyrtpositionX = [None] * 3
    destroyrtpositionY = [None] * 3
    # Four submarines with length of 2
    submarinepositionX = [None] * 4
    submarinepositionY = [None] * 4
""" Real player board """
class RealPlayer(Player):
    binCanvas = [0] * squareNumber
    for i in range(squareNumber):
        binCanvas[i] = [0] * squareNumber
    randomOnesX = [] # generating position of ships in horizontal
    randomOnesY = [] # generating position of ships in vertical
    name = "PLAYER AREA"
    location = 2 # location of the label
    tk.Label(root, text = name).grid(row = location)
    canvas = tk.Canvas(root, width=squeareWidth*squareNumber, height=squareHeigth*squareNumber)
    canvas.grid(row = location + 1) 
    shipsLeft = 10 # total number of ships in the ocean (board)    
    def pickCoordinates(self): 
        return
""" Computer Board """
class Computer(Player):
    binCanvas = [0] * squareNumber
    for i in range(squareNumber):
        binCanvas[i] = [0] * squareNumber
    randomOnesX = [] # generating position of ships in horizontal
    randomOnesY = [] # generating position of ships in vertical
    name = "COMPUTER AREA"
    location = 0 # location of the label
    tk.Label(root, text = name).grid(row = location)
    canvas = tk.Canvas(root, width=squeareWidth*squareNumber, height=squareHeigth*squareNumber)
    canvas.grid(row = location + 1)
    shipsLeft = 10 # total number of ships in the ocean (board)
    def pickCoordinates(self):
        return
""" gameboard class """
class GameBoard:
    fireMode = 0
    fleet = 0
    level = 0
    shootsLeft = 6
    gameState = 0
    computerPlayer = Computer()
    realPlayer = RealPlayer()
    counter = [0,0]
    computerCount = 0
    realPlayerCount = 0
    members = [computerPlayer, realPlayer] # Computer = 0 Player = 1
    turn = 0
    gameOver = 0
    pickedLength = 30
    pickedDirection = 0
    lastDrawX = []
    lastDrawY = []
    tempCanvas = copy.deepcopy(members[1].binCanvas) # used to implement deepcopy
    __instance = None

    @staticmethod # staticmethod is bound to the class
    def getInstance():
        """ Static access method. """
        if GameBoard.__instance == None:
            GameBoard()
        return GameBoard.__instance
# Batlleship has only one instance of the class. It follows singleton class
    def __init__(self):
        """ Virtually private constructor. """
        if GameBoard.__instance != None:
            raise Exception("This class is a singleton class!") # class that can have only one object 
        else:
            GameBoard.__instance = self        
        return
    """ Board button colors """   
    def showFields(self, player):
        for y in range (squareNumber):
            for x in range (squareNumber):
                if self.members[player].binCanvas[x][y] == 1:
                    self.members[player].canvas.create_rectangle(x*squeareWidth,y*squareHeigth, (x*squeareWidth) +  squeareWidth ,(y*squareHeigth) + squareHeigth, fill="grey")
                if self.members[player].binCanvas[x][y] == 0:
                    self.members[player].canvas.create_rectangle(x*squeareWidth,y*squareHeigth,(x*squeareWidth) +  squeareWidth ,(y*squareHeigth) + squareHeigth, fill="white")
                if player == 1:    
                    if self.members[player].binCanvas[x][y] == 2:
                        self.members[player].canvas.create_rectangle(x*squeareWidth,y*squareHeigth,(x*squeareWidth) +  squeareWidth ,(y*squareHeigth) + squareHeigth, fill="green")
                else:
                    if self.members[player].binCanvas[x][y] == 2:
                        self.members[player].canvas.create_rectangle(x*squeareWidth,y*squareHeigth,(x*squeareWidth) +  squeareWidth ,(y*squareHeigth) + squareHeigth, fill="white")
                if self.members[player].binCanvas[x][y] == 3:
                    self.members[player].canvas.create_rectangle(x*squeareWidth,y*squareHeigth,(x*squeareWidth) +  squeareWidth ,(y*squareHeigth) + squareHeigth, fill="red")
    """ To find the winner """
    def checkWin(self):
        if self.members[0].shipsLeft == 0 :
            button1_text.set("You Win - Play Again")
            return True
        elif self.members[1].shipsLeft == 0:
            button1_text.set("Game Over - Play Again")
            return True
        else:
            button1_text.set("Give Up!")
            return False
    """ attacking """
    def shoot(self, x, y, player):
        if self.fireMode == 1 and self.shootsLeft == 0: # i shots are done then program stops
            return
        if self.gameState == 3:
            return
        self.gameState = 1
        if x < 0 or y < 0 or x > 9 or y > 9: # checks that if its outside the borders then restarts
            return 1
        hit = 0
        if self.members[player].binCanvas[x][y] == 1 or self.members[player].binCanvas[x][y] == 3:
            hit = 1
            return hit
        if self.members[player].binCanvas[x][y] == 0:
            self.members[player].binCanvas[x][y] = 1
            hit = 2
        if self.members[player].binCanvas[x][y] == 2:
            self.members[player].binCanvas[x][y] = 3
            self.counter[player] = self.counter[player] + 1
            hit = 3
        
        self.showFields(player)
        if self.fireMode == 1:
            self.shootsLeft = self.shootsLeft - 1
            if self.shootsLeft == 0:
                if self.turn == 1:
                    self.turn = 0
                else:
                    self.turn = 1
            return hit
        
        if hit == 2:
            if self.turn == 1:
                self.turn = 0
            else:
                self.turn = 1
            return hit
        else:
            return hit
    """ Checking for appropriate space between the ships """
    def spaceChecker(self, length, direction, x, y, player):
        for i in range (0, length):
            if direction == 1:
                if x > 0 and x < 9 and (self.members[player].binCanvas[x+1][y+i] == 2 or self.members[player].binCanvas[x-1][y+i] == 2):
                    return True
                if y > 0 and y < 9 and (self.members[player].binCanvas[x][y+i+1] == 2 or self.members[player].binCanvas[x][y-1] == 2):
                    return True
                if self.members[player].binCanvas[x][y+i] == 2:
                    return True
                if x == 0 and (self.members[player].binCanvas[x+1][y+i] == 2):
                    return True
                if x == 9 and (self.members[player].binCanvas[x-1][y+i] == 2):
                    return True
                if y == 0 and (self.members[player].binCanvas[x][y+1+i] == 2):
                    return True
                if y == 9 and (self.members[player].binCanvas[x][y-1] == 2):
                    return True
            else:
                if y > 0 and y < 9 and (self.members[player].binCanvas[x+i][y+1] == 2 or self.members[player].binCanvas[x+i][y-1] == 2):
                    return True
                if x > 0 and x < 9 and (self.members[player].binCanvas[x+i+1][y] == 2 or self.members[player].binCanvas[x-1][y] == 2):
                    return True
                if self.members[player].binCanvas[x+i][y] == 2:
                    return True
                if y == 0 and (self.members[player].binCanvas[x+i][y+1] == 2):
                    return True
                if y == 9 and (self.members[player].binCanvas[x+i][y-1] == 2):
                    return True
                if x == 0 and (self.members[player].binCanvas[x+i+1][y] == 2):
                    return True
                if x == 9 and (self.members[player].binCanvas[x-1][y] == 2):
                    return True
        return False
    """ setting the board with random placements """
    def setFields(self, length, player):
        while True:
            crossing = False
            direction = random.randint(0,1)
            x = random.randint(0, 9-length) if direction == 0 else random.randint(0,9)# returns random integers between the end points for X value
            y = random.randint(0, 9-length) if direction == 1 else random.randint(0,9)# returns random integers between the end points for Y value
            
            crossing = self.spaceChecker(length, direction, x, y, player)

            if crossing: 
                continue
            for i in range (0,length):
                if direction == 1:
                    self.members[player].binCanvas[x][y+i] = 2
                else:
                    self.members[player].binCanvas[x+i][y] = 2
            break
    """ choosing points on board """
    def choose(self, player):
        self.members[player].binCanvas = [0] * squareNumber
        for i in range(squareNumber):
            self.members[player].binCanvas[i] = [0] * squareNumber
        if self.fleet == 0:
            for i in range(5, 1, -1):
                for x in range(0,6-i):
                    self.setFields(i,player)
        else:
            for i in range(4, 1, -1):
                for x in range(0,5-i):
                    self.setFields(i,player)

    """ define on how the game works """
    def play(self):
        squareNumber
        self.choose(0) # computer = 0
        self.choose(1) # player = 1
        self.showFields(0)
        self.showFields(1)
        hit = 1
        hitX = 0
        hitY = 0
        direction = 0
        changeDirection = 0
        tempTurn = 1
        while not self.gameOver:
            if self.gameState != 0 and self.checkWin():
                self.shootsLeft = 6
                self.gameState = 0
                self.turn = 0
            if self.turn == 0:
                if tempTurn != self.turn:
                    tempTurn = self.turn
                    self.shootsLeft = self.members[1].shipsLeft
                if self.gameState == 0 or self.gameState == 3:
                    self.members[1].canvas.bind('<Button-1>', self.pick) # binding function
                else:
                    self.members[1].canvas.unbind('<Button-1>')
                
                self.members[0].canvas.bind('<Button-1>', self.realPlayerShoot)
                root.update()
            else:
                self.members[0].canvas.unbind('<Button-1>')
                if tempTurn != self.turn:
                    tempTurn = self.turn
                    self.shootsLeft = self.members[0].shipsLeft

                if self.fireMode == 1 and self.level == 1 and len(self.members[1].randomOnesX)>0:
                    shipsLeft = True
                    for i in range(len(self.members[1].randomOnesX)):
                        if self.members[1].binCanvas[self.members[1].randomOnesX[i]][self.members[1].randomOnesY[i]] != 3:
                            self.shoot(self.members[1].randomOnesX[i], self.members[1].randomOnesY[i], 1)
                    if not shipsLeft:
                        self.members[1].randomOnesX.clear()
                        self.members[1].randomOnesY.clear()
                if direction == 0:
                    if hit == 1 or hit == 2:
                        pressure = 0
                        while True:
                            pressure = pressure + 1
                            if pressure > 120:
                                break
                            x = random.randrange(0,squareNumber)
                            y = random.randrange(0,squareNumber)
                            if pressure < 60:
                                if (x % 2 == 1 and y % 2 == 0):
                                    continue
                                if x + 1 <= 9 and (self.members[1].binCanvas[x+1][y] == 1): 
                                    continue
                                if x - 1 >= 0 and (self.members[1].binCanvas[x-1][y] == 1): 
                                    continue
                                if y + 1 <= 9 and (self.members[1].binCanvas[x][y+1] == 1): 
                                    continue
                                if y - 1 >= 0 and (self.members[1].binCanvas[x][y-1] == 1): 
                                    continue
                            if (x % 2 == 1 and y % 2 == 0):
                                continue
                            if x + 1 <= 9 and (self.members[1].binCanvas[x+1][y] == 3): 
                                continue
                            if x - 1 >= 0 and (self.members[1].binCanvas[x-1][y] == 3): 
                                continue
                            if y + 1 <= 9 and (self.members[1].binCanvas[x][y+1] == 3): 
                                continue
                            if y - 1 >= 0 and (self.members[1].binCanvas[x][y-1] == 3): 
                                continue
                            if not self.members[1].binCanvas[x][y] == 1 or self.members[1].binCanvas[x][y] == 3:
                                break
                        hit = self.shoot(x, y, 1)
                        hitX = x
                        hitY = y
                        if hit == 3 and self.level == 1:
                            self.shipFinder(1, x, y)
                            for i in range(len(self.members[1].randomOnesX)):
                                self.shoot(self.members[1].randomOnesX[i], self.members[1].randomOnesY[i], 1)
                            self.members[1].shipsLeft = self.members[1].shipsLeft - 1
                            hit = 1
                    if hit == 3:
                        while True:
                            trigger = self.shoot(hitX -1, hitY, 1)
                            if trigger == 2: 
                                break
                            elif trigger == 3:
                                direction = 1
                                hit = 1
                                break
                            trigger = self.shoot(hitX + 1, hitY, 1)
                            if trigger == 2: 
                                break
                            elif trigger == 3:
                                direction = 2
                                hit = 1
                                break
                            trigger = self.shoot(hitX, hitY -1, 1)
                            if trigger == 2: 
                                break
                            elif trigger == 3:
                                direction = 3
                                hit = 1
                                break
                            trigger = self.shoot(hitX, hitY +1, 1)
                            if trigger == 2: 
                                break
                            elif trigger == 3:
                                direction = 4
                                hit = 1
                                break
                if direction != 0 and changeDirection < 2:
                    counter = 0
                    if changeDirection == 0:
                        counter = 2
                    else:
                        counter = 1
                    while True and counter < 5:
                        if direction == 1:
                            trigger = self.shoot(hitX - counter, hitY, 1)
                            if trigger == 2 or trigger == 1:
                                direction = 2
                                changeDirection = changeDirection + 1
                                break
                            else:
                                counter = counter + 1
                        if direction == 2:
                            trigger = self.shoot(hitX + counter, hitY, 1)
                            if trigger == 2 or trigger == 1:
                                direction = 1
                                changeDirection = changeDirection + 1
                                break
                            else:
                                counter = counter + 1
                        if direction == 3:
                            trigger = self.shoot(hitX, hitY  - counter, 1)
                            if trigger == 2 or trigger == 1:
                                direction = 4
                                changeDirection = changeDirection + 1
                                break
                            else:
                                counter = counter + 1
                        if direction == 4:
                            trigger = self.shoot(hitX, hitY + counter, 1)
                            if trigger == 2 or trigger == 1:
                                direction = 3
                                changeDirection = changeDirection + 1
                                break
                            else:
                                counter = counter + 1
                if direction > 0 and changeDirection > 1:
                    self.members[1].shipsLeft = self.members[1].shipsLeft - 1
                    hit = 1
                    changeDirection = 0
                    direction = 0
                root.update()
    """ player shooting """
    def realPlayerShoot(self, event):
        x = int(event.x/squeareWidth)
        y = int(event.y/squareHeigth)
        hit = self.shoot(x, y, 0)
        if hit == 3:
            self.shipFinder(0, x, y)
            print(self.members[0].randomOnesX)
            print(self.members[0].randomOnesY)
            shipsLeft = False
            for i in range(len(self.members[0].randomOnesX)):
                if self.members[0].binCanvas[self.members[0].randomOnesX[i]][self.members[0].randomOnesY[i]] != 3:
                    shipsLeft = True
            if not shipsLeft:
                self.members[0].shipsLeft = self.members[0].shipsLeft - 1 
            
            
    """ append function to choose ships in computer board """
    def shipFinder(self, player, x, y):
        self.members[player].randomOnesX.clear()
        self.members[player].randomOnesY.clear()
        count = 1
        while True: 
            if (x+count < squareNumber) and (self.members[player].binCanvas[x+count][y] == 2 or self.members[player].binCanvas[x+count][y] == 3):
                self.members[player].randomOnesX.append(x+count)
                self.members[player].randomOnesY.append(y)
                count = count +1
            else:
                count = 1
                break
        while True: 
            if (x - count >= 0) and (self.members[player].binCanvas[x-count][y] == 2 or self.members[player].binCanvas[x-count][y] == 3):
                self.members[player].randomOnesX.append(x-count)
                self.members[player].randomOnesY.append(y)
                count = count +1
            else:
                count = 1
                break
        while True: 
            if (y - count >= 0) and (self.members[player].binCanvas[x][y - count] == 2 or self.members[player].binCanvas[x][y - count] == 3):
                self.members[player].randomOnesX.append(x)
                self.members[player].randomOnesY.append(y- count)
                count = count +1
            else:
                count = 1
                break
        while True: 
            if (y+count < squareNumber) and (self.members[player].binCanvas[x][y+count] == 2 or self.members[player].binCanvas[x][y+count] == 3):
                self.members[player].randomOnesX.append(x)
                self.members[player].randomOnesY.append(y+count)
                count = count +1
            else:
                break
        self.members[player].randomOnesX.append(x)
        self.members[player].randomOnesY.append(y)

    def pick(self, event):
        self.members[1].randomOnesX.clear()
        self.members[1].randomOnesY.clear()

        x = int(event.x/squeareWidth)
        y = int(event.y/squareHeigth)

        if self.members[1].binCanvas[x][y] == 2:
            self.tempCanvas = copy.deepcopy(self.members[1].binCanvas)
            self.shipFinder(1, x, y)
            self.pickedLength = self.pickedLength - len(self.members[1].randomOnesX)
            for i in range(len(self.members[1].randomOnesX)):
                self.members[1].binCanvas[self.members[1].randomOnesX[i]][self.members[1].randomOnesY[i]] = 0
        
        elif self.members[1].binCanvas[x][y] != 1 and self.pickedLength != 30:
            while True:
                direction = 0
                # checking whether points are placed next to each other
                if len(self.lastDrawX) == 1 and not (( self.lastDrawX[0] == x + 1 and self.lastDrawY[0] == y) or ( self.lastDrawX[0] == x - 1 and self.lastDrawY[0] == y) or ( self.lastDrawX[0] == x and self.lastDrawY[0] == y + 1) or ( self.lastDrawX[0] == x and self.lastDrawY[0] == y - 1)):
                    break
                # checking in which direction the points should be set
                if len(self.lastDrawX) > 1:
                    for i in range(len(self.lastDrawX)):
                        if self.lastDrawX[0] == self.lastDrawX[1]:
                            direction = 1
                            print("Horizontal")
                        else:
                            direction = 2
                            print("Vertical")

                if direction == 2 and not ((x + 1 == min(self.lastDrawX) and y == self.lastDrawY[self.lastDrawX.index(min(self.lastDrawX))]) or (x - 1 == max(self.lastDrawX) and y == self.lastDrawY[self.lastDrawX.index(max(self.lastDrawX))])):
                    print("Error1")
                    break
                if direction == 1 and not ((y + 1 == min(self.lastDrawY) and x == self.lastDrawX[self.lastDrawY.index(min(self.lastDrawY))]) or (y - 1 == max(self.lastDrawY) and x == self.lastDrawX[self.lastDrawY.index(max(self.lastDrawY))])):
                    print("Error2")
                    break
                
                if x + 1 <= 9 and self.members[1].binCanvas[x+1][y] == 1 and not (x + 1 == min(self.lastDrawX) and y == self.lastDrawY[self.lastDrawX.index(min(self.lastDrawX))]): 
                    break
                if x - 1 >= 0 and self.members[1].binCanvas[x-1][y] == 1 and not (x - 1 == max(self.lastDrawX) and y == self.lastDrawY[self.lastDrawX.index(max(self.lastDrawX))]): 
                    break
                if y + 1 <= 9 and self.members[1].binCanvas[x][y+1] == 1 and not (y + 1 == min(self.lastDrawY) and x == self.lastDrawX[self.lastDrawY.index(min(self.lastDrawY))]): 
                    break
                if y - 1 >= 0 and self.members[1].binCanvas[x][y-1] == 1 and not (y - 1 == max(self.lastDrawY) and x == self.lastDrawX[self.lastDrawY.index(max(self.lastDrawY))]): 
                    break

                self.members[1].binCanvas[x][y] =  3
                self.pickedLength = self.pickedLength +1
                self.lastDrawX.append(x)
                self.lastDrawY.append(y)
                break

        if self.pickedLength < 30:
            button1_text.set("Return")
            self.gameState = 3
            for t in range (squareNumber):
                for z in range (squareNumber):
                    if self.members[1].binCanvas[z][t] != 0:
                        self.members[1].binCanvas[z][t] = 1
        else:
            for t in range (squareNumber):
                for z in range (squareNumber):
                    if self.members[1].binCanvas[z][t] != 0:
                        self.members[1].binCanvas[z][t] = 2
            self.pickedDirection == 0
            self.lastDrawX.clear()
            self.lastDrawY.clear()
            button1_text.set("Shuffle")
            self.gameState = 0
        self.showFields(1)
        root.update()
    

gameBoard = GameBoard()

""" Randomize the fleet position """
def startStopper():
    if gameBoard.gameState == 3:
        gameBoard.pickedLength = 30
        gameBoard.members[1].binCanvas = copy.deepcopy(gameBoard.tempCanvas)
        gameBoard.showFields(1)
        button1_text.set("Shuffle")
        gameBoard.gameState = 0
        gameBoard.lastDrawX.clear()
        gameBoard.lastDrawY.clear()

    else:
        gameBoard.counter = [0,0]
        button1_text.set("Shuffle")
        gameBoard.gameState = 0
        gameBoard.choose(0)
        gameBoard.choose(1)
        gameBoard.showFields(0)
        gameBoard.showFields(1)
        gameBoard.turn = 0
        if gameBoard.fireMode == 0:
            gameBoard.members[0].shipsLeft = 10
            gameBoard.members[1].shipsLeft = 10
        else:
            gameBoard.members[0].shipsLeft = 6
            gameBoard.members[1].shipsLeft = 6
            gameBoard.tempTurn = 1
            gameBoard.shootsLeft = 6
            gameBoard.turn = 0
        gameBoard.play()
        gameBoard.pickedLength = 30
""" changing the number of fleets """
def fleetChanger(): #This is the Game mode modifier
    if gameBoard.gameState == 0:
        if gameBoard.fleet == 0:
            gameBoard.fleet = 1
            gameBoard.members[0].shipsLeft = 6#change of ships
            gameBoard.members[1].shipsLeft = 6#change of ships
            button4_text.set("Small Fleet")
        else:
            if gameBoard.fireMode == 1:
                gameBoard.fireMode = 0
                button3_text.set("Classic Fire-Mode")#fire mode used if selected
            gameBoard.fleet = 0
            gameBoard.members[0].shipsLeft = 10
            gameBoard.members[1].shipsLeft = 10
            button4_text.set("Big Fleet (Classic)")#10 ship game mode
        startStopper()
"""Modes of attacking mode """
def fireMode(): #Each fire mode and its functions
    print(gameBoard.fireMode, " GAMESTATE")
    if gameBoard.gameState == 0:
        if gameBoard.fireMode == 1:
            button3_text.set("Classic Fire-Mode")
            gameBoard.fireMode = 0
        else:
            button3_text.set("Chain Fire-Mode") #differentiates the fire mode based on amount of ships 
            gameBoard.fireMode = 1
            if gameBoard.fleet == 0:
                gameBoard.fleet = 1
                gameBoard.members[0].shipsLeft = 6
                gameBoard.members[1].shipsLeft = 6
                button4_text.set("Small Fleet")
                startStopper()
""" Levels of the game """        
def level():
    if gameBoard.level == 0:
        gameBoard.level = 1
        button2_text.set("Difficult-Mode")
    else:
        gameBoard.level = 0
        button2_text.set("Easy")

#MAIN MENU BUTTONS
tk.Button(root, text="Start", command=startStopper, textvariable=button1_text).grid(row = 5)
tk.Button(root, text="Rule", command=level, textvariable=button2_text).grid(row = 6)
tk.Button(root, text="Classic Fire-Mode", command=fireMode, textvariable=button3_text).grid(row = 7)
tk.Button(root, text="Big Fleet (Classical)", command=fleetChanger, textvariable=button4_text).grid(row = 8)

#IN GAME MENU BUTTONS
""" Button declaration """
button1_text.set("Shuffle")
button2_text.set("Easy")
button3_text.set("Classic Fire-Mode")
button4_text.set("Big Fleet (Classical)")


gameBoard.play()

root.mainloop()
