from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(snake.speed)
    screen.update()
    snake.move()

    # Cause snake to reappear on the other side of screen when it reaches end of screen

    if snake.head.xcor() > 280:
        snake.reappear_x()

    if snake.head.xcor() < -280:
        snake.reappear_neg_x()

    if snake.head.ycor() > 280:
        snake.reappear_y()

    if snake.head.ycor() < -280:
        snake.reappear_neg_y()

    # Check the distance between food and snake
    
    if snake.head.distance(food) < 20:
        scoreboard.update_score()
        snake.extend()
        food.refresh()
        snake.speed_up()

    # Check if snake collides with tail and end the game if it does
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False



screen.exitonclick()