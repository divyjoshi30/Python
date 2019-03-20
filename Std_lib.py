import turtle
print("Modules...")
'''Turtle Modules started, gives animated functionality.'''
print("Turtle module for animation")
# noinspection PyUnresolvedReferences turned off from code>code_analysis>configure syntax>unrresolvedrefe.
# turtle.forward(150)
# turtle.right(250)
# turtle.forward(150)
# turtle.done()      #turtle stays there until we close the window, no need to use time functions.

#to import a specific function we can do his
# from turtle import forward, right    #to call multiple functions from a module
# forward(120)
# right(220)          #as we are only importing 1 function, no need to use prefix as turtle it can run on its own.
# turtle.done()       #comment the above section to make this run

from turtle import *
import time
time.sleep(3)
forward(120)
pencolor("red")
circle(50)
pencolor("blue")
circle(60)
pencolor("green")
circle(70)
pencolor("magenta")
circle(80)
pencolor("black")
forward(120)
right(180)
forward(120)
pencolor("magenta")
circle(80)
pencolor("green")
circle(70)
pencolor("blue")
circle(60)
pencolor("red")
circle(50)
print("Turtle done running")
done()
