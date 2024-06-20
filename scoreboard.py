from turtle import Turtle

FONT = ("Courier", 80, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.penup()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def l_score_update(self):
        self.l_score += 1
        self.update()

    def r_score_update(self):
        self.r_score += 1
        self.update()
