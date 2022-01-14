"""
Chapter 03, Excercise 07
Purpose: Use a nested-for loop to display the following pattern in row-major sequence
         xxxxx
         xxxxx
         xxxxx
         xxxxx
         xxxxx
"""
row = 0
col = 0

#Start from the 1st row and
while row != 6:
    col = 0
    while col !=6:
        print ("x", end="")
        col += 1
    row += 1
    print()
