import random
import time

from pico2d import *

start = None

class Boy:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None

    PUNCH,KICK = 10,11
    D1,D2,D3,D4,D5,D6,D7,D8,D9 = 1,2,3,4,5,6,7,8,9
    WAVE = 12

    def __init__(self):
        self.x, self.y = 400, 100
        self.frame = random.randint(0, 7)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0
        self.ydir = 0
        self.state = self.D5
        self.framecount = 0
        self.gravity = 5
        self.jump = 0
        self.d_time,  self.l_time,  self.r_time,  self.u_time, self.p_time, self.k_time = 0,0,0,0,0,0
        self.skillstate = 0
        self.skilltime = 0
        self.frameasd = 0


    def handle_idle(self,frame_time):
        global D1,D2,D3,D4,D5,D6,D7,D8,D9
        global PUNCH,KICK
        distance = Boy.RUN_SPEED_PPS * frame_time
        #if(self.state == self.D5):
        self.dir = 0
        self.ydir = 0
        if(self.frame > 8):
                self.frame ,self.jump = 0,0

    def handle_punch(self,frame_time):
        global PUNCH,KICK
        global D1,D2,D3,D4,D5,D6,D7,D8,D9
        distance = Boy.RUN_SPEED_PPS * frame_time
        #if(self.state == self.PUNCH):
        if(self.frame < 117):
                 self.frame = 117
        if(self.frame >= 122):
                self.state = self.D5
        #177~ 183
    def handle_kick(self,frame_time):
        global PUNCH,KICK
        global D1,D2,D3,D4,D5,D6,D7,D8,D9
        distance = Boy.RUN_SPEED_PPS * frame_time
        #if(self.state == self.KICK):
        if(self.frame < 177):
                self.frame = 177
        if(self.frame >= 183):
                self.state = self.D5

    def handle_left_right(self,frame_time):
        global PUNCH,KICK
        global D1,D2,D3,D4,D5,D6,D7,D8,D9
        distance = Boy.RUN_SPEED_PPS * frame_time

        #if(self.state == self.D4 or self.state == self.D6):
        if(self.frame < 9):
                self.frame = 9
        if(self.D4==1):
                    self.dir = -1
        if(self.D6 ==1):
                    self.dir = +1
        if(self.frame > 18):
                    self.frame = 9

        self.x +=(self.dir * distance)

        #점프
    def handle_jump(self,frame_time):
        global PUNCH,KICK
        global D1,D2,D3,D4,D5,D6,D7,D8,D9
        distance = Boy.RUN_SPEED_PPS * frame_time

        #if(self.state ==self.D8 ):
        if(self.frame < 29):
                    self.frame = 29
        if(self.frame > 29 and self.frame < 33):
                    self.ydir = 1
        if(self.frame >= 33):
            self.frame = 33
            self.ydir = -1
            if(self.y <=100):
                self.state = self.D5
                self.jump = 0
                self.up = False
        self.y += (self.ydir * distance)

    def handle_wave(self,frame_time):
        pass

        #34~41 앉기
    def handle_down(self,frame_time):
        global D1,D2,D3,D4,D5,D6,D7,D8,D9
        global PUNCH,KICK

        #if(self.state ==self.D2 ):
        if(self.frame < 35):
                self.frame = 35
        if(self.frame >= 41):
                self.frame = 41

    handle_state = {
        D2 : handle_down,
        D5 : handle_idle,
        PUNCH : handle_punch,
        KICK : handle_kick,
        D8 : handle_jump,
        D4: handle_left_right,
        D6: handle_left_right,
        WAVE: handle_wave
    }


    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        self.total_frames += Boy.FRAMES_PER_ACTION * Boy.ACTION_PER_TIME * frame_time
        self.frame += 0.1
        self.framecount += 1
        self.x = clamp(0, self.x, 800)
        self.handle_state[self.state](self,frame_time)

        if(self.state == self.WAVE):
            print("%d" % self.state)

        if (self.D2 ==True) and (self.D6 == True) and (self.PUNCH == True)and \
                (self.r_time > self.d_time -30)and(self.p_time > self.r_time-30):
            self.state = self.WAVE
            if (self.state == self.WAVE):
                self.frameasd+=1
                self.frame+=0.5
            if self.frame<267:
                    self.frame = 267
            if(self.frame >= 274):
                    self.state = self.D5

            if(self.frameasd>274):
                self.frameasd =0
                self.framecount = 0
                self.state = self.D5
                self.down, self.right,self.punch = False,False,False

        #다른기술?
        # if (self.D2 ==True) and (self.D6 == True) and (self.PUNCH == True)and \
        #         (self.framecount > self.d_time-30)and(self.r_time > self.d_time -30)and(self.p_time > self.r_time-30):
        #     self.skillstate = 2
        #     if (self.skillstate == 2):
        #         # self.x -=10
        #         self.frameasd+=1
        #         self.frame+=0.5
        #         if self.frame<267:
        #             self.frame = 267
        #         if(self.frame >= 274):
        #             self.state = self.D5
        #
        #         if(self.frameasd>10):
        #             self.skillstate = 0
        #             self.frameasd =0
        #             self.framecount = 0
        #             self.state = self.D5
        #             self.down, self.right,self.punch = False,False,False


        self.image = load_image('resource\iori Yagami\iori Yagami_%d.png' % self.frame)

    def draw(self):
        self.image.draw(self.x ,self.y)
        #self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_DOWN:
                self.state = self.D2
                self.d_time = self.framecount
                #print ("down_time : %d" % self.d_time)
            if event.key == SDLK_UP:
                self.state = self.D8
                self.jump = 1
                self.u_time = self.framecount
                #print ("up_time : %d" % self.u_time)
            if event.key == SDLK_LEFT:
                self.state = self.D4
                # 또는 D6
                self.jump = 0
                self.dir = -1
                self.l_time = self.framecount
                #print ("left_time : %d" % self.l_time)
            if event.key == SDLK_RIGHT:
                self.state = self.D6
                self.dir = +1
                self.r_time = self.framecount
                #print ("right_time : %d" % self.r_time)
            if event.key == SDLK_a:
                self.state = self.PUNCH
                self.jump = 0
                self.p_time = self.framecount
                #print ("p_time : %d" % self.p_time)
            if event.key == SDLK_s:
                self.state = self.KICK
                self.jump = 0
                self.k_time = self.framecount
                #print ("kick_time : %d" % self.k_time)
        # if event.type == SDL_KEYUP:
        #     if event.key == SDLK_DOWN:
        #         self.state = self.D2
        #         self.d_time = self.framecount
        #         #print ("down_time : %d" % self.d_time)
        #     if event.key == SDLK_UP:
        #         self.state = self.D8
        #         self.jump = 1
        #         self.u_time = self.framecount
        #         #print ("up_time : %d" % self.u_time)
        #     if event.key == SDLK_LEFT:
        #         self.state = self.D4
        #         # 또는 D6
        #         self.jump = 0
        #         self.dir = -1
        #         self.l_time = self.framecount
        #         #print ("left_time : %d" % self.l_time)
        #     if event.key == SDLK_RIGHT:
        #         self.state = self.D6
        #         self.dir = +1
        #         self.r_time = self.framecount
        #         #print ("right_time : %d" % self.r_time)
        #     if event.key == SDLK_a:
        #         self.state = self.PUNCH
        #         self.jump = 0
        #         self.p_time = self.framecount
        #         #print ("p_time : %d" % self.p_time)
        #     if event.key == SDLK_s:
        #         self.state = self.KICK
        #         self.jump = 0
        #         self.k_time = self.framecount
        #         #print ("kick_time : %d" % self.k_time)


#
# #12~15 걷기
#         if((self.left or self.right == True)): # and self.jump ==0 ):
#             self.state = self.D4
#             # 또는 D6
#             self.jump = 0
#         #29~33 점프
#         if(self.up == True and (self.left == True)):
#             self.state = self.D7
#             self.jump = 1
#         if(self.up == True and (self.right == True)):
#             self.state = self.D9
#             self.jump = 1
#         if(self.up == True):
#             self.state = self.D8
#             self.jump = 1
#
#         if (self.punch == True):
#             self.state = self.PUNCH
#             self.jump = 0
#
#         if(self.kick == True):
#             self.state = self.KICK
#             self.jump = 0






