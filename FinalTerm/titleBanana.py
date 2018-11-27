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


# Boy States

class IdleState:

    @staticmethod
    def enter(banana, event):
       pass


    @staticmethod
    def exit(banana, event):
        pass

    @staticmethod
    def do(banana):
        banana.frame = (banana.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    @staticmethod
    def draw(banana):
        if banana.dir == 1:
            banana.image.opacify(1)
            banana.image.clip_draw(int(banana.frame) * 150, 150, 150, 150, banana.x, banana.y)


class Banana:

    def __init__(self, stage):
        self.x, self.y = 1600 // 2, 90
        self.jumpRange = 0
        self.opacifyValue = 1
        self.GhostX, self.GhostY = 0, 0
        self.rad = 0
        self.standup = 0
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('Resource\\character\\Banana\\sittingBanana.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState

    def add_event(self, event):
        self.event_que.insert(0, event)

    def StageUpdate(self, stage):
        pass

    def get_bb(self):
        return self.x - 30, self.y - 50, self.x + 25, self.y + 50


    def update(self):
        self.cur_state.do(self)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        pass