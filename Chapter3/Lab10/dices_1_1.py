"""
File:           dices_1_1.py
Authors:        Louis Lautz, Ayush Pradhan, Michalis Iona, Bogdan Neacsa
Description:    An attempt to divide the program from Lab 9 into two files
                using a game.py file with most of the functionality in it 🙀.
"""

import random  # used for random dice rolls
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from abc import ABC, abstractmethod

from game import Game


class Dices(tk.Tk):

    # Initializer and attributes -----------------------------------
    def __init__(self, pot=100, number=2, bet=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title('Double-or-nothing')
        self.geometry('400x160')
        self.resizable(width = True, height = True)

        self.game = Game(pot, number, bet)
        
        self.createLayout()

    # Creates the main game window
    def createLayout(self):
        self.labelBet = ttk.Label(self, text="Place your bet", width = 60, anchor = tk.CENTER)
        self.labelBet.grid(row=0, column=0, sticky=tk.NSEW)
        self.game.betEntryField = ttk.Entry(self)
        self.game.betEntryField.grid(row=1, column=0, sticky=tk.NSEW)
        self.rollButton = ttk.Button(self, text="Roll the dices", command=self.prepare) #command=self.game.prepare)
        self.rollButton.grid(row=2, column=0, padx=5, pady=5)
        self.labelPot = ttk.Label(self, text="The pot starts from 100", width = 40, anchor = tk.CENTER)
        self.labelPot.grid(row=3, column=0, sticky=tk.NSEW)
        self.tennerSelect = tk.IntVar()
        self.tennerCheck = ttk.Checkbutton(self, text="Activate Tenner", variable=self.tennerSelect,
        onvalue = 1, offvalue = 0, command=self.tennerSelection)
        self.tennerCheck.grid(row=4, column=0, sticky=tk.NSEW)
        self.tennerSelection()
        self.errorLabel = ttk.Label(self, text="")
        self.errorLabel.grid(row=5, column=0, sticky=tk.NSEW)

    # Checks for the tenner rules and returns a string to check()
    def tenner(self):
        if self.game.isTenner:
            self.game.bet = self.game.bet * 10
            if self.game._Game__faces[0] + self.game._Game__faces[1] == 10:
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
            
   # Checks for possible errors in the inputs
    def prepare(self):
        result = ''
        if not self.game.betEntryField.get():
            self.errorLabel.config(text="Please input a bet into the entry field")
        elif self.game.pot <= int(self.game.betEntryField.get())*10 and self.game.isTenner:
            self.errorLabel.config(text="Your bet is too high to play Tenner. \nThe bet can't be higher than a tenth of the pot")
        else:
            self.errorLabel.config(text="")
            self.game.roll()
            result = self.game.check(self.tenner())
            
        # Checks if the game is over
        if self.game.pot > 0:
            result += f"\nYour pot is now {self.game.pot}" 
            self.labelPot.config(text=result)
            self.game.betEntryField.delete(0, tk.END)    
        else:
            if tk.messagebox.askyesno("The pot is empty!", "Do you want to play again?"):
                self.game.pot = 100
                self.createLayout()
            else:
                self.destroy()            

if __name__ == '__main__':
    Dices().mainloop()