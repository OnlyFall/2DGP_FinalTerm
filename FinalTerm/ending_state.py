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
score = 0

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

def loadScore(insert):
    global score
    score = insert



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
    global font
    global score
    if font == None:
        font = load_font('ENCR10B.TTF', 20)
    #font = load_font()
    clear_canvas()
    BackgroundImage.draw(800, 400, 1600, 800)
    for game_object in game_world.all_objects():
        game_object.draw()

    font.draw(800, 400, "Score!!!!!!!", (255, 255, 255))
    font.draw(800, 350, str(score), (255, 255, 255))
    update_canvas()





