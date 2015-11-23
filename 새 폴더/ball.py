import random

from pico2d import *

class Ball:

    image = None;

    def __init__(self):
        self.x, self.y = random.randint(200, 790), 60
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class BigBall(Ball):
    image = None
    def __init__(self):
        self.x, self.y = random.randint(100,700), 500
        self.fall_speed = random.randint(50,120)
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')

    # fill here
    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        self.y -= frame_time*self.fall_speed
    def stop(self):
        self.fall_speed = 0
        self.y = 500
        if self.y is 500:
            self.x = random.randint(100,700)
            self.fall_speed = random.randint(50,120)
