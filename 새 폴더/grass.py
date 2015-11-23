import random

from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        self.xsi,self.ysi = 400,30

        self.x,self.y = self.xsi,self.ysi
    def draw(self):
        self.image.draw(self.x,self.y)

    def get_bb(self):
        return self.x - self.xsi, self.y - self.ysi, self.x + self.xsi, self.y + self.ysi

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
