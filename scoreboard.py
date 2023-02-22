from turtle import Turtle

SCORE_ALIGN = "center"
SCORE_FONT = ("Arial", 18, "italic")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 272)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            arg=f"Score: {self.score} Highscore: {self.highscore}",
            align=SCORE_ALIGN,
            font=SCORE_FONT,
        )

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            arg="Game Over",
            align=SCORE_ALIGN,
            font=SCORE_FONT,
        )
