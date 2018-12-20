import turtle
import random


'Objects coordinates'

#base
base_object = turtle.Turtle(visible=False)
BASE_X , BASE_Y = 0 , -350
base = ['image/images/base.gif','image/images/base.gif','image/images/base.gif']
base_constant = 1
base_hp = 1000
base_half_hp = base_hp // 2

#house
house_object = turtle.Turtle(visible=False)
HOUSE_X, HOUSE_Y = 250 , -350
house = ['image/images/house_1.gif','image/images/house_2.gif','image/images/house_3.gif']
house_constant = 2
house_hp = 600
house_half_hp = house_hp // 2

#kremlin
kremlin_object = turtle.Turtle(visible=False)
KREMLIN_X, KREMLIN_Y = 450 , -350
kremlin = ['image/images/kremlin_1.gif','image/images/kremlin_2.gif','image/images/kremlin_3.gif']
kremlin_constant = 3
kremlin_hp = 600
kremlin_half_hp = kremlin_hp // 2

#nuclear
nuclear_object = turtle.Turtle(visible=False)
NUCLEAR_X, NUCLEAR_Y = -250 , -350
nuclear = ['image/images/nuclear_1.gif','image/images/nuclear_2.gif','image/images/nuclear_3.gif']
nuclear_constant = 4
nuclear_hp = 600
nuclear_half_hp = nuclear_hp //2

#skyscraper
skyscraper_object = turtle.Turtle(visible=False)
SKYSCRAPER_X, SKYSCRAPER_Y = -450 , -350
skyscraper = ['image/images/skyscraper_1.gif','image/images/skyscraper_2.gif','image/images/skyscraper_3.gif']
skyscraper_constant = 5
skyscraper_hp = 600
skyscraper_half_hp = skyscraper_hp // 2


'Constant and database'
my_missiles_data =[]
enemy_missiles_data = []
all_object = []
object_name = [base_object,house_object,kremlin_object,nuclear_object,skyscraper_object,]
enemy_spawn_detector = 0
game_over_constant = 0
target_base = 0
target = [[HOUSE_X, HOUSE_Y], [KREMLIN_X, KREMLIN_Y], [NUCLEAR_X, NUCLEAR_Y], [SKYSCRAPER_X, SKYSCRAPER_Y]]


'Window settings'
window = turtle.Screen()
window.setup(1200 + 3, 800 + 3)
window.screensize(1200, 800)
background = "image/images/background.png"
window.bgpic(background)

def massive_sum(data):
    sum = 0
    for i in range(3):
        for j in range(1):
            sum += data[i][j]
    return sum

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
                    'radius': 0,
                    'explode': 0}
    my_missiles_data.append(this_missile)

def enemy_missile_spawn():
    enemy_missile = turtle.Turtle(visible = False)
    enemy_missile.color('red')
    enemy_missile.penup()
    x = random.randint(-550,550)
    y = 400
    enemy_missile.setpos(x = x , y = y)
    constant = random.randint(0, 3)
    base_target = massive_sum(target)
    if base_target == 0:
        target_missile = [BASE_X, BASE_Y]
        alpha = enemy_missile.towards(BASE_X, BASE_Y)
    else:
        while target[constant][0] == 0:
            constant = random.randint(0, 3)
        target_missile = target[constant]
        alpha = enemy_missile.towards(target[constant][0] ,target[constant][1])
    enemy_missile.setheading(alpha)
    enemy_missile.pendown()
    enemy_missile.showturtle()
    this_missile = {'missile': enemy_missile,
                    'target': target_missile,
                    'object_type': object_name[constant+1],
                    'status': 'launched',
                    'radius': 0,
                    'explode': 0}
    enemy_missiles_data.append(this_missile)

def flight_of_missile(data):
    for info in data:
        missile = info['missile']
        status = info['status']
        if status == 'launched':
            missile.forward(4)
            target = info['target']
            if missile.distance(x=target[0], y=target[1]) < 10 or missile.ycor() < -350.0:
                info['status'] = 'explode'
                missile.shape('circle')
        elif status == 'explode' :
            info['explode'] = 1
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

def destroy_object():
    global target_base
    for enemy_info in enemy_missiles_data:
        status = enemy_info['status']
        object = enemy_info['object_type']
        if status == 'explode' and enemy_info['explode'] == 0:
            for object_info in all_object:
                if object == object_info['object']:
                    objectname = object_info['object']
                    object_info['health'] -= 100
                    if object_info['health'] == object_info['half_health'] :
                        pic = object_info['picture']
                        object_status = object_info['status']
                        swap_pic = str(pic[object_status])
                        window.register_shape(swap_pic)
                        objectname.shape(swap_pic)
                        object_info['status'] += 1
                    if object_info['health'] == 0:
                        pic = object_info['picture']
                        object_status = object_info['status']
                        swap_pic = pic[object_status]
                        window.register_shape(swap_pic)
                        objectname.shape(swap_pic)
                        object_info['status'] += 1
                        constant = object_info['constant']
                        target[constant-2][0] = 0
                        target[constant - 2][1] = 0
                        all_object.remove(object_info)
                        target_base +=1

def base_health():
    for info in all_object:
        new_base = info['object']
        base_hp = info['health']
        if target_base == 4:
            for enemy_info in enemy_missiles_data:
                status = enemy_info['status']
                target = enemy_info['target']
                if status == 'explode' and target[0] == 0:
                    info['health'] -= 100
                    if base_hp == 0:
                        new_base.clear()
                        new_base.hideturtle()

def game_over():
    global game_over_constant
    for info in all_object:
        new_base = info['object']
        base_hp = info['health']
        if base_hp <= 0 and game_over_constant  == 0:
            new_base.clear()
            new_base.hideturtle()
            game_over_write = turtle.Turtle()
            game_over_write.write("GAME OVER", True, align="center" ,font=("Arial", 100, "normal"))
            game_over_constant = 1

def spawn_object(pic, objectname, x, y, constant, health, half_health):#and info
    object = objectname
    object.penup()
    object.setpos(x, y)
    window.register_shape(pic[0])
    object.shape(pic[0])
    object.showturtle()
    info = {'object': objectname,
            'constant': constant,
            'picture': pic,
            'status': 1,
            'target': [x,y],
            'health': health,
            'half_health': half_health}
    all_object.append(info)


window.tracer(n = 2)
spawn_object(pic = base, objectname = base_object, x = BASE_X, y = BASE_Y, constant = base_constant, health = base_hp, half_health = base_half_hp)
spawn_object(pic = house, objectname = house_object, x = HOUSE_X, y = HOUSE_Y, constant = house_constant, health = house_hp, half_health = house_half_hp)
spawn_object(pic = kremlin, objectname = kremlin_object, x = KREMLIN_X, y = KREMLIN_Y, constant = kremlin_constant, health = kremlin_hp, half_health = kremlin_half_hp)
spawn_object(pic = nuclear, objectname = nuclear_object, x = NUCLEAR_X, y = NUCLEAR_Y, constant = nuclear_constant, health = nuclear_hp, half_health = nuclear_half_hp)
spawn_object(pic = skyscraper, objectname = skyscraper_object, x = SKYSCRAPER_X , y = SKYSCRAPER_Y, constant = skyscraper_constant, health = skyscraper_hp, half_health = skyscraper_half_hp)
window.tracer(n = 1)
window.onclick(my_missile_spawn)


while True:
    window.update()
    enemy_spawn_detector += 1
    if enemy_spawn_detector % 100 == 0:
        enemy_spawn_detector = 0
        enemy_missile_spawn()
    if game_over_constant  == 0:
        if target_base == 4:
            base_health()
        game_over()
        destroy_object()
        missile_contact()
        flight_of_missile(data = my_missiles_data)
        flight_of_missile(data = enemy_missiles_data)
    else:
        game_over()





