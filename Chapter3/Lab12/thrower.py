"""
File:           Thrower.py
Author:         Michalis Iona
Description:    A program that lets the user select the dice type and number of dices.
                The result is shown in the window and saved in a file.
"""

import tkinter as tk
import tkinter.ttk as ttk

from tkinter import messagebox
from abc import ABC, abstractmethod
from Dice import Dice
from FileHandler import ReadWrite

class Thrower(tk.Tk):

    # Initializer and attributes
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Dice Roller')
        self.geometry('400x160')
        self.resizable(width = True, height = True)

        self.dices = Dice()

        try:
            print("Reading file")
            readString = ReadWrite().read('lab12_savefile.txt')
            self.lastThrow = f"Last throw: {self.formatString(readString)}"
        except:
            print("No savefile found")
            self.lastThrow = ""
        self.createLayout()


    def createLayout(self):
        self.titleLabel = ttk.Label(self, text="Select your dices and give 'em a roll!",\
             width = 35, anchor = tk.CENTER)
        self.titleLabel.grid(row=0, column=0, sticky=tk.NSEW)

        self.throwsLabel = ttk.Label(self, text=f"{self.lastThrow}", width = 20, anchor = tk.CENTER)
        self.throwsLabel.grid(row=1, column=0, sticky=tk.NSEW)

        self.firstLabel = ttk.Label(self, text="Number of Dices:", width=16)
        self.firstLabel.grid(row=2, column=0, sticky=tk.NSEW)

        self.diceAmountChoice = tk.IntVar(self)
        self.diceAmountChoice.set(1)
        self.diceAmountChoiceList = (0, 1, 2, 3, 4, 5)
        self.diceAmountDropdown = ttk.OptionMenu(self, self.diceAmountChoice, *self.diceAmountChoiceList)
        self.diceAmountDropdown.grid(row=2, column=2, sticky=tk.NSEW)

        self.firstLabel = ttk.Label(self, text="Sides of Dices:", width=16)
        self.firstLabel.grid(row=3, column=0, sticky=tk.NSEW)

        self.diceTypeChoice = tk.IntVar(self)
        self.diceTypeChoiceList = (0, 4, 6, 10, 12, 20)
        self.diceTypeChoice.set(4)
        self.diceTypeDropdown = ttk.OptionMenu(self, self.diceTypeChoice, *self.diceTypeChoiceList)
        self.diceTypeDropdown.grid(row=3, column=2, sticky=tk.NSEW)

        self.rollButton = ttk.Button(self, text="ROLL!", command=self.callRoll)
        self.rollButton.grid(row=4, column=1, sticky=tk.NS)


    # Is called when the button is pressed
    def callRoll(self):
        resultString = self.dices.roll(self.diceAmountChoice.get(), self.diceTypeChoice.get())

        # save into savefile
        ReadWrite().write("lab12_savefile.txt", resultString)

        self.throwsLabel.configure(text=f"Last throw: {self.formatString(resultString)}")


    # Formats the string in the format from the save file, to the format of the tk window
    def formatString(self, message):
        resultStringList = message.split(", ")
        resultString = ""
        for i in range(len(resultStringList)-2):
            resultString += f"{str(resultStringList[i+2])}, "
        # removes the last space and , from the string
        return resultString[0:-2]



if __name__ == '__main__':
    Thrower().mainloop()

