#!/usr/bin/python
from random import choice
import turtle

turtle.speed(0)
directions=['f','b','l','r']

def walk(distence,lenth=10):

	for x in range(distence):
		step=choice(directions)

		if step == 'f':
			edge()
			turtle.forward(lenth)

		elif step == 'b':
			turtle.left(180)
			edge()
			turtle.forward(lenth)

		elif step == 'l':
			turtle.left(90)
			edge()
			turtle.forward(lenth)

		elif step == 'r':
			turtle.right(90)
			edge()
			turtle.forward(lenth)

def edge():
	direction = turtle.heading()
	width = turtle.window_width()
	height = turtle.window_height()

	if direction == 0 and turtle.xcor() >= width/2:
		turtle.penup()
		turtle.goto(-1*turtle.xcor(), turtle.ycor())
		turtle.pendown()

	elif direction == 90 and turtle.ycor() >= height/2:
		turtle.penup()
		turtle.goto(turtle.xcor(), -1*turtle.ycor())
		turtle.pendown()

	elif direction == 180 and turtle.xcor() <= -1*width/2:
		turtle.penup()
		turtle.goto(-1*turtle.xcor(), turtle.ycor())
		turtle.pendown()

	elif direction == 270 and turtle.ycor() <= -1*height/2:
		turtle.penup()
		turtle.goto(turtle.xcor(), -1*turtle.ycor())
		turtle.pendown()

if __name__ == "__main__":
	while True:
		walk(1000)
