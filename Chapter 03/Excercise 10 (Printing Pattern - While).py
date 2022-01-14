"""
Chapter 03, Excercise 10
Purpose: Use a nested-while loop to display the following pattern in row-major sequence
         x   x
          x x
           x
          x x
         x   x
"""
row = 1
col = 1

while row <6:
    col = 1
    while col<6:
        if ((row == col) or (row + col) == 6):
            print ("x", end="")
        else:
            print (" ", end="")
        col += 1
    row+=1
    print()
