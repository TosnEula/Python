"""
Fall 2021 , COP 2034.01, Introduction to Programming Using Python
Assignment 02, Excercise 01
Student Name: Dominique Shim
Purpose: Prints the given pattern using nested for loops:
         0000000x
         000000xx
         00000xxx
         0000xxxx
         000xxxxx
         00xxxxxx
         0xxxxxxx
         xxxxxxxx
"""


for x in range(1,8):                            #outer for loop to make each line
    for y in range(0,7):                        #inner for loop to print each value in the line
        if y < 7-x:                             #Should the inner for loop be less that 7 minus the value of x, '0' will be printed
            print ("0", end="")
        else:
            print ("x", end="")                 #else print 'x'
    print()                                     #once the inner loop is finished break line
    
