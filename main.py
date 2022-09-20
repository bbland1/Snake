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
game_is_on = True

screen.listen()

def game_done():
    global game_is_on
    game_is_on = False
    score.reset()
    screen.bye()


# Allows user to use the arrow buttons to move the snake the game is listening for key presses
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(game_done, "e")

# The game code
while game_is_on:
    # update the screen for the changes to show
    screen.update()
    # A small pause in the update as moves happen
    time.sleep(0.1)
    snake.move()

    # Detect when the snake "collects" the food
    if snake.head.distance(food) < 15:
        food.new_piece()
        snake.extend()
        score.add()

    # Detect the collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
        food.reset()

    # Detect the collision of the head with rest of body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
            food.new_piece()

screen.exitonclick()
