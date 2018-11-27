import random
import title_state
import math
import json
import os
from Shoot import Shoot
from pico2d import *
import game_framework
import game_world
import ShootPatern
import ending_state

from Health import Health
from Banana import Banana
from background import Back

name = "MainState"
#사용자 점수, 목숨
userScore = 0
hart = 0

banana = None
back = None
Die = None
health = None
StageCount = 0
Launchlatency = 0
stage = 1
def enter():
    global banana, back
    global Die
    global health
    global stage
    global StageCount
    global shootingTime
    global hart
    global userScore

    hart = 0
    userScore = 0
    stageCount = get_time()
    shootingTime = stageCount
    stage = 3
    back = Back(stage)
    health = Health()
    banana = Banana(stage)
    game_world.add_object(back, 0)
    game_world.add_object(health, 0)
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
    global StageCount, back, Launchlatency, hart
    global stage
    if get_time() - StageCount > 10:
        stage = random.randint(1, 3)
        back.stageUpdate(stage)
        banana.StageUpdate(stage)
        StageCount = get_time()

    if get_time() - Launchlatency > 1:
        Launchlatency = get_time()
        if stage == 1:
            ShootPatern.Pattern1()
        elif stage == 2:
            ShootPatern.Pattern2()
        elif stage == 3:
            ShootPatern.Pattern3()
        elif stage == 4:
            ShootPatern.Pattern4()
        elif stage == 5:
            ShootPatern.Pattern5()

    for game_object in game_world.check_object(2):
        if game_world.collide(game_object, banana) == True:
            if hart < 4:
                hart += 1
            else:
                back.endMusic()
                game_framework.change_state(ending_state) #여기에 체력 다 사라지면 결과창으로 넘어감

            game_world.remove_object(game_object)
            health.crashCount(hart)




    for game_object in game_world.all_objects():
        game_object.update()


font = None

def draw():
    global font


    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()






