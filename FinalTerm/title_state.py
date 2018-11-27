import game_framework
import main_state
from pico2d import *


name = "TitleState"
BackgroundImage = None
START = None
END = None
sound = None
startSelect = 0
endSelect = 1
banana = None

def enter():
    global BackgroundImage
    global START
    global END
    global sound
    global banana

    BackgroundImage = load_image("Resource\\BG\\title_stateImage.png")
    START = load_image('Resource\\UI\\start.png')
    END = load_image('Resource\\UI\\ENDpng.png')
    banana = load_image('Resource\\character\\Banana\\sittingBanana.png')
    sound = load_music('Resource\\IngameBGM\\On the Long journey.mp3')
    sound.set_volume(20)
    sound.play()


def exit():
    global BackgroundImage
    global START
    global END
    global sound
    del(BackgroundImage)
    del(START)
    del(END)


def handle_events():
    global startSelect, endSelect
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


frame = 0
def draw():
    global startSelect
    global endSelect
    global frame
    clear_canvas()
    BackgroundImage.draw(800, 400, 1600, 800)
    banana.clip_draw(frame * 150, 0, 150, 150, 1200, 190)
    START.clip_draw(startSelect * 129, 0, 129, 25, 800, 300)
    END.clip_draw(0, endSelect * 17, 31, 17, 800, 250, 60, 20)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






