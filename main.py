
import pgzrun
from pgzero.builtins import Actor, keyboard, sounds, music, clock, keys
from random import randint
from random import randint


def draw():
    if Game_Over:
        screen.fill(' pink' )
        screen.draw.text(f'Time out !, your score : {Score}',(200,300),fontsize = 50)
        screen.draw.text(f'Press Enter to play again',(350,350),fontsize = 50)
    elif Game_Over_1:
        screen.fill('blue')
        screen.draw.text('You are Dead', (350, 350), fontsize=50)
    else:
        if Time >= 40:
            screen.fill('gray')
            screen.draw.text(f'No.1',(500,10),fontsize = 40)
            screen.draw.text(f'Score :+ {Score}',(5,10),fontsize = 30) 
            screen.draw.text(f'Time : {Time}',(890,10),fontsize = 30)
            screen.draw.text(f' Music.Play O:P ',(850,40),fontsize = 30)           
            dog.draw()
            coin.draw()
            coin1.draw()
            coin2.draw()           
            gg.draw()
            gg1.draw()
            gg2.draw()
            gg3.draw()
            gg4.draw()                                                  
            gun.draw()
            gun1.draw()
            gun2.draw()
            gun3.draw()
        elif 20<Time<=40:
            screen.fill('blue')
            screen.draw.text('No.2',(500,10),fontsize = 40)
            screen.draw.text(f'No.1',(500,10),fontsize = 40)
            screen.draw.text(f'Score : {Score}',(5,10),fontsize = 30)
            screen.draw.text(f'Time : {Time}',(890,10),fontsize = 30)
            screen.draw.text(f' Music.Play O:P ',(850,40),fontsize = 30)       
            dog.draw()
            coin.draw()
            coin1.draw()            
            coin2.draw()           
            gg.draw()
            gg1.draw()
            gg2.draw()
            gg3.draw()
            gg4.draw()                                                 
            gun.draw()
            gun1.draw()
            gun2.draw()
            gun3.draw()
        else:
            screen.fill('green')
            screen.draw.text('No.3',(500,10),fontsize = 40)
            screen.draw.text(f'Score : {Score}',(5,10),fontsize = 30)
            screen.draw.text(f'Time : {Time}',(890,10),fontsize = 30)
            screen.draw.text(f' Music.Play O:P ',(850,40),fontsize = 30)      
            dog.draw()
            coin.draw()
            coin1.draw()
            coin2.draw()            
            gg.draw()
            gg1.draw()
            gg2.draw()
            gg3.draw()
            gg4.draw()                                                   
            gun.draw()
            gun1.draw()
            gun2.draw()
            gun3.draw()            

def on_key_down(key , mod, unicode):
    global Score, Time,Game_Over,Game_Over_1
    if Game_Over:
        if key == keys.RETURN:
           Score = 0
           Time = 60
           Game_Over = False
           place_coin()
           dog.pos = (WIDTH/2,HEIGHT/2)
           ggg()
           ggg_1()
           ggg_2()
           ggg_3()
           ggg_4()
           gunn()
           gunn1()
           gunn2()       
           clock.schedule_interval(count_time,1.0)
    if Game_Over_1:
        if key == keys.RETURN:
           Score = 0
           Time = 60
           Game_Over_1= False
           place_coin()
           dog.pos = (WIDTH/2,HEIGHT/2)
           ggg()
           ggg_1()
           ggg_2()
           ggg_3()
           ggg_4()
           gunn()
           gunn1()
           gunn2()       

def place_coin():
    while True:
        coin.x = randint(coin.width, WIDTH - dog.width)
        coin.y = randint(coin.height, HEIGHT - dog.height)
        if not dog.colliderect(coin):
            break    

def place_coin1():
    while True:
        coin1.x = randint(coin1.width, WIDTH - dog.width)
        coin1.y = randint(coin1.height, HEIGHT - dog.height)
        if not dog.colliderect(coin1):
            break

def place_coin2():
    while True:
        coin2.x = randint(coin2.width, WIDTH - dog.width)
        coin2.y = randint(coin2.height, HEIGHT - dog.height)
        if not dog.colliderect(coin2):
            break

def ggg():
    while True:
       gg.x = randint(gg.width, WIDTH - dog.width)
       gg.y = 0
       gg.y = gg.y   + randint(1,8)
       if not dog.colliderect(gg):
           break

def ggg_1():
    while True:
       gg1.x = randint(gg1.width, WIDTH - dog.width)
       gg1.y = 0
       gg1.y = gg1.y   + randint(1,8)
       if not dog.colliderect(gg1):
           break

def ggg_2():
    while True:
       gg2.x = randint(gg2.width, WIDTH - dog.width)
       gg2.y = 0
       gg2.y = gg2.y   + randint(1,8)
       if not dog.colliderect(gg2):
           break

def ggg_3():
    while True:
       gg3.x = randint(gg3.width, WIDTH - dog.width)
       gg3.y = 0
       gg3.y = gg3.y   + randint(1,8)
       if not dog.colliderect(gg3):
           break

def ggg_4():
    while True:
       gg4.x = randint(gg4.width, WIDTH - dog.width)
       gg4.y = 0
       gg4.y = gg4.y   + randint(1,8)
       if not dog.colliderect(gg4):
           break

def gunn():
    while True:  
        gun.x = 1024
        gun.x = gun.x-randint(5,10)
        gun.y = randint(gun.height, HEIGHT - dog.height)
        if not dog.colliderect(gun):
           break

def gunn1():
    while True:
        gun1.x = 1024
        gun1.x = gun1.x-randint(5,10)
        gun1.y = randint(gun1.height, HEIGHT - dog.height)
        if not dog.colliderect(gun1):
           break

def gunn2():
    while True:
        gun2.x = 1024
        gun2.x = gun2.x-randint(5,10)
        gun2.y = randint(gun2.height, HEIGHT - dog.height) 
        if not dog.colliderect(gun2):
           break

def update():
    global Score,Game_Over_1
    gg.angle = gg.angle -0.5
    gg1.angle = gg1.angle -0.5
    gg2.angle = gg2.angle -0.5
    gg3.angle = gg3.angle -0.5
    gg4.angle = gg4.angle -0.5
    gun3.angle = gun3.angle +10
    gun3.x = gun3.x + 10
    gg.y = gg.y   + randint(1,8)
    gg1.y = gg1.y + randint(1,8)
    gg2.y = gg2.y + randint(1,8)
    gg3.y = gg3.y + randint(1,8)
    gg4.y = gg4.y + randint(1,8)
    gun.x = gun.x-randint(5,12)
    gun1.x = gun.x-randint(5,12)
    gun2.x = gun.x-randint(5,12)
    if keyboard.O:
            music.play('rick')      
    elif keyboard.P:
        music.stop()
    elif gun.x <= 0:
            gun.x = 1024
            gunn()
            sounds.pew.play()
    elif gun1.x <= 0:
            gun1.x = 1024
            gunn1()
    elif gun2.x <= 0:
            gun2.x = 1024
            gunn2()
    elif gg.y>HEIGHT :
            gg.y = 0
            ggg()
    elif gg1.y>HEIGHT :
            gg1.y = 0
            ggg_1()
    elif gg2.y>HEIGHT :
            gg2.y = 0
            ggg_2()
    elif gg3.y>HEIGHT :
            gg3.y = 0
            ggg_3()
    elif gg4.y>HEIGHT :
            gg4.y = 0
            ggg_4()
    elif gun3.x > WIDTH:
        gun3.x = 0  
    elif(dog.colliderect(coin)):
        sounds.ping.play()
        Score += 1
        place_coin()
    elif(dog.colliderect(coin1)):
        sounds.ping.play()
        Score += 1
        place_coin1()
    elif(dog.colliderect(coin2)):
        sounds.ping.play()
        Score += 1
        place_coin2()
    elif(dog.colliderect(gg)):
        if Time>=57 :
            Game_Over_1 = False
        else:
            music.stop()
            sounds.tom.play(1)
            Game_Over_1 = True
    elif(dog.colliderect(gg1)):
        if Time>=57 :
            Game_Over_1 = False
        else:
            music.stop()
            sounds.tom.play(1)
            Game_Over_1 = True
    elif(dog.colliderect(gg2)):
        if Time>=57:
            Game_Over_1 = False
        else:
            music.stop()
            sounds.tom.play(1)
            Game_Over_1 = True
    elif(dog.colliderect(gg3)):
        if Time>=57:
           Game_Over_1 = False
        else:
            music.stop()
            sounds.tom.play(1)
            Game_Over_1 = True
    elif(dog.colliderect(gg4)):
        if Time>=57:
            Game_Over_1 = False
        else:
            music.stop()
            sounds.tom.play(1)
            Game_Over_1 = True
    elif(dog.colliderect(gun)):
        if Time>=57:
            Game_Over_1 = False
        else:
            music.stop()
            sounds.tom.play(1)
            Game_Over_1 = True
    elif(dog.colliderect(gun1)):
        if Time>=57:
           Game_Over_1 = False
        else:
            music.stop()
            sounds.tom.play(1)
            Game_Over_1 = True
    elif(dog.colliderect(gun2)):
        if Time>=57:
            Game_Over_1 = False
        else:
            music.stop()
            sounds.tom.play(1)
            Game_Over_1 = True
    elif(dog.colliderect(gun3)):
        if Time>=57:
            Game_Over_1 = False
        else:
            music.stop()
            sounds.tom.play(1)
            Game_Over_1 = True
    elif Game_Over_1:
        screen.fill('pink')
        screen.draw.text('You are Dead', (350, 350), fontsize=50)
    elif Time == MAX_TIME:
        Game_Over = False
        Game_Over_1 = False
    elif (dog.y>HEIGHT):
        dog.y = 600
    elif (dog.x>WIDTH):
        dog.x = 1024
    elif (dog.y<0):
        dog.y = 0
    elif (dog.x<0):
        dog.x = 0
    elif (keyboard.A):dog.x -= 13
    elif (keyboard.D): dog.x += 13
    elif (keyboard.W):dog.y -= 13
    elif (keyboard.S):dog.y += 13

def count_time():
    global Time,Game_Over
    Time -= 1
    if Time == MAX_TIME:
        Game_Over = True
        clock.unschedule(count_time)

TITLE = 'Coin Collection Games'
WIDTH = 1024
HEIGHT = 600
Score = 0
Time = 60
Game_Over = False
Game_Over_1 = False
MAX_TIME = 0

dog = Actor('ufo',(WIDTH/2,HEIGHT/2))
coin = Actor('coin')
coin1 = Actor('coin')
coin2 = Actor('coin')
gg = Actor('meter')
gg1 = Actor('meter')
gg2 = Actor('meter')
gg3 = Actor('meter')
gg4 = Actor('meter')
gun = Actor('lazer',(600,150))
gun1 = Actor('lazer',(600,300))
gun2 = Actor('lazer',(600,450))
gun3 = Actor('lazer',(0,600))

place_coin()
place_coin1()
place_coin2()
clock.schedule_interval(count_time,1.0)
pgzrun.go()