'''
Project name: Space Invaders
Author: Aayush Kurup
Libraries used: turtle
Start Date: 15-08-2018
'''
import turtle
'''
Some constants
'''
player_speed = 15
enemy_speed = 2
bullet_state = 'ready'
bullet_speed = 20
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
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Space Invaders')
draw_screen()

# Player Configs
player = turtle.Turtle()
player.speed(0)
player.shape('triangle')
player.hideturtle()
player.color('blue')
player.pu()
player.left(90)
player.setpos(0,-230)
player.showturtle()

def left():
    if(player.xcor()>-180):
        x = player.xcor()
        x -= player_speed
        player.setx(x)

def right():
    if(player.xcor()<180):
        x = player.xcor()
        x += player_speed
        player.setx(x)

def fire():
    global bullet_state
    if(bullet_state == 'ready'):
        bullet_state = 'fire'
        bullet.setpos(player.xcor(),player.ycor()+10)
        bullet.showturtle()

# Keyboard Bindings
wn.onkey(left,'Left')
wn.onkey(right,'Right')
wn.onkey(fire,'space')
wn.listen()

# Enemy Config
enemy = turtle.Turtle()
enemy.hideturtle()
enemy.pu()
enemy.shape('circle')
enemy.color('red')
enemy.speed(0)
enemy.showturtle()
enemy.setpos(-180,220)
enemy.speed(1)

# bullet config
bullet = turtle.Turtle()
bullet.hideturtle()
bullet.speed(0)
bullet.pu()
bullet.setheading(90)
bullet.shape('triangle')
bullet.color('yellow')
bullet.shapesize(0.3,0.3)


while True:
    enemy.fd(enemy_speed)

    if(enemy.xcor()>180):
        y = enemy.ycor()
        y -=10
        enemy.sety(y)
        enemy_speed *= -1

    if(enemy.xcor()<-180):
        y = enemy.ycor()
        y -=10
        enemy.sety(y)
        enemy_speed *= -1

    if(bullet_state == 'fire'):
        bullet.fd(bullet_speed)

    if(bullet.ycor() == 240):
        bullet_state = 'ready'
        bullet.hideturtle()
