from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

# Setting up the initial background screen of the game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
# makes it so the screen doesn't auto update makes it so the snake will look smoother
screen.tracer(0)

# Creating the snake and food objects from the classes imported
snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()

# Allows user to use the arrow buttons to move the snake the game is listening for key presses
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# The game code

game_is_on = True

while game_is_on:
    # update the screen for the changes to show
    screen.update()
    # A small pause in the update as moves happen
    time.sleep(0.1)
    snake.auto_move()

    # Detect when the snake "collects" the food
    if snake.head.distance(food) < 15:
        food.a_new_piece()
        score.add_score()

    # Detect the collision with the wall
    if snake.head.xcor() > 280 or snake.head.ycor() < -280:
        



screen.exitonclick()
