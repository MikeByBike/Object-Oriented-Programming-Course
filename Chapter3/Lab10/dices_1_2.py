"""
File:           dices_1_2.py
Authors:        Louis Lautz, Ayush Pradhan, Michalis Iona, Bogdan Neacsa
Description:
"""

from random import randint
from game import Game
import tkinter as tk
from tkinter import messagebox

import random
from abc import ABC, abstractmethod

class Tenner(ABC):
    @abstractmethod
    def tenner(self):
        pass    

class Dices(Tenner, tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title('Double-or-nothing')
        self.geometry('400x160')
        self.game = Game()
        self.createLayout()
        
    def main(self):
        dices = Dices()
        print(f'Double-or-nothing - The pot is {dices.pot}.')

        while True:
            bet = input('Place a bet or leave [ENTER]: ').strip()
            if len(bet) >= 1:
                try:
                    dices.bet = int(bet)
                    dices.throw()
                    print(dices.check())
                    if dices.pot<= 0:
                        print('The pot is empty!", "Do you want to play again?')
                        break
                except ValueError as error:
                    print(error)
            else:
                if dices.pot > 0:
                    print(f'You won {dices.pot}.')
                break


    

    def CreateLayout(self):
        self.Label = tk.Label(self, text="Place your bet:", width=30, anchor=tk.CENTER, wraplength=90)
        self.Label.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=10)
        entry = tk.Entry(self, width=10)
        entry.grid(row=1, column=0, padx=10, pady=10)
        entry.bind('<Return>', (lambda event: self.show(entry)))
        self.Label_2 = tk.Label(self, text=f"Starting pot is  {self.game.pot}", width=30, anchor=tk.S, wraplength=90)
        self.Label_2.grid(row=3, column=0, sticky=tk.NSEW, padx=10, pady=10)

        self.game.selectvalue = tk.IntVar()
        button = tk.Checkbutton(self, text="Tenner", variable=self.game.selectvalue, onvalue=1, offvalue=0, command=self.tenner)
        button.grid(sticky=tk.N + tk.S)
        self.tenner()

    def show(self, entry):
        self.game.bet = int(entry.get())
        self.game.throw()
        text = self.game.check()
        title = 'Result: '
        tk.messagebox.showinfo(title, text)
        self.Label_2.config(text=f'Current pot: {self.game.pot}')
        text = self.game.check()
        if self.game.pot== 0:
            title = "Place your bet: "
            text = "Starting Pot"
            msgbox = tk.messagebox.askquestion(title="Option", message="Want to play again?")
            if msgbox == 'Yes':
                self.reset()
            else:
                self.destroy()
        else:
            title = "Result: "

    def reset(self):
        self.game.pot = 100
        self.Label_2.config(text = f'Current pot: {self.game.pot}')
        self.game.selectvalue.set(0)
        self.tenner()

    def tenner(self):
        if self.game.selectvalue.get():

            self['bg']='black'
        else:
            self['bg']='red'

      

if __name__ == '__main__':
    root = Dices()
    root.mainloop()
    Game()