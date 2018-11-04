from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


class Shoot:
    image = None

    def __init__(self, x, y, distanceX, distanceY):
        if Shoot.image == None:
            Shoot.image = load_image('ShootingImage\\먼지.png')
        self.x, self.y, self.distanceX, self.distanceY = x, y, distanceX, distanceY

    def draw(self):
        #self.image.draw(self.x, self.y)
        self.image.clip_draw(0, 0, 50, 50, self.x, self.y, 25, 25)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 8, self.y + 8

    def update(self):
        self.x += self.distanceX * game_framework.frame_time
        self.y += self.distanceY * game_framework.frame_time

        if self.x < 5 or self.x > 1600 - 5 or self.y < 5 or self.y > 795:
            game_world.remove_object(self)
