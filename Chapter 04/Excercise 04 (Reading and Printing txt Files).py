"""
Chapter 4, Excercise 4
Purpose: Read in the contents from an input file called in.txt
        and display the contents on the screen
"""

#Open the input file
inFile = open("in.txt", 'r') #Does not need to be clsed as it is being read


#Read in the contents
contents = inFile.readline()


#display the contents
print (contents, end="")
