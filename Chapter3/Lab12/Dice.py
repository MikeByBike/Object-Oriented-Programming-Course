"""
File:           Thrower.py
Authors:        Louis Lautz, Ayush Pradhan, Michalis Iona, Bogdan Neacsa
Description:    This file contains the dice class, which is responsible for rolling the dices🙀
"""

import random

class Dice():
    def roll(self, number, diceType):
        resultString = f"{diceType}, {number}"

        for i in range(number):
            resultString += f", {random.randint(1, diceType)}"
        
        return resultString
        
        

