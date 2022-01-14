"""
Fall 2021 , COP 2034.01, Introduction to Programming Using Python
Assignment 04, Excercise 01
Student Name: Dominique Shim
Purpose: Prints the given pattern using nested for loops into a text file named out.txt:
     00x00
     00x00
     xxxxx
     00x00
     00x00
"""


file = open("out.txt", "w") #Define a variable named file which write to the text file "out.txt"

for x in range(0,5):
    for y in range(0,5):
        if (y==2 or x==2):
            file.write("x")#Writes x to the text file if y=2 or x=2
        else:
            file.write("0")#Writes 0 to the text file if false
    file.write("\n")#Breaks the line in the text file after the inner loop is finished

file.close()#closes the text file once done printing the pattern.
