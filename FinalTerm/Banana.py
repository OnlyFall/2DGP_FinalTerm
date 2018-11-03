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


# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 0.9 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6



# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE, DIE, DOWN, END_GOIDLE, END_GORUN = range(10)

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
            banana.jumpRange = 0

    @staticmethod
    def do(banana):
        banana.frame = (banana.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6

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

             
        if (r, g, b) == (78, 201, 17) or (r, g, b) == (67, 119, 108) or (r, g, b) == (45, 132, 114) or (r, g, b) == (106, 150, 194) or (r, g, b) == (70, 106, 144) or (r, g, b) == (46, 79, 114) or (r, g, b) == (78, 163, 146):
            pass

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
            banana.jumpRange = 0

    @staticmethod
    def do(banana):
        banana.frame = (banana.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
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


        if (r, g, b) == (78, 201, 17) or (r, g, b) == (67, 119, 108) or (r, g, b) == (45, 132, 114) or (r, g, b) == (106, 150, 194) or (r, g, b) == (70, 106, 144) or (r, g, b) == (46, 79, 114) or (r, g, b) == (78, 163, 146):
            pass

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
        banana.frame = (banana.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        banana.x += banana.velocity * game_framework.frame_time
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
            banana.image.clip_draw(int(banana.frame) * 150, 150, 150, 150, banana.x, banana.y)
        else:
            banana.image.opacify(1)
            banana.image.clip_draw(int(banana.frame) * 150, 0, 150, 150, banana.x, banana.y)


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
        banana.frame = (banana.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        banana.x += banana.velocity * game_framework.frame_time
        if banana.dir == 1:
            banana.y -= 200 * game_framework.frame_time * 2
        else:
            banana.y -= 200 * game_framework.frame_time * 2

        banana.x = clamp(25, banana.x, 1600 - 25)

        if banana.y <= 90:
            if banana.velocity > 0 or banana.velocity < 0:
                banana.add_event(END_GORUN)
            else:
                banana.add_event(END_GOIDLE)

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

        if (r, g, b) == (78, 201, 17) or (r, g, b) == (67, 119, 108) or (r, g, b) == (45, 132, 114) or (r, g, b) == (106, 150, 194) or (r, g, b) == (70, 106, 144) or (r, g, b) == (46, 79, 114) or (r, g, b) == (78, 163, 146):
            if banana.velocity > 0 or banana.velocity < 0:
                banana.add_event(END_GORUN)
            else:
                banana.add_event(END_GOIDLE)

    @staticmethod
    def draw(banana):
        if banana.dir == 1:
            banana.image.opacify(1)
            banana.image.clip_draw(int(banana.frame) * 150, 150, 150, 150, banana.x, banana.y)
        else:
            banana.image.opacify(1)
            banana.image.clip_draw(int(banana.frame) * 150, 0, 150, 150, banana.x, banana.y)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: JumpUpState, DOWN:JumpDownState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: JumpUpState, DOWN:JumpDownState},
    JumpUpState: {RIGHT_DOWN: JumpUpState, LEFT_DOWN: JumpUpState, RIGHT_UP: JumpUpState, LEFT_UP: JumpUpState, SPACE: JumpUpState, DOWN:JumpDownState},
    JumpDownState: {END_GOIDLE: IdleState, END_GORUN: RunState, RIGHT_DOWN: JumpDownState, LEFT_DOWN: JumpDownState, RIGHT_UP: JumpDownState, LEFT_UP: JumpDownState, SPACE: JumpDownState}
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
        self.image = load_image('character\\Banana\\totalBanana.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.stage = stage
        self.CrashImageStage1 = PIL.Image.open("STEP\\PT_0005.png")
        self.CrashImageStage2 = PIL.Image.open("STEP\\PT_0004.png")
        self.CrashImageStage3 = PIL.Image.open("STEP\\PT_0003.png")
        self.CrashImageStage4 = PIL.Image.open("STEP\\PT_0002.png")
        self.CrashImageStage5 = PIL.Image.open("STEP\\PT_0001.png")
        self.cur_state.enter(self, None)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def StageUpdate(self, stage):
        self.stage = stage

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
