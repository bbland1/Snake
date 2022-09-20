from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.new_piece()

    # randomizes the adding of the food pieces
    def new_piece(self):
        random_x = random.randrange(-260, 260, 20)
        random_y = random.randrange(-260, 240, 20)
        self.goto(random_x, random_y)

    def reset(self):
        self.new_piece()
