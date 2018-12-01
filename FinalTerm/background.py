from pico2d import *
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


#바나나의 기본 애니메이션 동작 속도
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 0.9 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6

class Back:
    def __init__(self, stage):
        self.change = False
        self.stage1 = load_image('Resource\\BG\\Stage1Map1.bmp')
        self.stage2 = load_image('Resource\\BG\\Stage1Map2.bmp')
        self.stage3 = load_image('Resource\\BG\\Stage1Map2.bmp')
        self.stage4 = load_image('Resource\\BG\\Stage1Map2.bmp')
        self.stage5 = load_image('Resource\\BG\\Stage1Map2.bmp')

        self.step1 = load_image('Resource\\STEP\\PT_0005.png')
        self.step2 = load_image('Resource\\STEP\\PT_0004.png')
        self.step3 = load_image('Resource\\STEP\\PT_0003.png')
        self.step4 = load_image('Resource\\STEP\\PT_0002.png')
        self.step5 = load_image('Resource\\STEP\\PT_0001.png')
        self.stage = stage
        self.beforeStage = stage

        self.imageMoveX = 0
        self.volume = load_music('Resource\\IngameBGM\\Town8.mp3')
        self.volume.set_volume(40)
        self.volume.play()
    def update(self):
        pass

    def scroll(self):
        pass

    def endMusic(self):
        self.volume.stop()
        del(self.volume)

    def MapChangeButton(self):
        self.change = True

    def stageUpdate(self, stage):
        self.stage = stage

    def draw(self):

        if self.change:
            if self.beforeStage == 1:
                self.stage1.clip_draw(100, 50, 1600, 800, 1600 // 2 - self.imageMoveX, 800 // 2)
            elif self.beforeStage == 2:
                self.stage2.clip_draw(100, 50, 1600, 800, 1600 // 2 - self.imageMoveX, 800 // 2)
            elif self.beforeStage == 3:
                self.stage3.clip_draw(100, 50, 1600, 800, 1600 // 2 - self.imageMoveX, 800 // 2)
            elif self.beforeStage == 4:
                self.stage4.clip_draw(100, 50, 1600, 800, 1600 // 2 - self.imageMoveX, 800 // 2)
            elif self.beforeStage == 5:
                self.stage5.clip_draw(100, 50, 1600, 800, 1600 // 2 - self.imageMoveX, 800 // 2)

            if self.stage == 1:
                self.stage1.clip_draw(100, 50, 1600, 800, 1600 - self.imageMoveX, 800 // 2)
            elif self.stage == 2:
                self.stage2.clip_draw(100, 50, 1600, 800, 1600 - self.imageMoveX, 800 // 2)
            elif self.stage == 3:
                self.stage3.clip_draw(100, 50, 1600, 800, 1600 - self.imageMoveX, 800 // 2)
            elif self.stage == 4:
                self.stage4.clip_draw(100, 50, 1600, 800, 1600 - self.imageMoveX, 800 // 2)
            elif self.stage == 5:
                self.stage5.clip_draw(100, 50, 1600, 800, 1600 - self.imageMoveX, 800 // 2)

            if self.imageMoveX >= 800:
                self.imageMoveX = 0
                self.change = False
                self.beforeStage = self.stage
            else:
                self.imageMoveX += RUN_SPEED_PPS  / 100



        else:
            if self.stage == 1:
                self.stage1.clip_draw(100, 50, 1600, 800, 1600 // 2, 800 // 2)
                self.step1.clip_draw(100, 50, 1600, 800, 1600 // 2, 800 // 2 - 50)

            elif self.stage == 2:
                self.stage2.clip_draw(100, 50, 1600, 800, 1600 // 2, 800 // 2)
                self.step2.clip_draw(100, 50, 1600, 800, 1600 // 2, 800 // 2 - 50)

            elif self.stage == 3:
                self.stage3.clip_draw(100, 50, 1600, 800, 1600 // 2, 800 // 2)
                self.step3.clip_draw(100, 50, 1600, 800, 1600 // 2, 800 // 2 - 50)

            elif self.stage == 4:
                self.stage4.clip_draw(100, 50, 1600, 800, 1600 // 2, 800 // 2)
                self.step4.clip_draw(100, 50, 1600, 800, 1600 // 2, 800 // 2 - 50)

            elif self.stage == 5:
                self.stage5.clip_draw(100, 50, 1600, 800, 1600 // 2, 800 // 2)
                self.step5.clip_draw(100, 50, 1600, 800, 1600 // 2, 800 // 2 - 50)

