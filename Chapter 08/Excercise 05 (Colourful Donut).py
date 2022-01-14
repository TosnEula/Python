"""
Chapter 08 Excercise 05
Purpose: Draw a colourful donut
"""

from turtle import *
from random import *

def main():
    """The main function of this program"""

    #create a turtle
    goofy = Turtle()

    #hide the turtle's body
    goofy.hideturtle()

    #set the RGB mode
    goofy.screen.colormode(255)

    #start drawing
    for i in range(18):
        #randomise the pen colour
        goofy.pencolor(randint(0,255), randint(0,255), randint(0,255))

        #draw a circle with radius of 20 pixels
        goofy.circle(20)

        #turn 20 degrees to the left
        goofy.left(20)

        #move forward 20 pixels
        goofy.forward(20)

#start the program
main()
