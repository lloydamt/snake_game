from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

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

    if snake.head.xcor() > 280:
        snake.reappear_x()

    if snake.head.xcor() < -280:
        snake.reappear_neg_x()

    if snake.head.ycor() > 280:
        snake.reappear_y()

    if snake.head.ycor() < -280:
        snake.reappear_neg_y()
    
    if snake.head.distance(food) < 20:
        snake.extend()
        food.refresh()
        snake.speed_up()





screen.exitonclick()