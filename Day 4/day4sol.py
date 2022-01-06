# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 15:45:23 2022

@author: rikpatel
"""
import numpy as np
numbers = [76,69,38,62,33,48,81,2,64,21,80,90,29,99,37,15,93,46,75,0,89,56,58,40,92,47,8,6,54,96,12,66,83,4,70,19,17,5,50,52,45,51,18,27,49,71,28,86,74,77,11,20,84,72,23,31,16,78,91,65,87,79,73,94,24,68,63,9,88,82,30,42,60,13,67,85,44,59,7,53,22,1,26,41,61,55,43,39,3,35,25,34,57,10,14,32,97,95,36,98
]

boards = np.genfromtxt('C:\\Users\\rikpatel\\advent-of-code\\Day 4\\input.txt', delimiter = None)
fives = np.arange(0,500,5)
array_boards = []
for i in fives:
    test = np.vstack([boards[i:i+5]])
    array_boards.append(test)
    

#print(array_boards[0])


#array_boards[0][array_boards[0] == 17] = 5
    
#print(array_boards[0][:,0])



# array_boards[0][:,0] = [ 5. 39. 87. 66. 91.]
#if ([5,39,87,66,91]) == (array_boards[0][:,0]).tolist():
    #print('hi')
    







for i in numbers:
    for j in array_boards:
        
        j[j == i] = -1
            
        for r in range(5):
            if [-1,-1,-1,-1,-1] == j[r].tolist() or [-1,-1,-1,-1,-1] == j[:,r].tolist():
                print(j)
                
                print(i)
                break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break

            
                
