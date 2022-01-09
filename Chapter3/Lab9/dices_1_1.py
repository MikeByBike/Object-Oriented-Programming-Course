"""
File:           dices_1_1.py
Authors:        Louis Lautz, Ayush Pradhan, Michalis Iona, Bogdan Neacsa
Description:    A better version of the dice game from lab 6. This version uses
                the tkinter module to make the program more visually appealing.
                It also contains a tenner gamemode that can be toggled.
"""

import random  # used for random dice rolls
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


class Dices(tk.Tk):

    # Initializer and attributes -----------------------------------
    def __init__(self, pot, number=2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title('Double-or-nothing')
        self.geometry('400x160')
        self.resizable(width = True, height = True)

        self.__pot = pot
        self.__bet = 1  # default value is 1, so the while loop in main doesnt stop right away
        self.__number = number  # default value is 2, but can be changed
        self.__faces = [0] * self.__number
        self.isTenner = False

        self.__createLayout()

    def __createLayout(self):
        self.labelBet = ttk.Label(self, text="Place your bet", width = 60, anchor = tk.CENTER)
        self.labelBet.grid(row=0, column=0, sticky=tk.NSEW)
        self.betEntryField = ttk.Entry(self)
        self.betEntryField.grid(row=1, column=0, sticky=tk.NSEW)
        self.rollButton = ttk.Button(self, text="Roll the dices", command=self.prepare)
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
    def prepare(self):
        if not self.betEntryField.get():
            self.errorLabel.config(text="Please input a bet into the entry field")
        elif self.pot <= int(self.betEntryField.get())*10 and self.isTenner:
            self.errorLabel.config(text="Your bet is too high to play Tenner. \nThe bet can't be higher than a tenth of the pot")
        else:
            self.errorLabel.config(text="")
            self.roll()
            self.check(self.tenner())
    
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
        
        # Checks if the game is over
        if self.pot > 0:
            result += f"\nYour pot is now {self.pot}" 
            self.labelPot.config(text=result)
            self.betEntryField.delete(0, tk.END)    
        else:
            if tk.messagebox.askyesno("The pot is empty!", "Do you want to play again?"):
                self.pot = 100
                self.__createLayout()
            else:
                self.destroy()

    def tenner(self):
        if self.isTenner:
            self.bet = self.bet * 10
            if self.__faces[0] + self.__faces[1] == 10:
                self.pot += self.bet * 10
                return f"You won {self.bet * 10} in Tenner!\n"
            else:
                self.pot -= self.bet
                return f"You lost {self.bet} in Tenner.\n"
        else:
            return ""

    def tennerSelection(self):
        if self.tennerSelect.get():
            self.isTenner = True
        else:
            self.isTenner = False


if __name__ == '__main__':
    Dices(100).mainloop()