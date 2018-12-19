import turtle
import math
import random


def my_missile_spawn(x,y):
    my_missile = turtle.Turtle(visible  = False)
    my_missile.color('white')
    my_missile.penup()
    my_missile.setpos(x = BASE_X , y = BASE_Y)
    my_missile.pendown()
    alpha = my_missile.towards(x , y)
    my_missile.setheading(alpha)
    my_missile.showturtle()
    this_missile = {'missile': my_missile ,
                    'target': [x,y],
                    'status': 'launched',
                    'radius': 0}
    my_missiles_data.append(this_missile)

def enemy_missile_spawn():
    enemy_missile = turtle.Turtle(visible = False)
    enemy_missile.color('red')
    enemy_missile.penup()
    x = random.randint(-550,550)
    y = 400
    enemy_missile.setpos(x = x , y = y)
    alpha = enemy_missile.towards(BASE_X ,BASE_Y)
    enemy_missile.setheading(alpha)
    enemy_missile.pendown()
    enemy_missile.showturtle()
    this_missile = {'missile': enemy_missile,
                    'target': [BASE_X, BASE_Y],
                    'status': 'launched',
                    'radius': 0}
    enemy_missiles_data.append(this_missile)

def flight_of_missile(data):
    for info in data:
        missile = info['missile']
        status = info['status']
        if status == 'launched':
            missile.forward(4)
            target = info['target']
            if missile.distance(x=target[0], y=target[1]) < 10:
                info['status'] = 'explode'
                missile.shape('circle')
        elif status == 'explode':
            info['radius'] += 1
            if info['radius'] > 5:
                missile.clear()
                missile.hideturtle()
                data.remove(info)
            else:
                missile.shapesize(info['radius'])

def missile_contact():
    for my_info in my_missiles_data:
        my_missile = my_info['missile']
        for enemy_info in enemy_missiles_data:
            enemy_missile = enemy_info['missile']
            if enemy_missile.distance(my_missile.xcor(), my_missile.ycor()) <10:
                enemy_missile.clear()
                enemy_missile.hideturtle()
                enemy_missiles_data.remove(enemy_info)
                my_info['status'] = 'explode'
                my_missile.shape('circle')

def base_health():
    global base_hp
    for enemy_info in enemy_missiles_data:
        status = enemy_info['status']
        if status == 'explode':
            base_hp -= 100

def game_over():
    global base_hp , game_over_constant
    if base_hp <= 0 and game_over_constant  == 0:
        base.clear()
        base.hideturtle()
        game_over_write = turtle.Turtle()
        game_over_write.write("GAME OVER", True, align="center" ,font=("Arial", 100, "normal"))
        game_over_constant = 1



'Constant and database'
my_missiles_data =[]
enemy_missiles_data = []
BASE_X , BASE_Y = 0 , -350
enemy_spawn_detector = 0
base_hp = 100
game_over_constant = 0

'Window settings'
window = turtle.Screen()
window.setup(1200 + 3, 800 + 3)
window.screensize(1200, 800)
background = "image/images/background.png"
window.bgpic(background)
window.onclick(my_missile_spawn)

'All base'
base = turtle.Turtle(visible = False)
base.penup()
base.setpos(BASE_X , BASE_Y)
window.register_shape('image/images/base.gif')
base.shape('image/images/base.gif')
base.showturtle()

while True:
    window.update()
    enemy_spawn_detector += 1
    if enemy_spawn_detector % 100 == 0:
        enemy_spawn_detector = 0
        enemy_missile_spawn()
    if game_over_constant  == 0:
        game_over()
        base_health()
        missile_contact()
        flight_of_missile(data = my_missiles_data)
        flight_of_missile(data = enemy_missiles_data)
    else:
        game_over()





