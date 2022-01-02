from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        snake.reappear_x()

    if snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reappear_y()


screen.exitonclick()