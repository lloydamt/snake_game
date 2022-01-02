from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.color("white")
        self.score = 0
        self.display_score()


    def display_score(self):
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 3
        self.display_score()

    def game_over(self):
        self.clear()
        self.write(f"Game Over. Final score: {self.score}", align=ALIGNMENT, font=FONT)