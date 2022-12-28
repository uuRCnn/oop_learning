from turtle import Screen
import turtle as t
import random

tony = t.Turtle()

colours = ["green", "black", "orange", "purple"]
tony.speed(30)
tony.pensize(12)

açılar = [90, 180, 270, 360]

for _ in range(200):
    tony.setheading(random.choice(açılar))
    tony.forward(24)
    tony.color(random.choice(colours))

screen = Screen()
screen.exitonclick()
