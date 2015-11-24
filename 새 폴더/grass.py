import random

from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        self.xsi,self.ysi = 400,30
        self.bgm = load_music('football.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
        self.x,self.y = self.xsi,self.ysi
    def draw(self):
        self.image.draw(self.x,self.y)

    def get_bb(self):
        return self.x - self.xsi, self.y - self.ysi, self.x + self.xsi, self.y + self.ysi

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class Back:
    image = None
    def __init__(self):
        self.xsi,self.ysi = 400,300
        self.frame = 0
        self.x,self.y = self.xsi,self.ysi
        for i in range(0, 14):
            self.image = load_image('map\map (%d).png' % i )

    def update(self,frame_time):
        self.frame += 0.5*frame_time
        if self.frame > 14 :
            self.frame = 0
        self.image = load_image('map\map (%d).png' % self.frame )

    def draw(self):
        self.image.clip_draw(0,0,800,600,self.x,self.y)

    def get_bb(self):
        return self.x - self.xsi, self.y - self.ysi, self.x + self.xsi, self.y + self.ysi

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
