"""
Chapter 07, Excercise 03
Purpose: Taking a random walk
"""

from turtle import *
from random import *


def randomWalk(t, turns=30, distance = 60):
    """walk randomly"""
    #using the true color system
    t.screen.colormode(255)
    
    
    for count in range(turns):
        #turn randomly
        t.setheading(randint(0,360)) 

        #Changes the colour of the pen each turn
        t.pencolor(randint(0,255), randint(0,255), randint(0,255))

        #move forward a random distance
        t.forward(randint(60,100))

randomWalk(Turtle())
