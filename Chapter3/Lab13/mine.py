"""
File:           mine.py
Author:         Michalis Iona
Description:    logic to MiniMine game
"""
from random import randint





class Mine:
    def __init__(self, slots=10, mines=10):
        self.slots = slots #10x10
        self.mines = mines
        self.points = 0 #every mineless slot adds 100 points
        self.minet = set() #accepts only unique values
        self.mineinfo = [0]*self.slots * self.slots #each slot sees its own and surrounding mines
        self.buttonStates = [1]*self.slots * self.slots #1 when the button is enables and 0 if disabled
        self.buttonLabels = [""]*self.slots * self.slots #saves the text displayed on each button





    def sow(self):        
        '''count own ond surrouding mines'''
        while len(self.minet) < self.mines:
            val = randint(0, self.slots * self.slots - 1)
            if val not in self.minet:
                self.minet.add(val) #new mines
                self.mineinfo[val] += 1
                if val % self.slots > 0:
                    self.mineinfo[val - 1] += 1 #left
                if val % self.slots < self.slots - 1:
                    self.mineinfo[val + 1] += 1 #right
                if val // self.slots > 0:
                    self.mineinfo[val - self.slots] += 1 #up
                if val // self.slots < self.slots - 1:
                    self.mineinfo[val + self.slots] += 1 #down
                if val % self.slots > 0 and val // self.slots > 0:
                    self.mineinfo[val - self.slots - 1] += 1 #up and left
                if val % self.slots > 0 and val // self.slots < self.slots - 1:
                    self.mineinfo[val + self.slots - 1] += 1 #down and left
                if val % self.slots <  self.slots - 1 and val // self.slots > 0:
                    self.mineinfo[val - self.slots + 1] += 1 #up and right
                if val % self.slots < self.slots - 1 and val // self.slots < self.slots - 1:
                    self.mineinfo[val + self.slots + 1] += 1 #down and right                 
    
    
    
    def newGame(self):
        self.minet.clear()
        self.mineinfo = [0]*self.slots * self.slots
        self.buttonStates = [1]*self.slots * self.slots
        self.buttonLabels = [""]*self.slots * self.slots
        self.points = 0
        self.sow()
     
        
     
    def isReady(self):
        '''(slots - mines)*100 (per point)'''
        return self.points == (self.slots * self.slots - self.mines) * 100
