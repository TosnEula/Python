"""
Chapter 03, Excercise 05
Student Name: Dominique Shim
Purpose: Use a while loop to compute the following arithmetic progression:
         3 + 8 + 13 + ... + 53
"""

sum = 0 #bucket
num = 3 #starting number

#loop
while num <= 53:
    sum += num
    num +=5

print("The result is: ",sum)
