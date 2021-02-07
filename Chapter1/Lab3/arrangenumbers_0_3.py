"""
Lab 3 - arrangenumbers_0_3.py
Description - Update 3: 8-puzzle arrangement game with an inversion counter and a randomized number order.
@author - Michalis Iona

"""
import random

#numbers list is shuffled
def Shuffle():
    for i in range(random.randint(2, 10)):
        first_random = random.randint(0, 8)
        second_random = random.randint(0, 8)
        while first_random == second_random:  # This prevents swapping
            second_random = random.randint(0, 8)
        Swap(first_random, second_random)
        
#swapping numbers
def Swap(first, second):
    numbers[first], numbers[second] = numbers[second], numbers[first]

#numbers list inversions are calculated
def InversionCounter():
    inversion = 0
    for i in range(9):
        for j in range(1, 9):
            if numbers[i] != '' and numbers[i] != '' and numbers[i] > numbers[j]:
                inversion += 1
    return inversion

#numbers are printed in 3*3 board
def Pattern(list):
    list_index = 0
    for i in range(3):
        for j in range(3):
            if (j + 1) % 3 == 0:
                print(list[list_index], end='\n')
            else:
                print(list[list_index], sep=' ', end=' ')
            list_index += 1
    print('')
    
#preparation loop breaks when numbers list is solvable
def Solvable():
    if InversionCounter() % 2 != 0:
        Pattern(numbers)
        print("The current combination is unsolvable. Shuffling again.\n")
        Shuffle()
        Solvable()
    else:
        print("Good luck!!\n")
        Pattern(numbers)
        
#intro
print('8 puzzle - arrange the numbers by swapping them with the empty place')
check = ('1','2','3','4','5','6','7','8','_')
numbers = ['4','7','2','6','8','3','5','_','1']
print('correct order: ', check)
Pattern(check)
Shuffle()
Solvable()
rounds = 1

#rounds
while numbers != list(check):
    wrong_input = True
    while wrong_input:  # false user inputs
        try:
            user_input = input(f"Round {rounds} | number to move: ")
            input_index = numbers.index(user_input)  # index of user input
            nothing_index = numbers.index("_")  # index of empty (_)
            Swap(input_index, nothing_index)
            Pattern(numbers)
            wrong_input = False
            rounds += 1
        except:
            print("Type a number between 1 and 8.")


#output in certain rounds
print(f"Congrats it took you {rounds} rounds!")
if rounds <= 8:
    print("You almost made it.")
elif rounds <= 10 and rounds > 8:
    print("You are average.")
elif rounds <= 13 and rounds > 10:
    print("You barely made it")
else:
    print("Game Over")
