from turtle import Turtle

SNAKE_START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in SNAKE_START_POSITION:
            self.add_segment(position)

    
    # add a segment to the snake
    def add_segment(self, position):
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.segments.append(snake_part)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    # creates the automatic moving of the snake  when the game opens
    def auto_move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
