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

from collections import  OrderedDict
loadRank = []
tmpRank = []

name = "MainState"
#사용자 점수, 목숨
userScore = 0
printScore = 0
hart = 0

banana = None
back = None
Die = None
health = None
StageCount = 0
Launchlatency = 0
stage = 1

skillGage = 0
skillStartTime = 0
skillUseCheck = False

HitSound = None

def enter():
    global banana, back
    global Die
    global health
    global stage
    global StageCount
    global shootingTime
    global hart
    global userScore, printScore
    global HitSound
    global skillGage


    if HitSound == None:
        HitSound = load_wav("Resource\\Sound\\Hit.wav")
    hart = 0
    userScore = 0
    printScore = 0
    skillGage = 0
    stageCount = get_time()
    shootingTime = stageCount
    stage = random.randint(1,3)
    back = Back(stage)
    health = Health()
    banana = Banana(stage)
    game_world.add_object(back, 0)
    game_world.add_object(health, 0)
    game_world.add_object(banana, 1)



def exit():
    global HitSound
    game_world.clear()

def pause():
    pass


def resume():
    pass



def handle_events():
    global skillGage
    global skillStartTime
    global skillUseCheck

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_z:
            if skillGage > 10 and skillUseCheck == False:
                skillStartTime = get_time()
                skillUseCheck = True
                banana.skillUse(True)

        elif event.type == SDL_KEYUP and event.key == SDLK_z:
            skillUseCheck = False
            banana.skillUse(False)


        else:
            banana.handle_event(event)




def update():
    file_data = OrderedDict()
    global StageCount, back, Launchlatency, hart
    global stage
    global userScore
    global printScore
    global skillGage
    global skillUseCheck
    global skillStartTime
    global HitSound

    if back.returnChangeMapResult() == False:
        banana.ChangeMap(False)

    if get_time() - StageCount > 30:
        back.MapChangeButton()
        banana.ChangeMap(True)
        stage = random.randint(1, 3)
        back.stageUpdate(stage)
        banana.StageUpdate(stage)
        StageCount = get_time()

    if get_time() - Launchlatency > 1:
        if skillUseCheck == False:
            skillGage += 1
        else:
            skillGage -= 3
            if skillGage < 2:
                skillUseCheck = False
                banana.skillUse(False)

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
        userScore += 10

    for game_object in game_world.check_object(2):
        if game_world.collide(game_object, banana):
            if skillUseCheck == False:
                HitSound.play()
                if hart < 4:
                    hart += 1
                else:
                    back.endMusic()
                    with open('Rank.json', 'r', encoding="utf-8") as f:
                        loadRank = json.load(f)
                    k = loadRank["Rank"]
                    tmpRank = k

                    tmpRank.append(userScore)
                    file_data["Rank"] = tmpRank

                    # loadRank.append(save_time)

                    with open('Rank.json', 'w', encoding="utf-8") as f:
                        json.dump(file_data, f, ensure_ascii=False, indent="\t")

                    ending_state.loadScore(userScore)
                    game_framework.change_state(ending_state) #여기에 체력 다 사라지면 결과창으로 넘어감

            game_world.remove_object(game_object)
            health.crashCount(hart)



    for game_object in game_world.all_objects():
        game_object.update()

    if printScore < userScore:
        printScore += 1


font = None

def draw():
    global font
    global printScore
    global skillGage

    if font == None:
        font = load_font('ENCR10B.TTF', 20)

    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    font.draw(1400, 700, "Score : %d" % int(printScore), (255, 255, 255))
    font.draw(1400, 670, "SP : %d" % float(skillGage), (255, 255, 255))

    update_canvas()






