"""
Lab 6 - dices_0_1.py
Description -  A class Dices that is a 2-dice double-or-nothing-dice-game played in console.
@author - Michalis Iona

"""
import random
class Dices:

    # Initializer and attributes 
    def __init__(self, pot, number=2):
        self.__pot = pot
        self.__bet = 1  # value is 1, in order for the while loop not to stop
        self.__number = number  # value can be changed
        self.__faces = [0] * self.__number

    # Properties
    @property
    def pot(self):
        return self.__pot

    @pot.setter #__pot, a positive only integer number
    def pot(self, pot):
        if pot > 0:
            self.__pot = pot
        else:
            self.__pot = 0       

    @property
    def bet(self):
        return self.__bet

    @bet.setter # __bet, a positive integer user inputs in the beginning of each round and the value can be 1...pot
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

    @number.setter #__number, by default 2, but can be set, must be bigger than 0 and else is 1
    def number(self, number):
        if number < 1:
            self.number = 1
        else:
            self.__number = number

    # Methods
    def faces(self): #__faces, a list of length number, contains the results of rolling (random numbers between 1..6)
        for i in range(self.__number):
            self.__faces[i] = random.randint(1, 6)

    def correction(self):
        if self.__number != 2:
            raise ValueError("Wrong game, double-or-nothing is a two dice game")
        result = f"{self.__faces[0]} and {self.__faces[1]} - "

        # These if-statements represent the dice result rules
        #Case 1 - If double 1 or 6 user wins the bet  ten fold (multiplied with 10)
        if self.__faces[0] == self.__faces[1] and (self.__faces[0] == 1 or self.__faces[0] == 6):
            result += f"You won {self.__bet} x10!"
            self.__pot += self.__bet * 10
        #Case 2 - If double 2, 3, 4, or 5 user wins the bet doubled (multiplied with 2)
        elif self.__faces[0] == self.__faces[1] and not (self.__faces[0] == 1 or self.__faces[0] == 6):
            result += f"You won {self.__bet} x2!"
            self.__pot += self.__bet * 2
        #Case 3 - If no double and sum equals 6, user loses the bet 
        elif self.__faces[0] != self.__faces[1] and self.__faces[0] + self.__faces[1] == 6:
            result += f"You lost {self.__bet}!"
            self.__pot -= self.__bet
        #Case 4 - If any other combination (no double, sum not 6) then user loses the doubled bet
        elif self.__faces[0] != self.__faces[1]:
            result += f"You lost {self.__bet} x2!"
            self.__pot -= self.__bet * 2
        print(result)

def main():
    dices = Dices(100)
    print(f"The game is double-or-nothing - pot is {dices.pot}.")
    while dices.pot != 0:
        while True:
            try:
                dices.bet = int(input("Place your bet or press ENTER to exit: "))
                dices.faces()
                dices.correction()
                break
            except:
                print(f"Place your bet between 1 and {dices.pot}")
        dices.pot = dices.pot # Updates the pot, so the pot doesnt get negative
        print(f"Current pot is {dices.pot}")
    print("No more bets - pot is gone!")

if __name__ == '__main__':
    main()
