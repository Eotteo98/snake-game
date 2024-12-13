import turtle
import random

segments = []

screen = turtle.Screen()
screen.bgcolor("black")
snake = turtle.Turtle()
snake.shape("circle")
snake.color("red")
snake.up()
snake.goto(-20,20)

food = turtle.Turtle()
food.color("yellow")
food.shape("classic")
food.up()
food.goto(30,-100)

score = 0
highscore = 0

pen = turtle.Turtle()
pen.color("white")
pen.up()
pen.goto(0,250)
pen.hideturtle()
pen.write("Your score is ", score)

#snake movement
def move():
    if(snake.setheading == "up"):
        y = snake.ycor()
        snake.sety(y+15)
    if(snake.setheading == "down"):
        y = snake.ycor()
        snake.sety(y-15)
    if(snake.setheading == "right"):
        x = snake.xcor()
        snake.setx(x+15)
    if(snake.setheading == "left"):
        x = snake.xcor()
        snake.setx(x-15)

#linking the functions
def go_up():
    snake.setheading = "up"
def go_down():
    snake.setheading = "down"
def go_right():
    snake.setheading = "right"
def go_left():
    snake.setheading = "left"

screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_right, "d")
screen.onkey(go_left, "a")

while True:
    screen.update()
    move()
    
    if snake.distance(food)<15:
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        food.penup()
        food.goto(x,y)
        food.pendown()
    
        #body segments
        new_segment = turtle.Turtle()
        new_segment.shape("circle")
        new_segment.color("orange")
        new_segment.up()
        segments.append(new_segment)

        score += 1

        if score >highscore:
            highscore = score
        pen.clear()
        pen.write("score: {0},highscore: {1}".format(score,highscore))
    
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments [i].goto(x,y)
    
    if len(segments) >0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x,y)

    





turtle.done()
