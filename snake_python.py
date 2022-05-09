#imports:
import turtle
import time
import random

#Delay:
delay = 0.1

#Score:
score = 0
highscore = 0

#Screen:
s = turtle.Screen()
s.setup(650,650) #Size
s.bgcolor('gray') #Color
s.title('Snake_proyect') #Title

#Snake
snake = turtle.Turtle()
snake.speed(1) #Snake Speed
snake.shape('square') #Snake form
snake.penup()
snake.goto(0,0) #Snake position
snake.color('green') #Snake Color
snake.direction = 'stop'

#Snake food:
food = turtle.Turtle()
food.shape('circle')
food.color('orange')
food.penup()
food.goto(0,100)

#Snake body:
body = []

#Scoreboard:
scoreboard_text = turtle.Turtle()
scoreboard_text.speed(0)
scoreboard_text.color('black')
scoreboard_text.penup()
scoreboard_text.hideturtle()
scoreboard_text.goto(0,260)
scoreboard_text.write('Score : 0\tHighscore : 0', align='center',font=('verdana',24,'normal'))

#Directions:
def up():
	snake.direction = 'up'

def down():
	snake.direction = 'down'

def right():
	snake.direction = 'right'

def left():
	snake.direction = 'left'

def movement():
	#Up:
	if snake.direction == 'up':
		y = snake.ycor() 
		snake.sety(y + 20)
	#Down:
	if snake.direction == 'down':
		y = snake.ycor() 
		snake.sety(y - 20)
	#Right
	if snake.direction == 'right':
		x = snake.xcor() 
		snake.setx(x + 20)
	#Left
	if snake.direction == 'left':
		x = snake.xcor() 
		snake.setx(x - 20)

#Asign the keys to the directions:
s.listen()
s.onkeypress(up, "Up")
s.onkeypress(down,"Down")
s.onkeypress(right,"Right")
s.onkeypress(left,"Left")

while True:
	s.update()
	#Colition with the wall:
	if snake.xcor() > 300 or snake.xcor() < -300 or snake.ycor() > 300 or snake.ycor() < -300:
		time.sleep(2)
		for i in body:
			i.clear()
			i.hideturtle()
		snake.home()
		snake.direction = 'stop'
		body.clear()

		#Clear the score:
		score = 0
		scoreboard_text.clear()
		scoreboard_text.write('Score : {}\tHighscore : {}'.format(score,highscore),align='center',font=('verdana',24,'normal'))

	if snake.distance(food) < 20: #If the snake touh the food then:
		x = random.randint(-250,250) #Choose a value in x
		y = random.randint(-250,250) #Choose a value in y
		food.goto(x,y) #Make it appear in the screen

		#New part of body:
		new_body = turtle.Turtle()
		new_body.shape('square')
		new_body.color('green')
		new_body.speed(1)
		new_body.penup()
		new_body.goto(0,0)

		body.append(new_body)

		#score:
		score +=10
		if score > highscore: #If the score is greater than the highscore
			highscore = score #Make it the highscore
			scoreboard_text.clear() #Clear the text
			scoreboard_text.write('Score : {}\tHighscore : {}'.format(score,highscore),align='center',font=('verdana',24,'normal'))

	b_total = len(body)
	for index in range(b_total -1,0,-1):
		x = body[index-1].xcor()
		y = body[index-1].ycor()
		body[index].goto(x,y)

	if b_total > 0:
		x = snake.xcor()
		y = snake.ycor()
		body[0].goto(x,y)

	movement()
	#Colition with the body
	for i in body:
		if i.distance(snake) < 20:
			for i in body:
				i.clear()
				i.hideturtle()
			snake.home()
			snake.direction = 'stop'
			body.clear()

			#Clear the score:
			score = 0
			scoreboard_text.clear()
			scoreboard_text.write('Score : {}\tHighscore : {}'.format(score,highscore),align='center',font=('verdana',24,'normal'))

	time.sleep(delay)

turtle.done()