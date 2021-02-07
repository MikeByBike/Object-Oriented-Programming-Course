"""
Lab 2 - arrangenumbers_0_2.py
Description - Update 2: 8-puzzle arrangement game with an inversion counter and a randomized number order.
@author - Michalis Iona

"""
#Intro
print('8 puzzle - arrange the numbers by swapping them with the empty place')
check = ('1','2','3','4','5','6','7','8','_')
numbers = ['4','7','2','6','8','3','5','_','1']
print('correct order: ', check)
print('numbers to arrange: ', numbers)

#Rounds
for i in range(8):
    user_input = input(f"{i + 1}. number to move:" )
    input_index =  numbers.index(user_input) #index of users input
    nothing_index = numbers.index('_') #index of empty
    numbers[input_index], numbers[nothing_index] = numbers[nothing_index], numbers[input_index] #indexes getting swap
    print(numbers)
                     
#Output
output = True
for i in range (len(numbers)):
    if numbers[i] != check[i]:
        output = False

#Checking that 'numbers' match with 'check'
if output:
    correct = True
else: 
    correct = False
    
print('The number are in the correct order is', correct)