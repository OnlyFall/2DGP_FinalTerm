from pico2d import *

class Back:
    def __init__(self):
        self.stage1 = load_image('BG\\Stage1Map1.bmp')
        self.step1 = load_image('STEP\\PT_0005.png')
        self.step2 = load_image('STEP\\PT_0004.png')
        self.step3 = load_image('STEP\\PT_0003.png')
        self.step4 = load_image('STEP\\PT_0002.png')
        self.step5 = load_image('STEP\\PT_0001.png')

    def update(self):
        pass

    def draw(self):
        self.stage1.clip_draw(0, 0, 1600, 800, 1600 // 2, 800 // 2)
        self.step1.clip_draw(100, 50, 1600, 800, 1600 // 2, 800 // 2 - 50)
        #self.image.draw(1200, 30)
