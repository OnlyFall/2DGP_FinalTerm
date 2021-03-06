import game_framework
from pico2d import *
import PIL.Image
import math
import random

import game_world

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


#바나나의 기본 애니메이션 동작 속도
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 0.9 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6

#바나나 점프시에 따로 설정된 타임들
TIME_PER_ACTION_JUMP = 0.5
ACTION_PER_TIME_JUMP = 0.9 / TIME_PER_ACTION
FRAMES_PER_ACTION_JUMP = 4



# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE, DIE, DOWN, END_IDLE, END_RUN = range(10)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States

class IdleState:

    @staticmethod
    def enter(banana, event):
        banana.timer = get_time() - 0.9
        if event == RIGHT_DOWN:
            banana.velocity += RUN_SPEED_PPS * 1.5
        elif event == LEFT_DOWN:
            banana.velocity -= RUN_SPEED_PPS * 1.5
        elif event == RIGHT_UP:
            banana.velocity -= RUN_SPEED_PPS * 1.5
        elif event == LEFT_UP:
            banana.velocity += RUN_SPEED_PPS * 1.5


    @staticmethod
    def exit(banana, event):
        if event == SPACE:
            banana.jumpSound.play()
            banana.jumpRange = 0

    @staticmethod
    def do(banana):
        banana.frame = (banana.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        banana.skillFrame = (banana.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5



        if banana.stage == 1:
            r, g, b, a = banana.CrashImageStage1.getpixel((banana.x + 100, 800 - banana.y - 30))
        elif banana.stage == 2:
            r, g, b, a = banana.CrashImageStage2.getpixel((banana.x + 100, 800 - banana.y - 30))
        elif banana.stage == 3:
            r, g, b, a = banana.CrashImageStage3.getpixel((banana.x + 100, 800 - banana.y - 30))
        elif banana.stage == 4:
            r, g, b, a = banana.CrashImageStage4.getpixel((banana.x + 100, 800 - banana.y - 30))
        elif banana.stage == 5:
            r, g, b, a = banana.CrashImageStage5.getpixel((banana.x + 100, 800 - banana.y - 30))

        if banana.Mapchange == False:
            if (r, g, b) == (78, 201, 17) or (r, g, b) == (67, 119, 108) or (r, g, b) == (45, 132, 114) or (r, g, b) == (106, 150, 194) or (r, g, b) == (70, 106, 144) or (r, g, b) == (46, 79, 114) or (r, g, b) == (78, 163, 146):
                pass

            else:
                if banana.y > 90:
                    banana.add_event(DOWN)

        else:
            if banana.y > 90:
                banana.add_event(DOWN)


    @staticmethod
    def draw(banana):
        if banana.dir == 1:
            banana.image.opacify(1)
            banana.image.clip_draw(int(banana.frame) * 150, 150, 150, 150, banana.x, banana.y)
        else:
            banana.image.opacify(1)
            banana.image.clip_draw(int(banana.frame) * 150, 0, 150, 150, banana.x, banana.y)

        if banana.skillUseCheck == True:
            banana.skillImage.clip_draw(int(banana.skillFrame) * 192, 192, 192, 192, banana.x, banana.y)


class RunState:

    @staticmethod
    def enter(banana, event):
        if event == RIGHT_DOWN:
            banana.velocity += RUN_SPEED_PPS * 1.5

        elif event == LEFT_DOWN:
            banana.velocity -= RUN_SPEED_PPS * 1.5

        elif event == RIGHT_UP:
            banana.velocity -= RUN_SPEED_PPS * 1.5

        elif event == LEFT_UP:
            banana.velocity += RUN_SPEED_PPS * 1.5

        banana.dir = clamp(-1, banana.velocity, 1)

    @staticmethod
    def exit(banana, event):
        if event == SPACE:
            banana.jumpSound.play()
            banana.jumpRange = 0

    @staticmethod
    def do(banana):
        banana.frame = (banana.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        banana.skillFrame = (banana.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        banana.x += banana.velocity * game_framework.frame_time
        banana.x = clamp(25, banana.x, 1600 - 25)

        if banana.stage == 1:
            r, g, b, a = banana.CrashImageStage1.getpixel((banana.x + 100, 800 - banana.y - 30))
        elif banana.stage == 2:
            r, g, b, a = banana.CrashImageStage2.getpixel((banana.x + 100, 800 - banana.y - 30))
        elif banana.stage == 3:
            r, g, b, a = banana.CrashImageStage3.getpixel((banana.x + 100, 800 - banana.y - 30))
        elif banana.stage == 4:
            r, g, b, a = banana.CrashImageStage4.getpixel((banana.x + 100, 800 - banana.y - 30))
        elif banana.stage == 5:
            r, g, b, a = banana.CrashImageStage5.getpixel((banana.x + 100, 800 - banana.y - 30))

        if banana.Mapchange == False:
            if (r, g, b) == (78, 201, 17) or (r, g, b) == (67, 119, 108) or (r, g, b) == (45, 132, 114) or (r, g, b) == (106, 150, 194) or (r, g, b) == (70, 106, 144) or (r, g, b) == (46, 79, 114) or (r, g, b) == (78, 163, 146):
                pass

            else:
                if banana.y > 90:
                    banana.add_event(DOWN)
        else:
            if banana.y > 90:
                banana.add_event(DOWN)

    @staticmethod
    def draw(banana):
        if banana.dir == 1:
            banana.image.opacify(1)
            banana.image.clip_draw(int(banana.frame) * 150, 450, 150, 150, banana.x, banana.y)
        else:
            banana.image.opacify(1)
            banana.image.clip_draw(int(banana.frame) * 150, 300, 150, 150, banana.x, banana.y)

        if banana.skillUseCheck == True:
            banana.skillImage.clip_draw(int(banana.skillFrame) * 192, 192, 192, 192, banana.x, banana.y)


class JumpUpState:

    @staticmethod
    def enter(banana, event):

        if event == RIGHT_DOWN:
            banana.velocity += RUN_SPEED_PPS * 1.5

        elif event == LEFT_DOWN:
            banana.velocity -= RUN_SPEED_PPS * 1.5

        elif event == RIGHT_UP:
            banana.velocity -= RUN_SPEED_PPS * 1.5

        elif event == LEFT_UP:
            banana.velocity += RUN_SPEED_PPS * 1.5

        banana.dir = clamp(-1, banana.velocity, 1)

    @staticmethod
    def exit(banana, event):
        pass

    @staticmethod
    def do(banana):
        banana.frame = (banana.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        banana.x += banana.velocity * game_framework.frame_time
        banana.skillFrame = (banana.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

        if banana.dir == 1:
            banana.jumpRange += 200 * game_framework.frame_time * 2
            banana.y += 200 * game_framework.frame_time * 2
        else:
            banana.jumpRange += 200 * game_framework.frame_time * 2
            banana.y += 200 * game_framework.frame_time * 2

        if banana.y > 750:
            banana.add_event(DOWN)

        banana.x = clamp(25, banana.x, 1600 - 25)

        if banana.jumpRange >= 200:
            banana.add_event(DOWN)


    @staticmethod
    def draw(banana):
        if banana.dir == 1:
            banana.image.opacify(1)
            banana.JumpImage.clip_draw(int(banana.frame) * 150, 0, 150, 150, banana.x, banana.y)
        else:
            banana.image.opacify(1)
            banana.JumpImage.clip_draw(int(banana.frame) * 150, 150, 150, 150, banana.x, banana.y)

        if banana.skillUseCheck == True:
            banana.skillImage.clip_draw(int(banana.skillFrame) * 192, 192, 192, 192, banana.x, banana.y)


class JumpDownState:

    @staticmethod
    def enter(banana, event):
        if event == RIGHT_DOWN:
            banana.velocity += RUN_SPEED_PPS * 1.5

        elif event == LEFT_DOWN:
            banana.velocity -= RUN_SPEED_PPS * 1.5

        elif event == RIGHT_UP:
            banana.velocity -= RUN_SPEED_PPS * 1.5

        elif event == LEFT_UP:
            banana.velocity += RUN_SPEED_PPS * 1.5

        banana.dir = clamp(-1, banana.velocity, 1)

    @staticmethod
    def exit(banana, event):
        pass

    @staticmethod
    def do(banana):
        banana.frame = (banana.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        banana.x += banana.velocity * game_framework.frame_time
        banana.skillFrame = (banana.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

        if banana.dir == 1:
            banana.y -= 200 * game_framework.frame_time * 2
        else:
            banana.y -= 200 * game_framework.frame_time * 2

        banana.x = clamp(25, banana.x, 1600 - 25)

        if banana.y <= 90:
            banana.landingSound.play()
            if banana.velocity > 0 or banana.velocity < 0:
                banana.add_event(END_RUN)
            else:
                banana.add_event(END_IDLE)

        if banana.stage == 1:
            r, g, b, a = banana.CrashImageStage1.getpixel((banana.x + 100, 800 - banana.y - 30))
        elif banana.stage == 2:
            r, g, b, a = banana.CrashImageStage2.getpixel((banana.x + 100, 800 - banana.y - 30))
        elif banana.stage == 3:
            r, g, b, a = banana.CrashImageStage3.getpixel((banana.x + 100, 800 - banana.y - 30))
        elif banana.stage == 4:
            r, g, b, a = banana.CrashImageStage4.getpixel((banana.x + 100, 800 - banana.y - 30))
        elif banana.stage == 5:
            r, g, b, a = banana.CrashImageStage5.getpixel((banana.x + 100, 800 - banana.y - 30))

        if banana.Mapchange == False:
            if (r, g, b) == (78, 201, 17) or (r, g, b) == (67, 119, 108) or (r, g, b) == (45, 132, 114) or (r, g, b) == (106, 150, 194) or (r, g, b) == (70, 106, 144) or (r, g, b) == (46, 79, 114) or (r, g, b) == (78, 163, 146):
                banana.landingSound.play()
                if banana.velocity > 0 or banana.velocity < 0:
                    banana.add_event(END_RUN)
                else:
                    banana.add_event(END_IDLE)

    @staticmethod
    def draw(banana):
        if banana.dir == 1:
            banana.image.opacify(1)
            banana.LandingImage.clip_draw(int(banana.frame) * 150, 0, 150, 150, banana.x, banana.y)
        else:
            banana.image.opacify(1)
            banana.LandingImage.clip_draw(int(banana.frame) * 150, 150, 150, 150, banana.x, banana.y)

        if banana.skillUseCheck == True:
            banana.skillImage.clip_draw(int(banana.skillFrame) * 192, 192, 192, 192, banana.x, banana.y)



next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: JumpUpState,
                DOWN: JumpDownState, END_IDLE: IdleState, END_RUN: RunState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: JumpUpState,
               DOWN: JumpDownState, END_RUN: RunState, END_IDLE: IdleState},
    JumpUpState: {RIGHT_DOWN: JumpUpState, LEFT_DOWN: JumpUpState, RIGHT_UP : JumpUpState, LEFT_UP: JumpUpState,
                  SPACE: JumpUpState, DOWN: JumpDownState},
    JumpDownState: {END_IDLE: IdleState, END_RUN: RunState, RIGHT_DOWN: JumpDownState, LEFT_DOWN: JumpDownState,
                    RIGHT_UP: JumpDownState, LEFT_UP: JumpDownState, SPACE: JumpDownState, DOWN: JumpDownState}
}

class Banana:

    def __init__(self, stage):
        self.x, self.y = 1600 // 2, 90
        self.jumpRange = 0
        self.opacifyValue = 1
        self.GhostX, self.GhostY = 0, 0
        self.rad = 0
        self.standup = 0
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('Resource\\character\\Banana\\totalBanana.png')
        self.LandingImage = load_image('Resource\\character\\Banana\\LandingBanana.png')
        self.JumpImage = load_image('Resource\\character\\Banana\\JumpBanana.png')
        self.skillImage = load_image('Resource\\SkillImage\\Skill.png')

        self.skillUseCheck = False
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.skillFrame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.stage = stage
        self. energy = 0
        self.Mapchange = False

        self.CrashImageStage1 = PIL.Image.open("Resource\\STEP\\PT_0005.png")
        self.CrashImageStage2 = PIL.Image.open("Resource\\STEP\\PT_0004.png")
        self.CrashImageStage3 = PIL.Image.open("Resource\\STEP\\PT_0003.png")
        self.CrashImageStage4 = PIL.Image.open("Resource\\STEP\\PT_0002.png")
        self.CrashImageStage5 = PIL.Image.open("Resource\\STEP\\PT_0001.png")
        self.cur_state.enter(self, None)

        self.jumpSound = load_wav("Resource\\Sound\\Jump.wav")
        self.landingSound = load_wav("Resource\\Sound\\Down.wav")


    def add_event(self, event):
        self.event_que.insert(0, event)

    def StageUpdate(self, stage):
        self.stage = stage

    def ChangeMap(self, bool):
        self.Mapchange = bool

    def get_bb(self):
        return self.x - 30, self.y - 50, self.x + 25, self.y + 50

    def skillUse(self, bool):
        self.skillUseCheck = bool

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
