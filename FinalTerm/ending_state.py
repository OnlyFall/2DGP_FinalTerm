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
from Banana import Banana
from background import Back

name = "EndingState"


def enter():
    #뒷배경 로드(BG폴더에서 할 예정)
    pass



def exit():
    pass

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


def update():
    pass




def draw():
    pass





