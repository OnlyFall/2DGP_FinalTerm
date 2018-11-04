from pico2d import *
import game_world
from Shoot import Shoot
import random

def Pattern1():
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

    for i in range(11):
        goX = math.cos((3.141592 / 180) * (i * 9 + 225)) * 400 + 800
        goY = math.sin((3.141592 / 180) * (i * 9 + 225)) * 400 + 750

        lengthX = goX - 800
        lengthY = goY - 750

        shoot = Shoot(800, 750, (lengthX / 2), (lengthY / 2))
        game_world.add_object(shoot, 2)

def Pattern3():
    pass

def Pattern4():
    pass

def Pattern5():
    pass


def MakeShoot():
    pass
