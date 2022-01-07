# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 15:45:23 2022

@author: rikpatel
"""
import numpy as np


nums = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

# boards = np.genfromtxt('C:\\Users\\rikpatel\\advent-of-code\\Day 4\\input.txt', delimiter = None)
example = np.genfromtxt('Day 4/example.txt', delimiter = None)
fifteen = np.arange(0,15,5)

fives = np.arange(0,500,5)
# array_boards = []
# for i in fives:
#     test = np.vstack([boards[i:i+5]])
#     array_boards.append(test)
    
boards = []
for i in fifteen:
    board = np.vstack([example[i:i+5]])
    boards.append(board)



# for board in boards:
#     print(board)
#     print()

################################# part 2

print("nums: ", nums)

for num in nums:
    print("Number:", num)
    for idx, board in enumerate(boards):

        board[board == num] = -1
        
        for r in range(5):
            if [-1,-1,-1,-1,-1] == board[r].tolist() or [-1,-1,-1,-1,-1] == board[:,r].tolist():
                print("This Board had Bingo (below): ")
                boards.pop(idx)
        
        print(board)
        print()


        if len(boards) == 0:
            print("done")
            print(board)
            print(num)
            break
        else:
            continue
        break
    else:
        continue
    break
                
        

    


 


            
                
