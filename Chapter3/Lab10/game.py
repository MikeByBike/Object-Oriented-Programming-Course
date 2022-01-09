"""
File:           game.py
Authors:        Louis Lautz, Ayush Pradhan, Michalis Iona, Bogdan Neacsa
Description:
"""

import random
# import tkinter as tk
# import tkinter.ttk as ttk
# from tkinter import messagebox
# from abc import ABC, abstractmethod


class Game: #(ABC):
    def __init__(self, pot=100, number=2, bet=1):        
        self.pot = pot
        self.number = number
        self.bet = bet
        
        self.__faces = [0] * self.__number
        self.isTenner = False

    # Abstract methods so they can be used in this class
    # Implementation is in Dices Class

    # @abstractmethod
    # def tenner(self):
    #     pass

    # @abstractmethod
    # def tennerSelection(self):
    #     pass

    # @abstractmethod
    # def createLayout(self):
    #     pass
        

    # Properties ---------------------------------------------------
    @property
    def pot(self):
        return self.__pot

    @pot.setter
    def pot(self, pot):
        if pot < 0:
            self.__pot = 0
        else:
            self.__pot = pot

    @property
    def bet(self):
        return self.__bet

    @bet.setter
    def bet(self, bet):
        if bet <= 0:
            self.__bet = 1
        elif bet > self.pot:
            self.__bet = self.__pot
        else:
            self.__bet = bet

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if number < 1:
            self.number = 1
        else:
            self.__number = number

    # Methods -------------------------------------------------------

    # # Checks for possible errors in the inputs
    # def prepare(self):
    #     if not self.betEntryField.get():
    #         self.errorLabel.config(text="Please input a bet into the entry field")
    #     elif self.pot <= int(self.betEntryField.get())*10 and self.isTenner:
    #         self.errorLabel.config(text="Your bet is too high to play Tenner. \nThe bet can't be higher than a tenth of the pot")
    #     else:
    #         self.errorLabel.config(text="")
    #         self.roll()
    #         self.check(self.tenner())
    
    def roll(self):
        for i in range(self.number):
            self.__faces[i] = random.randint(1, 6)

    def check(self, tennerResult):
        self.bet = int(self.betEntryField.get())  #Takes the user input from the entry field
        
        result = tennerResult + f"{self.__faces[0]} and {self.__faces[1]} - "

        # These if-statements represent the dice result rules
        
        if self.__faces[0] == self.__faces[1]:
            #Case 1 - Both dices are equal and either 1 or 6 - receive bet ten fold
            if self.__faces[0] == 1 or self.__faces[0] == 6:
                result += f"You won {self.bet} x10!"
                self.pot += self.bet * 10
            #Case 2 - Both dices are equal and either 2, 3, 4 or 5 - receive double of the bet
            else:
                result += f"You won {self.bet} x2!"
                self.pot += self.bet * 2
        else:
            #Case 3 - The dices are not equal, but the sum of both is 6 - lose your bet
            if self.__faces[0] + self.__faces[1] == 6:
                result += f"You lost {self.bet}!"
                self.pot -= self.bet
            #Case 4 - The dices are not equal and their sum is not 6 - lose double of your bet
            else:
                result += f"You lost {self.bet} x2!"
                self.pot -= self.bet * 2
        
        return result
        # # Checks if the game is over
        # if self.pot > 0:
        #     result += f"\nYour pot is now {self.pot}" 
        #     self.labelPot.config(text=result)
        #     self.betEntryField.delete(0, tk.END)    
        # else:
        #     if tk.messagebox.askyesno("The pot is empty!", "Do you want to play again?"):
        #         self.pot = 100
        #         self.createLayout()
        #     else:
        #         self.destroy()