"""
Fall 2021 , COP 2034.01, Introduction to Programming Using Python
Assignment 05, Excercise 01
Student Name: Dominique Shim
Purpose: Prints each individual character of a word using recursion
"""


def main():
    """Main of the program"""

    #Request a word to be segmented
    word = input("Please enter a string: ")

    #Finds the length of the word and substract it by 1
    size = len(word)-1

    
    print ("The characters are: ", end="")
    #Calls the function getChar to print each charater of the inputted variable
    getChar(word, size)

def getChar(word, length):
    """Function to recursively print each character in a word"""

    #Base case, to print the first letter of the word
    if length == 0:
        x = slice(0,1)
        print(word[x]," ", end="")

    #Recursive call which decreases the length variable by one    
    else:
        getChar(word, length-1)
        #slice to get the character in a word with exception of the first letter
        x = slice(length, length+1)
        #prints the sliced section of the word 
        print(word[x]," " , end="")

#calls the main at the start of the program
main()
