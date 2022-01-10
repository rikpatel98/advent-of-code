# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 11:18:29 2022

@author: rikpatel
"""
import numpy as np

with open("input.txt", 'r') as f:
    nums = [line for line in f.readlines()]
    
    
nums = [i.strip('\n') for i in nums]
empty = []
for unsplit in nums:
    
    split_coordinates = unsplit.split(' -> ')
    empty.append(split_coordinates)
    
    



x1 = []
x2 = []
y1 = []
y2 = []


for i in empty:
    x1.append(i[0].split(',')[0])
    y1.append(i[0].split(',')[1])
    x2.append(i[1].split(',')[0])
    y2.append(i[1].split(',')[1])
    
    


board = np.zeros((1000,1000))



x1_copy = []
x2_copy = []
y1_copy = []
y2_copy = []

for count in range(len(x1)):
    if x1[count] == x2[count] or y1[count] == y2[count]:
        x1_copy.append(x1[count])
        x2_copy.append(x2[count])
        y1_copy.append(y1[count])
        y2_copy.append(y2[count])
        
        
        

x1_copy = [int(x) for x in x1_copy]
x2_copy = [int(x) for x in x2_copy]
y1_copy = [int(x) for x in y1_copy]
y2_copy = [int(x) for x in y2_copy]



    
            
            
        
for count in range(len(x1_copy)):
    x_one = x1_copy[count]
    x_two = x2_copy[count]
    y_one = y1_copy[count]
    y_two = y2_copy[count]
    
    if x_one == x_two:
        board[:,x_one][min(y_one,y_two):(max(y_one,y_two)+1)] += 1
    elif y_one == y_two:
        board[y_one,:][min(x_one,x_two):(max(x_one,x_two)+1)] += 1
        
        
print((board>=2).sum())