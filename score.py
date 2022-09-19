from tkinter import font
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False,
                   align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(
            f"GAME OVER\nFinal Score: {self.score}", False, align=ALIGNMENT, font=FONT)
