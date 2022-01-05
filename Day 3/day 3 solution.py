# -*- coding: utf-8 -*-

with open("input.txt", 'r') as f:
    nums = [line for line in f.readlines()]

nums = [i.strip('\n') for i in nums]
nums_dupe1 = nums
nums_dupe2 = nums



empty = []
for i in range(len(nums[0])):
    counter = 0
    for j in range(len(nums)):
        if int(nums[j][i]) == 1:
            counter+=1
        else:
            counter-= 1
    
    if counter >0:
        empty.append(1)
    else:
        empty.append(0)
        
        
binary  = ''.join([str(i) for i in empty])
binary2 = binary.replace("1", "2").replace("0", "1").replace("2", "0")

print(int(binary,2))
print(int(binary2,2))
print(int(binary,2) * int(binary2,2))

#part 2

empty2 = []
for i in range(len(nums_dupe1[0])):
    counter = 0
    for j in range(len(nums_dupe1)):
        if int(nums_dupe1[j][i]) == 1:
            counter+=1
        else:
            counter-= 1
    if len(nums_dupe1) == 1:
        break
    if counter >= 0:
        nums_dupe1 = [x for x in nums_dupe1 if x[i] == '1']
    if counter < 0:
        nums_dupe1 = [x for x in nums_dupe1 if x[i] == '0']

print(nums_dupe1)
                
for i in range(len(nums_dupe2[0])):
    counter = 0
    for j in range(len(nums_dupe2)):
        if int(nums_dupe2[j][i]) == 1:
            counter+=1
        else:
            counter-= 1
    if len(nums_dupe2) == 1:
        break
    if counter >= 0:
        nums_dupe2 = [x for x in nums_dupe2 if x[i] == '0']
    if counter < 0:
        nums_dupe2 = [x for x in nums_dupe2 if x[i] == '1']
print(nums_dupe2)


x1 =(int(nums_dupe1[0],2))
x2 =(int(nums_dupe2[0],2))
print(x1*x2)
        
#['00100', '11110', '10110', '10111']