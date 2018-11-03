from pico2d import *

class Music:
    def __init__(self, data):
        self.music = data

    def rapeat_play(self):
        Mix_PlayMusic(self.music, -1)

    def play(self, n=1):
        Mix_PlayMusic(self.music, n)

    def set_volume(self, v):
        Mix_Volume(v)

    def get_volume(self):
        return Mix_VolumeMusic(-1)

    def stop(self):
        Mix_HaltMusic()

    def pause(self):
        Mix_PauseMusic()

    def resume(self):
        Mix_ResumeMusic()

    def __del__(self):
        Mix_FreeMusic(self.music)