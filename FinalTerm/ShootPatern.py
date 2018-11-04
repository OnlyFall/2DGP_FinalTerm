from pico2d import *
import game_world
from Shoot import Shoot
import random

shootTime = 0

def Pattern1():
    global shootTime
    switch = random.randint(1, 2)

    for i in range(10):
        if switch == 1:
            goX = math.cos((3.141592 / 180) * (i * 9 + 180)) * 400 + 1580
            goY = math.sin((3.141592 / 180) * (i * 9 + 180)) * 400 + 750
        else:
            goX = math.cos((3.141592 / 180) * (i * 9 + 176)) * 400 + 1580
            goY = math.sin((3.141592 / 180) * (i * 9 + 176)) * 400 + 750

        lengthX = goX - 1600
        lengthY = goY - 800

        shoot = Shoot(1580, 750, (lengthX / 2), (lengthY / 2))
        game_world.add_object(shoot, 2)

def Pattern2():
    global shootTime

    if shootTime == 0:
        for i in range(11):
            goX = math.cos((3.141592 / 180) * (i * 9 + 225)) * 400 + 800
            goY = math.sin((3.141592 / 180) * (i * 9 + 225)) * 400 + 750

            lengthX = goX - 800
            lengthY = goY - 750

            shoot = Shoot(800, 750, (lengthX / 2), (lengthY / 2))
            game_world.add_object(shoot, 2)

    elif shootTime == 1:
        for i in range(11):
            goX = math.cos((3.141592 / 180) * (i * 20 + 90)) * 400 + 1580
            goY = math.sin((3.141592 / 180) * (i * 20 + 90)) * 400 + 300

            lengthX = goX - 1580
            lengthY = goY - 300

            shoot = Shoot(1580, 300, (lengthX / 2), (lengthY / 2))
            game_world.add_object(shoot, 2)

    elif shootTime == 2:
        for i in range(11):
            goX = math.cos((3.141592 / 180) * (i * 20 + 270)) * 400 + 20
            goY = math.sin((3.141592 / 180) * (i * 20 + 270)) * 400 + 300

            lengthX = goX - 20
            lengthY = goY - 300

            shoot = Shoot(30, 300, (lengthX / 2), (lengthY / 2))
            game_world.add_object(shoot, 2)

    shootTime = (shootTime + 1) % 3

def Pattern3():
    global shootTime

    for i in range(16):
        if shootTime == 0:
            goX = (i + 1) * 100
            goY = 0

            lengthX = goX - (i + 1) * 100
            lengthY = goY - 750

            shoot = Shoot(goX, 750, (lengthX / 2), (lengthY / 2))
            game_world.add_object(shoot, 2)

        elif shootTime == 1:
            goX = (i + 1) * 100 - 50
            goY = 0

            lengthX = goX - ((i + 1) * 100 - 50)
            lengthY = goY - 750

            shoot = Shoot(goX, 750, (lengthX / 2), (lengthY / 2))
            game_world.add_object(shoot, 2)

    for i in range(5):
        goX = 0
        goY = i * 160

        lengthX = goX - 1580
        lengthY = goY - (i * 160)

        shoot = Shoot(goX, 750, (lengthX / 2), (lengthY / 2))
        game_world.add_object(shoot, 2)

    shootTime = (shootTime + 1) % 2


def Pattern4():
    pass

def Pattern5():
    pass


def MakeShoot():
    pass
