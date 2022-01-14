"""
generate 5 random integers and appends it to file named num.txt
"""

from random import *    #imports library random

#open the output file
outFile = open("num.txt", "a") #Append

#generate 5 numbers and write them to num.txt
for i in range(5):
    num = randint(1, 10)
    outFile.write(str(num) + "\n")

#close the output file
outFile.close()
