import turtle
import random


'Objects coordinates'

#base
BASE_X , BASE_Y = 0 , -350
base = ['image/images/base.gif','image/images/base.gif','image/images/base.gif']
base_constant = 1
base_hp = 1000
base_half_hp = base_hp // 2

#house
HOUSE_X, HOUSE_Y = 250 , -350
house = ['image/images/house_1.gif','image/images/house_2.gif','image/images/house_3.gif']
house_constant = 2
house_hp = 600
house_half_hp = house_hp // 2

#kremlin
KREMLIN_X, KREMLIN_Y = 450 , -350
kremlin = ['image/images/kremlin_1.gif','image/images/kremlin_2.gif','image/images/kremlin_3.gif']
kremlin_constant = 3
kremlin_hp = 600
kremlin_half_hp = kremlin_hp // 2

#nuclear
NUCLEAR_X, NUCLEAR_Y = -250 , -350
nuclear = ['image/images/nuclear_1.gif','image/images/nuclear_2.gif','image/images/nuclear_3.gif']
nuclear_constant = 4
nuclear_hp = 600
nuclear_half_hp = nuclear_hp //2

#skyscraper
SKYSCRAPER_X, SKYSCRAPER_Y = -450 , -350
skyscraper = ['image/images/skyscraper_1.gif','image/images/skyscraper_2.gif','image/images/skyscraper_3.gif']
skyscraper_constant = 5
skyscraper_hp = 600
skyscraper_half_hp = skyscraper_hp // 2


'Constant and database'
my_missiles_data =[]
enemy_missiles_data = []
all_object = []
enemy_spawn_detector = 0
game_over_constant = 0
target = [[HOUSE_X, HOUSE_Y], [KREMLIN_X, KREMLIN_Y], [NUCLEAR_X, NUCLEAR_Y], [SKYSCRAPER_X, SKYSCRAPER_Y]]


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
    constant = random.randint(0,2)
    x = random.randint(-550,550)
    y = 400
    enemy_missile.setpos(x = x , y = y)
    alpha = enemy_missile.towards(target[constant][0] ,target[constant][1])
    enemy_missile.setheading(alpha)
    enemy_missile.pendown()
    enemy_missile.showturtle()
    this_missile = {'missile': enemy_missile,
                    'target': target[constant],
                    'object_type': constant+1,
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
            if missile.distance(x=target[0], y=target[1]) < 10:
                info['status'] = 'explode'
                missile.shape('circle')
        elif status == 'explode':
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
    for enemy_info in enemy_missiles_data:
        status = enemy_info['status']
        object = enemy_info['object_type']
        if status == 'explode' and enemy_info['explode'] == 0:
            for object_info in all_object:
                if object == object_info['object']:
                    object_info['health'] -= 100
                if object_info['health'] == object_info['half_health'] :
                    pic = object_info['picture']
                    object_status = object_info['status']
                    swap_pic = str(pic[object_status])
                    print(swap_pic)
                    #
                    object.shape(swap_pic)
                    object_info['status'] += 1
                if object_info['health'] == 0:
                    pic = object_info['picture']
                    object_status = object_info['status']
                    swap_pic = pic[object_status]
                    window.register_shape(swap_pic)
                    object.shape(swap_pic)
                    object_info['status'] += 1
                    del(target[object-1])

# def game_over():
#     global base_hp , game_over_constant
#     if base_hp <= 0 and game_over_constant  == 0:
#         base.clear()
#         base.hideturtle()
#         game_over_write = turtle.Turtle()
#         game_over_write.write("GAME OVER", True, align="center" ,font=("Arial", 100, "normal"))
#         game_over_constant = 1

def spawn_object(pic, x, y, constant, health, half_health):#and info
    object = turtle.Turtle(visible=False)
    object.penup()
    object.setpos(x, y)
    window.register_shape(pic[0])
    object.shape(pic[0])
    object.showturtle()
    info = {'object': constant,
            'picture': pic,
            'status': 1,
            'target': [x,y],
            'health': health,
            'half_health': half_health}
    all_object.append(info)


'Window settings'
window = turtle.Screen()
window.setup(1200 + 3, 800 + 3)
window.screensize(1200, 800)
background = "image/images/background.png"
window.bgpic(background)
window.onclick(my_missile_spawn)
window.register_shape('image/images/house_2.gif')
window.register_shape('image/images/kremlin_2.gif')
window.register_shape('image/images/nuclear_2.gif')
window.register_shape('image/images/skyscraper_2.gif')
# window.register_shape(swap_pic)
# window.register_shape(swap_pic)
# window.register_shape(swap_pic)



window.tracer(n = 2)
spawn_object(pic = base, x = BASE_X, y = BASE_Y, constant = base_constant, health = base_hp, half_health = base_half_hp)
spawn_object(pic = house, x = HOUSE_X, y = HOUSE_Y, constant = house_constant, health = house_hp, half_health = house_half_hp)
spawn_object(pic = kremlin, x = KREMLIN_X, y = KREMLIN_Y, constant = kremlin_constant, health = kremlin_hp, half_health = kremlin_half_hp)
spawn_object(pic = nuclear, x = NUCLEAR_X, y = NUCLEAR_Y, constant = nuclear_constant, health = nuclear_hp, half_health = nuclear_half_hp)
spawn_object(pic = skyscraper, x = SKYSCRAPER_X , y = SKYSCRAPER_Y, constant = skyscraper_constant, health = skyscraper_hp, half_health = skyscraper_half_hp)
# window.tracer(n = 1)
print(all_object)

while True:
    window.update()
    enemy_spawn_detector += 1
    if enemy_spawn_detector % 100 == 0:
        enemy_spawn_detector = 0
        enemy_missile_spawn()
    if game_over_constant  == 0:
        #game_over()
        destroy_object()
        missile_contact()
        flight_of_missile(data = my_missiles_data)
        flight_of_missile(data = enemy_missiles_data)
    else:
        pass
        #game_over()





