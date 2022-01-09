"""
File:           dices_1_0.py
Author:         Michalis Iona
Description:    A better version of the dice game from lab 6. This version uses
                the tkinter module to make the program more visually appealing.
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

        self.__pot = pot
        self.__bet = 1  # default value is 1, so the while loop in main doesnt stop right away
        self.__number = number  # default value is 2, but can be changed
        self.__faces = [0] * self.__number

        self.__createLayout()

    def __createLayout(self):
        self.labelBet = ttk.Label(self, text="Place your bet")
        self.labelBet.grid(row=0, column=0, sticky=tk.NSEW)
        self.betEntryField = ttk.Entry(self)
        self.betEntryField.grid(row=1, column=0, sticky=tk.NSEW)
        self.rollButton = ttk.Button(self, text="Roll the dices", command=self.roll)
        self.rollButton.grid(row=2, column=0, sticky=tk.NSEW)
        self.labelPot = ttk.Label(self, text="The pot starts from 100")
        self.labelPot.grid(row=3, column=0, sticky=tk.NSEW)


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
        print("Test")
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
    def roll(self):
        for i in range(self.__number):
            self.__faces[i] = random.randint(1, 6)
        self.check()

    def check(self):
        self.__bet = int(self.betEntryField.get())  #Takes the user input from the entry field

        if self.__bet <= 0:
            self.__bet = 1
        elif self.__bet > self.__pot:
            self.__bet = self.__pot

        result = f"{self.__faces[0]} and {self.__faces[1]} - "

        # These if-statements represent the dice result rules
        #Case 1 - Both dices are equal and either 1 or 6 - receive bet ten fold
        if self.__faces[0] == self.__faces[1] and (self.__faces[0] == 1 or self.__faces[0] == 6):
            result += f"You won {self.__bet} x10!"
            self.__pot += self.__bet * 10
        #Case 2 - Both dices are equal and either 2, 3, 4 or 5 - receive double of the bet
        elif self.__faces[0] == self.__faces[1] and not (self.__faces[0] == 1 or self.__faces[0] == 6):
            result += f"You won {self.__bet} x2!"
            self.__pot += self.__bet * 2
        #Case 3 - The dices are not equal, but the sum of both is 6 - lose your bet
        elif self.__faces[0] != self.__faces[1] and self.__faces[0] + self.__faces[1] == 6:
            result += f"You lost {self.__bet}!"
            self.__pot -= self.__bet
        #Case 4 - The dices are not equal and their sum is not 6 - lose double of your bet
        elif self.__faces[0] != self.__faces[1]:
            result += f"You lost {self.__bet} x2!"
            self.__pot -= self.__bet * 2

        # Checks if the game is over
        if self.__pot > 0:
            result += f"\nYour pot is now {self.__pot}" 
            self.labelPot.config(text=result)
            self.betEntryField.delete(0, tk.END)    
        else:
            if tk.messagebox.askyesno("The pot is empty!", "Do you want to play again?"):
                self.__pot = 100
                self.__createLayout()
            else:
                self.destroy()


if __name__ == '__main__':
    Dices(100).mainloop()

