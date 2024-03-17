import turtle
import math
import random
wn = turtle.Screen() 
wn.bgcolor("Green")

player = turtle.Turtle() 
red_dot = turtle.Turtle()
goal = turtle.Turtle()
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(-250,250)

red_dot.penup()
red_dot.goto(x=250, y=200)
player.color("blue")
red_dot.color("red")
goal.color("yellow")
text.color("black")
red_dot.shape("circle")
goal.shape("circle")
player.shape("square") 
player.penup()
goal.penup()
goal.setposition(random.randint(-100, 100), random.randint(-100,100))
red_dot.pendown()
for i in range(4):
    red_dot.backward(500)
    red_dot.left(90)
    if i == 4:
        break
red_dot.hideturtle() 
speed = 0
score = 0

def TurnLeft():
    player.left(90)
    
def TurnRight():
    player.right(90)
    
def Forward():
    global speed
    speed = 2
    
def Backward():
    global speed
    speed = -2

turtle.listen()

turtle.onkey(TurnLeft, "Left")
turtle.onkey(TurnRight, "Right")
turtle.onkey(Forward, "Up")
turtle.onkey(Backward, "Down")

while True:
    player.forward(speed)
    
    if player.ycor() > 188 and speed == 2:
        player.right(180)
    if player.ycor() > 188 and speed == -2:
        player.right(180)
    if player.ycor() < -288 and speed == 2:
        player.right(180)
    if player.ycor() < -288 and speed == -2:
        player.right(180)
    if player.xcor() > 242 and speed == 2:
        player.right(180)
    if player.xcor() > 242 and speed == -2:
        player.right(180)
    if player.xcor() < -242 and speed == 2:
        player.right(180)
    if player.xcor() < -242 and speed == -2:
        player.right(180)
        
    d = math.sqrt(math.pow(player.xcor()-goal.xcor(),2) + math.pow(player.ycor()-goal.ycor(),2)) 
    if d < 20:
        goal.hideturtle()
        score += 1
        text.clear()
        text.write(score)
        goal.setposition(random.randint(-100,100), random.randint(-100,100))
        goal.showturtle()
        
    if score == 50:
        text.clear()
        text.goto(-20,-20)
        text.color("blue")
        text.clear()
        text.write('YOU WIN')
        break
