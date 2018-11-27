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

from Health import Health
from titleBanana import Banana
from background import Back

name = "EndingState"

BackgroundImage = None
banana = None

def enter():
    #뒷배경 로드(BG폴더에서 할 예정)
    global BackgroundImage
    global banana
    banana = Banana()
    BackgroundImage = load_image("Resource\\BG\\title_stateImage.png")
    game_world.add_object(banana, 0)


def exit():
    global BackgroundImage
    del(BackgroundImage)
    pass

def pause():
    pass


def resume():
    pass

def loadScore():
    pass



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()


def update():
    for game_object in game_world.all_objects():
        game_object.update()




font = None
def draw():
    #font = load_font()
    clear_canvas()
    BackgroundImage.draw(800, 400, 1600, 800)
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()





