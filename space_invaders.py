'''
Project name: Space Invaders
Author: Aayush Kurup
Libraries used: turtle, math.sqrt, random.rantint
Start Date: 15-08-2018
'''

import turtle
from math import sqrt
from random import randint

'''
Some constants
'''
player_speed = 15
enemy_speed = 2
bullet_state = 'ready'
bullet_speed = 20
score = 0

'''
Setting up the player and enemies icons
'''
turtle.register_shape('player.gif')
turtle.register_shape('invader.gif')

'''
The below function draws the playing screen
'''
def draw_screen():
    turtle_drawer = turtle.Turtle()
    turtle_drawer.speed(0)
    turtle_drawer.hideturtle()
    turtle_drawer.color('white')
    turtle_drawer.pu()
    turtle_drawer.setpos(-200,-250)
    turtle_drawer.pd()
    for i in range(2):
        turtle_drawer.fd(400)
        turtle_drawer.left(90)
        turtle_drawer.fd(500)
        turtle_drawer.left(90)

# Screen Configs
screen= turtle.Screen()
screen.bgcolor('black')
screen.title('Space Invaders')
draw_screen()

# Player Configs
player = turtle.Turtle()
player.speed(0)
player.shape('player.gif')
player.hideturtle()
player.color('blue')
player.pu()
player.left(90)
player.setpos(0,-230)
player.showturtle()

# Enemies config
enemies = []
for i in range(5):
    enemy = turtle.Turtle()
    enemy.hideturtle()
    enemy.pu()
    enemy.shape('invader.gif')
    enemy.color('red')
    enemy.setpos(-180,220)
    enemies.append(enemy)

for enemy in enemies:
    x = randint(-180,180)
    y = randint(150,230)
    enemy.setpos(x,y)
    enemy.showturtle()

# bullet config
bullet = turtle.Turtle()
bullet.hideturtle()
bullet.speed(0)
bullet.pu()
bullet.setheading(90)
bullet.shape('triangle')
bullet.color('yellow')
bullet.shapesize(0.3,0.3)

# Scores config
scorekeeper = turtle.Turtle()
scorekeeper.pu()
scorekeeper.color('white')
scorekeeper.hideturtle()
scorekeeper.setpos(-200,260)
scorekeeper.write('Score {}'.format(score),font=("Arial", 14, 'bold'))

'''
The below function will move the player left
'''
def left():
    if(player.xcor()>-180):
        x = player.xcor()
        x -= player_speed
        player.setx(x)

'''
The below function will move the player right
'''
def right():
    if(player.xcor()<180):
        x = player.xcor()
        x += player_speed
        player.setx(x)

'''
The below function will set the player to shoot the enemy
'''
def fire():
    global bullet_state
    if(bullet_state == 'ready'):
        bullet_state = 'fire'
        bullet.setpos(player.xcor(),player.ycor()+10)
        bullet.showturtle()

'''
The below function will check if the enemy collides with the player or not
'''
def is_colliding_player():
    # calculating the distance b/w the two objects
    x = enemy.xcor()-player.xcor()
    y = enemy.ycor()-player.ycor()
    x = x**2
    y = y**2
    if(sqrt(x+y)<=20):          # if distance <= 20 , Then
        return True
    else:
        return False            # otherwise return False

'''
The below function will check if the enemy collides with the bullet or not
'''
def is_colliding_bullet():
    # calculating the distance b/w the two objects
    x = enemy.xcor()-bullet.xcor()
    y = enemy.ycor()-bullet.ycor()
    x = x**2
    y = y**2
    if(sqrt(x+y)<30):       # if distance <= 30 , Then
        return True
    else:
        return False        # otherwise return False

'''
The below function will update the score
'''
def update_score():
    scorekeeper.undo()
    scorekeeper.write('Score {}'.format(score),font=("Arial", 14, 'bold'))

# Keyboard Bindings
screen.onkey(left,'Left')
screen.onkey(right,'Right')
screen.onkey(fire,'space')
screen.listen()

# Main Loop
while True:
    for enemy in enemies:
        enemy.fd(enemy_speed)

        if(enemy.xcor()>180):
            for e in enemies:
                y = e.ycor()
                y -=10
                e.sety(y)
                enemy_speed *= -1

        if(enemy.xcor()<-180):
            for e in enemies:
                y = e.ycor()
                y -=10
                e.sety(y)
                enemy_speed *= -1

        if(bullet_state == 'fire'):
            bullet.fd(bullet_speed)

        if(bullet.ycor() == 240):
            bullet_state = 'ready'
            bullet.hideturtle()

        if(is_colliding_player()):
            break

        if(is_colliding_bullet()):
            enemy.hideturtle()
            x = randint(-180,180)
            y = randint(150,230)
            enemy.setpos(x,y)
            enemy.showturtle()
            score +=10
            update_score()

screen.exitonclick()
