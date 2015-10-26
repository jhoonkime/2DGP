__author__ = 'kimpc'

from pico2d import *

import random


class RYU:
    image = None

    LEFT,DOWN,RIGHT,UP = 0, 1, 2, 3
    IDLE,HADOKEN,SHORUKEN = 0,1,2

    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.state = self.IDLE
        self.idle_frames =0

        if self.image == None:
            self.image = load_image('animation_sheet.png')

    def State_Idle(self):
        self.state = self.IDLE

        #self.idle_frames += 1* Select
        pass
        #if self.x < 0:
        #    self.state = self.RIGHT_RUN
        #    self.x = 0
        #if self.run_frames == 100:
        #    self.state = self.LEFT_STAND
        #    self.stand_frames = 0
        pass
    def State_Hadoken(self):
        self.idle_frames += 1
        self.state =self.HADOKEN
        self.y += 10
        if self.idle_frames >=5:
            self.state = self.IDLE

    def State_Shoruken(self):
        self.idle_frames += 1

        self.state =self.SHORUKEN
        self.y -= 10
        if self.idle_frames >=5:
            self.state = self.IDLE



    handle_state = {
            IDLE: State_Idle,
            HADOKEN: State_Hadoken,
            SHORUKEN: State_Shoruken,
    }

    def update(self):
        self.frame = (self.frame+1 ) % 8
        self.handle_state[self.state](self)

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

