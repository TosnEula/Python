"""
Chapter 4, Excercise 7
Purpose: Read in the contents from an input file called in.txt
        and display the contents on the screen
"""

from os.path import * #imports library to move through the computers directory



if exists("in.txt"):        #Checks if txt file exists
    #Open the input file
    inFile = open("in.txt", 'r') #Does not need to be clsed as it is being read

    #Read in the contents
    while True:
        line = inFile.readline()
        if line == "":
            break
        else:
            print (line, end="")

else:
    print ("The file does not exist.")
