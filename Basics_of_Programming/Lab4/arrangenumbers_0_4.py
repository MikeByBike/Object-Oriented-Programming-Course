"""
Lab 4 - arrangenumbers_0_4.py
Description - Update 4: 8-puzzle arrangement game with an inversion counter and a randomized number order.
@author - Michalis Iona

"""
import random

def isReady(numbers, check):
    return numbers == list(check)


def move(numbers):
    while True:  # if a user inputs something wrong, the program doesnt stop
        try:
            number_input = input("What number you want to swap: ")
            input_index = numbers.index(number_input)     # find index of input
            empty_index = numbers.index("_")             # find index of _
            numbers[input_index], numbers[empty_index] = numbers[empty_index], numbers[input_index]
            break
        except:
            print("Type a number between 1 and 8.")
            
def isSolvable(numbers):
    inversions = 0
    for i in range(9):
        for j in range(1, 9):
            if numbers[i] != '' and numbers[j] != '' and numbers[i] > numbers[j]:
                inversions += 1
    return inversions % 2 == 0

def shuffle(numbers):
    for i in range(random.randint(4, 12)):
        first = random.randint(0, 8)
        second = random.randint(0, 8)
        numbers[first], numbers[second] = numbers[second], numbers[first]

def printBoard(numbers):
    list_index = 0
    for i in range(3):
        for j in range(3):
            if (j + 1) % 3 == 0:
                print(numbers[list_index], end='\n')
            else:
                print(numbers[list_index], sep=' ', end=' ')
            list_index += 1

def create():
    createdlist = []
    for i in range(1, 9):
        createdlist.append(str(i))
    createdlist.append('_')
    return createdlist

def main():
    # create a list of numbers, shuffle the order and add an empty string to the end
    numbers = create()
    check = tuple(numbers)
    # preparation loop
    while True:
        shuffle(numbers)
        if isSolvable(numbers):
            break
    print('8 puzzle - arrange the numbers by swapping them with the empty place')
    # the main loop
    while True:
        printBoard(numbers)
        if isReady(numbers, check):
            print('Good work!')
            break
        else:
            move(numbers)

if __name__ == '__main__':
    main()