"""
Chapter 03, Excercise 07
Purpose: Use a nested-for loop to display the following pattern in row-major sequence
         xxxxx
         xxxxx
         xxxxx
         xxxxx
         xxxxx
"""

#Start from the 1st row and
for row in range (1,6):
    for col in range (1,6):
        print ("x", end="")
    print()
