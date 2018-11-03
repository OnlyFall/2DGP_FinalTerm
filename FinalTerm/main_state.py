import random
import json
import os
from Shoot import Shoot
from pico2d import *
import game_framework
import game_world

from Banana import Banana
from background import Back

name = "MainState"

banana = None
back = None
Die = None
StageCount = 0
shootingTime = 0
stage = 1
def enter():
    global banana, back
    global Die
    global stage
    global StageCount
    global shootingTime
    stageCount = get_time()
    shootingTime = stageCount
    back = Back(stage)
    banana = Banana(stage)
    game_world.add_object(back, 0)
    game_world.add_object(banana, 1)



def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            banana.handle_event(event)


def update():
    global StageCount, back, shootingTime
    global stage
    if get_time() - StageCount > 10:
        stage = random.randint(1, 5)
        back.stageUpdate(stage)
        banana.StageUpdate(stage)
        StageCount = get_time()

    if get_time() - shootingTime > 2:
        shootingTime = get_time()

        for i in range(10):
            lengthX = 1600 - (-50)
            lengthY = 800 - (400 - (i * 100))

            shoot = Shoot(1580, 750, -(lengthX / 2), -(lengthY / 2))
            game_world.add_object(shoot, 1)


    print(StageCount)
    print(stage)
    for game_object in game_world.all_objects():
        game_object.update()




def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






