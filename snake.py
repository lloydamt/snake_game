from turtle import Turtle
import time

STARTING_POSITION = [(0,0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.speed = 0.25

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        self.head.forward(20)

    def extend(self):
        x_pos = self.segments[-1].xcor()
        y_pos = self.segments[-1].ycor()
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        self.segments.append(new_segment)
        new_segment.goto(x_pos, y_pos)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reappear_x(self):
        y_position = self.head.ycor()
        self.head.goto(-280, y_position)
    
    def reappear_neg_x(self):
        y_position = self.head.ycor()
        self.head.goto(280, y_position)

    def reappear_y(self):
        x_position = self.head.xcor()
        self.head.goto(x_position, -280)

    def reappear_neg_y(self):
        x_position = self.head.xcor()
        self.head.goto(x_position, 280)


    def speed_up(self):
        self.speed *= 0.9
        time.sleep(self.speed)