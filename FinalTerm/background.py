from pico2d import *

class Back:
    def __init__(self, stage):
        self.change = False
        self.stage1 = load_image('Resource\\BG\\Stage1Map1.bmp')
        self.stage2 = load_image('Resource\\BG\\Stage1Map2.bmp')
        self.stage3 = load_image('Resource\\BG\\Stage1Map1.bmp')
        self.stage4 = load_image('Resource\\BG\\Stage1Map1.bmp')
        self.stage5 = load_image('Resource\\BG\\Stage1Map1.bmp')

        self.step1 = load_image('Resource\\STEP\\PT_0005.png')
        self.step2 = load_image('Resource\\STEP\\PT_0004.png')
        self.step3 = load_image('Resource\\STEP\\PT_0003.png')
        self.step4 = load_image('Resource\\STEP\\PT_0002.png')
        self.step5 = load_image('Resource\\STEP\\PT_0001.png')
        self.stage = stage

        self.volume = load_music('Resource\\IngameBGM\\Town8.mp3')
        self.volume.set_volume(40)
        self.volume.play()
    def update(self):
        pass

    def MapChangeButton(self):
        self.change = True

    def stageUpdate(self, stage):
        self.stage = stage

    def draw(self):
        self.stage1.clip_draw(0, 0, 1600, 800, 1600 // 2, 800 // 2)

        if self.stage == 1:
            self.step1.clip_draw(100, 50, 1600, 800, 1600 // 2, 800 // 2 - 50)

        elif self.stage == 2:
            self.step2.clip_draw(100, 50, 1600, 800, 1600 // 2, 800 // 2 - 50)

        elif self.stage == 3:
            self.step3.clip_draw(100, 50, 1600, 800, 1600 // 2, 800 // 2 - 50)

        elif self.stage == 4:
            self.step4.clip_draw(100, 50, 1600, 800, 1600 // 2, 800 // 2 - 50)

        elif self. stage == 5:
            self.step5.clip_draw(100, 50, 1600, 800, 1600 // 2, 800 // 2 - 50)
        #self.image.draw(1200, 30)
