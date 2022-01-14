"""
Chapter 05, Excercise 05
Purpose: Use a dictonary to convert a hexidecimal number into its equivalent binary number.
"""

def main():
    """The main function of the program"""

    #Prompt for hexidecimal number
    hexNum = input("Please input a hexidecimal number: ")

    #Convert the number into binary format
    binNum = convert(hexNum)

    #Display the number on the screen
    print("The hexidecimal number", hexNum, " in binary format is", binNum)

def convert(hexidecimal):

    #the mapping between hexidecimal digits and binary digits
    mapTable = {"0":"0000", "1":"0001", "2":"0010","3":"0011",
                "4":"0100", "5":"0101", "6":"0110","7":"0111",
                "8":"1000", "9":"1001", "A":"1010","B":"1011",
                "C":"1100", "D":"1101", "E":"1110","F":"1111"}
    
    #Build the corresponding binary number
    binary = ""

    for dig in hexidecimal:
        binary += mapTable[dig]

    return binary

main()
