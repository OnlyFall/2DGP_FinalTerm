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
sound = None
printScore = 0

def enter():
    #뒷배경 로드(BG폴더에서 할 예정)
    global BackgroundImage
    global banana
    global sound
    global printScore

    printScore = 0
    banana = Banana()
    BackgroundImage = load_image("Resource\\BG\\title_stateImage.png")
    game_world.add_object(banana, 0)
    sound = load_music('Resource\\IngameBGM\\On the Long journey.mp3')
    sound.set_volume(20)
    sound.play()


def exit():
    global BackgroundImage
    global sound
    del(sound)
    del(BackgroundImage)

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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
                game_framework.change_state(title_state)



def update():
    global printScore
    for game_object in game_world.all_objects():
        game_object.update()

    if printScore < score:
        printScore += 1




smallfont = None
bigfont = None

def draw():
    global smallfont
    global bigfont
    global score
    if smallfont == None:
        smallfont = load_font('ENCR10B.TTF', 20)

    if bigfont == None:
        bigfont = load_font('ENCR10B.TTF', 40)

    #font = load_font()
    clear_canvas()
    BackgroundImage.draw(800, 400, 1600, 800)
    for game_object in game_world.all_objects():
        game_object.draw()

    bigfont.draw(680, 400, "Score!!!!!!!", (255, 255, 255))
    bigfont.draw(760, 350, str(printScore), (255, 255, 255))

    smallfont.draw(650, 250, "Press 'R' key is Restart", (255, 255, 255))
    update_canvas()





