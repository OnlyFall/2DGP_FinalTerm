import game_framework
import main_state
import ending_state
from pico2d import *
from titleBanana import Banana
import game_world

name = "TitleState"
BackgroundImage = None
START = None
END = None

sound = None
selectSound = None

font = None
startSelect = 0
endSelect = 1
banana = None

R = 255
G = 255
B = 255

def enter():
    global BackgroundImage
    global START
    global END
    global sound, selectSound
    global banana
    global font

    if font == None:
        font = load_font('ENCR10B.TTF', 60)

    BackgroundImage = load_image("Resource\\BG\\title_stateImage.png")
    START = load_image('Resource\\UI\\start.png')
    END = load_image('Resource\\UI\\ENDpng.png')
    banana = Banana()
    game_world.add_object(banana, 0)
    sound = load_music('Resource\\IngameBGM\\On the Long journey.mp3')
    selectSound = load_wav('Resource\\Sound\\Select.wav')
    sound.set_volume(20)
    sound.play()


def exit():
    global BackgroundImage
    global START
    global END
    global sound, selectSound

    game_world.clear()
    del(sound)
    del(selectSound)
    del(BackgroundImage)
    del(START)
    del(END)


def handle_events():
    global startSelect, endSelect
    global selectSound
    StartsoundPlay = False
    EndsoundPlay = False
    events = get_events()
    for event in events:
        if(event.type == SDL_MOUSEMOTION):
            mouseX = event.x
            mouseY = 800 - event.y - 1
            if mouseX > (1600 / 2) - (129 / 2) and  mouseX < (1600 / 2) + (129 / 2) and mouseY < 300 + (25 / 2) and mouseY > 300 - (25 / 2):
                startSelect = 1
            else:
                startSelect = 0

            if(mouseX > (1600 / 2) - (60 / 2) and mouseX < (1600 / 2) + (60 / 2) and mouseY < 250 + (20 / 2) and mouseY > 250 - (20 / 2)):
                endSelect = 1
            else:
                endSelect = 0

        elif(event.type == SDL_MOUSEBUTTONDOWN):
            if startSelect == 1:
                game_framework.change_state(main_state)
            elif endSelect == 1:
                game_framework.quit()

        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)


def draw():
    global startSelect
    global endSelect
    global frame
    global font
    clear_canvas()
    BackgroundImage.draw(800, 400, 1600, 800)
    START.clip_draw(startSelect * 129, 0, 129, 25, 800, 300)
    END.clip_draw(0, endSelect * 17, 31, 17, 800, 250, 60, 20)
    font.draw(700, 500, "Banana", (255, 255, 255))
    font.draw(660, 440, "Survivor", (255, 255, 255))

    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def pause():
    pass


def resume():
    pass






