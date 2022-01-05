# -*- coding: utf-8 -*-

with open("input.txt", 'r') as f:
    nums = [line for line in f.readlines()]

nums = [i.strip('\n') for i in nums]


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