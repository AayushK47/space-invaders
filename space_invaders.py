'''
Project name: Space Invaders
Author: Aayush Kurup
Libraries used: turtle, math.sqrt, random.rantint
Start Date: 15-08-2018
End Date: 16-08-2018
'''

# Imports
import turtle
from math import pow,sqrt
from random import randint

# Screen Configs
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Space Invaders')
turtle.register_shape('player.gif')
turtle.register_shape('invader.gif')

# Drawing the game frame
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)
drawer.color('white')
drawer.penup()
drawer.setpos(-230,-230)
drawer.pendown()
drawer.pensize(3)
for i in range(4):
    drawer.fd(450)
    drawer.left(90)
drawer.pu()
score = 0

# Setting the scoreboard
scorekeeper = turtle.Turtle()
scorekeeper.hideturtle()
scorekeeper.speed(0)
scorekeeper.pu()
scorekeeper.color('white')
scorekeeper.setpos(-220,200)
scoreStr = 'Score: {}'.format(score)
scorekeeper.write(scoreStr,False,align='left')

# Player configs
player = turtle.Turtle()
player.color('blue')
player.shape('player.gif')
player.penup()
player.speed(0)
player.setpos(0,-210)
player.setheading(90)

playerspeed = 15


# enemy config
number_of_enemies = 5
enemies = []
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color('red')
    enemy.shape('invader.gif')
    enemy.penup()
    enemy.speed(0)
    enemy.setpos(randint(-200,180),randint(100,200))

enemyspeed = 2

# bullet config
bullet = turtle.Turtle()
bullet.shape('triangle')
bullet.color('yellow')
bullet.pu()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

'''
There will be 2 bullet states
'ready' and 'fire'
In ready state, player can fire bullets
In fire state, player has already fired a bullet and can not fire another 1
'''
bulletstate = 'ready'

# Functions

'''
The below function will be used to move the player right
'''
def move_left():
    x = player.xcor() - playerspeed
    if(x < -210):
        player.setx(-210)
    else:
        player.setx(x)

'''
The below function will be used to move the player right
'''
def move_right():
    x = player.xcor() + playerspeed
    if(x > 210):
        player.setx(200)
    else:
        player.setx(x)

'''
The below function will be used to fire the bullet
'''
def fire_bullet():
    global bulletstate
    if(bulletstate == 'ready'):
        bulletstate = 'fire'
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setpos(x,y)
        bullet.showturtle()

'''
The below function will print game over in the middle of the screen
'''
def print_game_over():
    drawer.setpos(-40,0)
    drawer.write('Game Over',False,align='left')
'''
The below function will be used to check if 2 entities(player, bullet or enemy) collide or not
'''
def isCollision(entity_1,entity_2):
    # getting the distance between the two entities using distance formula (pythagorean formula just tweeked a bit)
    distance = sqrt(pow(entity_1.xcor()-entity_2.xcor(),2)+pow(entity_1.ycor()-entity_2.ycor(),2))
    if(distance < 15):
        # if distance is less than 15, then
        return True
    else:
        # otherwise
        return False


# Keyboard Event Bindings
turtle.listen()
turtle.onkey(move_left,'Left')
turtle.onkey(move_right,'Right')
turtle.onkey(fire_bullet,'space')

# A flag to break the loop
flag = None

# Main Loop
while(True):
    for enemy in enemies:
        # Moving the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # if the enemy reaches its boundry, move down and change direction 
        if(enemy.xcor() > 210):
            for e in enemies:
                e.sety(e.ycor() - 40)
            enemyspeed *= -1

        if(enemy.xcor() < -210):
            for e in enemies:
                e.sety(e.ycor() - 40)
            enemyspeed *= -1

        # If a bullet hits the enemy, then reset the enemy position and change the score
        if(isCollision(bullet, enemy)):
            bullet.ht()
            bulletstate = 'ready'
            bullet.setpos(0,-400)
            enemy.setpos(randint(-200,180),randint(100,200))
            score += 10
            scoreStr = 'Score: {}'.format(score)
            scorekeeper.clear()
            scorekeeper.write(scoreStr,False,align='left')
            
        # if the enemy hits player, Game Over
        if(isCollision(player, enemy)):
            player.hideturtle()
            enemy.hideturtle()
            print ("Game Over")
            flag = True
            break

        # Or if the enemy reaches the surface, Game Over
        if(enemy.ycor() < -210 ):
            flag = True
            break

    # checking if we need to break the loop
    if(flag):
        print_game_over()
        break

    # Changing bullet states
    if(bulletstate == 'fire'):
        bullet.sety(bullet.ycor() + bulletspeed)

    if(bullet.ycor() > 210):
        bullet.ht()
        bulletstate = 'ready'
