import time
from food import Food
from snake import Snake
from turtle import Screen
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Grow the Snake")
screen.tracer(0)

turks = Snake()
food = Food()
score = Scoreboard()

screen.listen()

screen.onkey(turks.up, "Up")
screen.onkey(turks.down, "Down")
screen.onkey(turks.left, "Left")
screen.onkey(turks.right, "Right")

game_is_active = True
while game_is_active:
    screen.update()
    time.sleep(0.1)
    turks.move()

    if turks.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        turks.extent()

    if (turks.head.xcor() > 280 or turks.head.xcor() < -280 or
            turks.head.ycor() > 280 or turks.head.ycor() < -280):
        score.reset_score()
        turks.reset_snake()

    for turk in turks.turks[1:]:
        if turks.head.distance(turk) < 10:
            score.reset_score()
            turks.reset_snake()

screen.exitonclick()
