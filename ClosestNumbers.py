import math 
import os 
import random 
import re 
import sys 

# Complete the closestNumbers function below. 
n = input() 
numbers = list(map(int,input().strip().split())) numbers.sort() 
lowestDiff = numbers[1]-numbers[0] 
result = [numbers[0],numbers[1]] 
for i in range(1,len(numbers)-1): 
if numbers[i+1]-numbers[i] < lowestDiff: result = [] 
result.append(numbers[i]) 
result.append(numbers[i+1]) 
lowestDiff = abs(numbers[i+1]-numbers[i]) elif numbers[i+1]-numbers[i] == lowestDiff: result.append(numbers[i]) 
result.append(numbers[i+1]) 
print(*result)


