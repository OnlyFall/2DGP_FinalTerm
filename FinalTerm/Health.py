from pico2d import *


class Health:
    def __init__(self):
        self.FullHeart = load_image('Resource\\UI\\HEART\\Heart.png')
        self.CrashHeart = load_image('Resource\\UI\\HEART\\DieHeart.png')
        self.x = 50
        self.y = 750
        self.crash = 0

    def update(self):
        pass

    def crashCount(self, crash):
        self.crash = crash

    def draw(self):
        for i in range(5):
            if i < 5 - self.crash:
                self.FullHeart.clip_draw(0, 0, 100, 100, self.x + (i * 50), self.y, 50, 50)
            else:
                self.CrashHeart.clip_draw(0, 0, 100, 100, self.x + (i * 50), self.y, 50, 50)

