"""
Lab 7 - dicestest.py
Description - Testing Dices program.
@author - Michalis Iona

"""
# Importing Dices
from dices_0_1.py import Dices

# creating class test
class DicesTest:
    
    # Big Pairs Test
    @staticmethod
    def testBigPairs()():
        dices = Dices()   
        big = [[1,1],[6,6]]
        startingpot = dices.pot
        for pair in big:
            dices.__Dices__number = pair
            dices.correction()
            dices.bet = 1
        endingpot = dices.pot
        return (endingpot - startingpot) == 2*10 

    # Small Pairs Test    
    @staticmethod
    def testSmallPairs():
        dices = Dices()
        i = 2
        small = []
        while i <= 5:
            small.append([i,i])
            i += 1
            
        startingpot = dices.pot
        for pair in small:
            dices.__Dices_number = pair
            dices.correction()
            dices.pot = 1
        endingpot = dices.pot
        return (startingpot - endingpot) == 4*2 

    # Sum Test        
    @staticmethod 
    def testSum():
        dices = Dices()
        startingpot = dices.pot
        Sum = []
        for i in range(1,7):
            for j in range(1,7):
                if i + j == 6 and i != 3:
                    Sum.append([i, j])
        
        for pair in Sum:
            dices.__Dices_number = pair
            dices.correction()
            dices.bet = 1
        endingpot = dices.pot
        return (startingpot - endingpot) == 0  
    # Losses Test        
    @staticmethod
    def testLosses():
        dices = Dices()
        startingpot = dices.pot
        Sum = []
        for i in range(1, 7):
            for j in range(1, 7):
                if i + j != 6 and i != 3:
                    Sum.append([i, j])
                    
        for pair in Sum:
            dices.__Dices_number = pair
            dices.correction()
            dices.bet = 1
        endingpot = dices.pot
        return (startingpot - endingpot) == 4*4*2 + 2*5*2 
    
if __name__ == '__main__' :
    print(f'Big pairs (1,1 ja 6,6) test is passed is: {DicesTest.testBigPairs()}')
    print(f'Small pairs (2,2 3,3 4,4 5,5) test passed: {DicesTest.testSmallPairs()}')
    print(f'Small losses test is passed: {DicesTest.testSum()}')
    print(f'Big losses test is passed: {DicesTest.testLosses()}')