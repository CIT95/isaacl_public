#For my dev_0 I planned on using lists to hold data used for generating a certain result. For example, a list containing the outcome of 100 coin flips
#My attempt at implmenting lists for this task

import random

#create an empty list for the results of the coin flips to be placed in
set = []

#asks user to input number of coin flips
print('Please enter the number of coin flips')
while True:
    try: 
        numberOfFlips = int(input())
        break
    except ValueError as e:
        print(e)
        continue

#for loop to flip as many times as the user stated
for x in range(numberOfFlips):
    value = random.randint(0,1)
    if value == 0:
        set.append(1) #heads
    else:
        set.append(0) #tails

#displays number of flips, heads, and tails.
print('In your '+str(numberOfFlips)+' flips. You received '+str(set.count(1))+ ' heads and '+str(set.count(0))+' tails.')
    
