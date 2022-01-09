"""
File:           dices_1_1.py
Authors:        Louis Lautz, Ayush Pradhan, Michalis Iona, Bogdan Neacsa
Description:    A betting game where you can make a bet and roll dices.
                Based on the dices you either lose money or gain money 🙀.
"""

import random  # used for random dice rolls
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from abc import ABC, abstractmethod
from filehandler import ReadWrite
from pathlib import Path # Used to check if the save file already exists
import os

from game import Game


class Tenner(ABC):
    @abstractmethod
    def tenner(self): pass    


class Dices(Tenner, tk.Tk):

    # Initializer and attributes -----------------------------------
    def __init__(self, pot=100, number=2, bet=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title('Double-or-nothing')
        self.geometry('400x160')
        self.resizable(width = True, height = True)

        print(pot)
        self.game = Game(pot, number, bet)
        
        self.createLayout()

        # Calls close() when you press the red X to close the window
        self.protocol("WM_DELETE_WINDOW", self.close)

    # Creates the main game window
    def createLayout(self):
        self.labelBet = ttk.Label(self, text="Place your bet", width = 60, anchor = tk.CENTER)
        self.labelBet.grid(row=0, column=0, sticky=tk.NSEW)
        self.betEntryField = ttk.Entry(self)
        self.betEntryField.grid(row=1, column=0, sticky=tk.NSEW)
        self.rollButton = ttk.Button(self, text="Roll the dices", command=self.prepare)
        self.rollButton.grid(row=2, column=0, padx=5, pady=5)
        self.labelPot = ttk.Label(self, text=f"The pot starts from {self.game.pot}", width = 40, anchor = tk.CENTER)
        self.labelPot.grid(row=3, column=0, sticky=tk.NSEW)
        self.tennerSelect = tk.IntVar()
        self.tennerCheck = ttk.Checkbutton(self, text="Activate Tenner", variable=self.tennerSelect,
        onvalue = 1, offvalue = 0, command=self.tennerSelection)
        self.tennerCheck.grid(row=4, column=0, sticky=tk.NSEW)
        self.tennerSelection()
        self.errorLabel = ttk.Label(self, text="")
        self.errorLabel.grid(row=5, column=0, sticky=tk.NSEW)

    # Is called whenever you are trying to close the window
    def close(self):
        '''
        called when the window closing cross is selected
        asks if user wants to save first 
        yes = true, no = false, cancel = None
        '''
        answer = tk.messagebox.askyesnocancel("Do you want to save before closing?")
        if answer:
            # Saves the current pot value in the savefile
            ReadWrite().write('D:/savefile.txt', str(self.game.pot))
            self.destroy()
        elif answer == False:
            # Changes the value in the savefile to 100 again
            ReadWrite().write('D:/savefile.txt', '100')
            self.destroy()

    # Checks for possible errors in the inputs
    def prepare(self):
        if not self.betEntryField.get():
            self.errorLabel.config(text="Please input a bet into the entry field")
        elif self.game.pot <= int(self.betEntryField.get())*10 and self.game.isTenner:
            self.errorLabel.config(text="Your bet is too high to play Tenner. \nThe bet can't be higher than a tenth of the pot")
        else:
            self.errorLabel.config(text="")
            self.game.bet = int(self.betEntryField.get())  #Takes the user input from the entry field
            self.game.roll()
            # calls tenner function, which returns to check, which returns to the label pot
            self.labelPot.config(text=self.game.check(self.tenner()))
            self.betEntryField.delete(0, tk.END)

            # Checks if the game is over
            if self.game.pot <= 0:    
                if tk.messagebox.askyesno("The pot is empty!", "Do you want to play again?"):
                    self.game.pot = 100
                    self.createLayout()
                else:
                    self.destroy()

    # Checks for the tenner rules and returns a string to check()
    def tenner(self):
        if self.game.isTenner:
            self.game.bet = self.game.bet * 10
            if sum(self.game._Game__faces) == 10:
                self.game.pot += self.game.bet * 10
                return f"You won {self.game.bet * 10} in Tenner!\n"
            else:
                self.game.pot -= self.game.bet
                return f"You lost {self.game.bet} in Tenner.\n"
        else:
            return ""

    # Updates the tick box value in real time
    def tennerSelection(self):
        if self.tennerSelect.get():
            self.game.isTenner = True
        else:
            self.game.isTenner = False


if __name__ == '__main__':
    # reads the value in the save file
    # the path is hard coded. Either change the path or save the file exactly there.
    startingPot = int(ReadWrite().read('D:/savefile.txt'))
    
    Dices(pot = startingPot).mainloop()