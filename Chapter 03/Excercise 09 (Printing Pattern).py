"""
Chapter 03, Excercise 09
Purpose: Use a nested-for loop to display the following pattern in row-major sequence
         x   x
          x x
           x
          x x
         x   x
"""

#Start from the 1st row and
for row in range (1,6):
    for col in range (1,6):
        if ((row == col) or (row + col) == 6):
            print ("x", end="")
        else:
            print (" ", end="")
    print()
