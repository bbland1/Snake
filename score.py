from tkinter import font
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", False,
                   align=ALIGNMENT, font=FONT)
        self.goto(0, 260)
        self.write(f"Press the 'E' to close the game.", False,
                   align=ALIGNMENT, font=("Courier", 10, "normal"))

    def add(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w",) as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(
    #         f"GAME OVER\nFinal Score: {self.score}", False, align=ALIGNMENT, font=FONT)


