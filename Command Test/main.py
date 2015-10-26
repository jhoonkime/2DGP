from imaplib import Flags
import sys
sys.path.append('../LabsAll/Labs')

import random

from pico2d import *

import time

MAP_ON = 0

running = None
grass = None

LEFT,DOWN,RIGHT,UP = False,False,False,False

ATT_PUNCH = False


xSize,ySize = 1024,480
Speed = 0.5

D1,D2,D3,D4,D5,D6,D7,D8,D9 = 1,2,3,4,5,6,7,8,9
WKDVNDQKFTK ,PUNCH= 10,11
ATT_KICK,KICK = 12,13





class BackGround:
    def __init__(self):
        self.i = 0
        self.x,self.y = 0,0
        self.image = load_image('map/map (%d).png' % self.i)

    def draw(self):
        self.image.clip_draw_to_origin(0,0,xSize,ySize,self.x , self.y,xSize,ySize)
        pass
    def update(self):
        self.i+=Speed
        if(self.i > 14):
            self.i = 0

        self.image = load_image('map/map (%d).png' % self.i)
        # self.image.draw(200, 30)


class WKDVND:
    global WKDVNDQKFTK,D5

    def __init__(self):
        self.i = 285
        self.x,self.y = grass.x,grass.y
        self.state = 2
        # for self.i in range(1,100):
        # self.image = load_image("Iori Yagami/Iori Yagami_%d.png" % self.i)
    def draw(self):
        self.image.draw(self.x , self.y)
        pass
    def update(self):
        self.i+=Speed
        if(self.state == 1):
            self.x = grass.x
        self.x-=5
        if(self.x<0):
            self.x = 700
            self.state = 1
        if self.i >290:
            self.i = 285
            self.state = 2
        self.image = load_image("Iori Yagami/Iori Yagami_%d.png" % self.i)
        # self.image.draw(200, 30)


class U_D_L_R:

    global LEFT,DOWN,RIGHT,UP
    global PUNCH,KICK

    def __init__(self):
        self.x, self.y = 50,ySize-50

        self.image = load_image('resource/LEFT.png')
        self.i = 0


    def draw(self):
            self.image.draw(self.x, self.y )

    def update(self):

        if( LEFT == True):
            self.i += Speed
            self.image = load_image('resource/LEFT.png')
        elif( DOWN == True):
            self.i += Speed
            self.image = load_image('resource/DOWN.png')
        elif( RIGHT == True):
            self.i += Speed
            self.image = load_image('resource/RIGHT.png')
        elif( UP == True):
            self.i += Speed
            self.image = load_image('resource/UP.png')
        elif( PUNCH == True):
            self.image = load_image('resource/PUNCH.png')
        elif( KICK == True):
            self.image = load_image('resource/KICK.png')

        else:
            pass




#오스왈드
class OsWald:
    global LEFT,DOWN,RIGHT,UP
    global ATT_PUNCH,PUNCH
    global ATT_KICK,KICK

    def __init__(self):
        self.i = 0
        self.state = D5
        self.x,self.y = 200,100
        self.gravity = 5
        self.jump = 0
        self.skill = 0
        self.start = 0
        self.end = 0
        self.motion = 0

    def draw(self):
        self.image.draw(self.x , self.y)
        pass
    def update(self):

        self.i += Speed
        if(self.i> 700):
            self.i = 0
        self.image = load_image("Oswald/Oswald_%d.png" % self.i)
        # self.image.draw(200, 30)
        pass


#이오리
class Grass:
    global LEFT,DOWN,RIGHT,UP
    global ATT_PUNCH,PUNCH
    global ATT_KICK,KICK

    def __init__(self):
        self.i = 0
        self.state = D5
        self.x,self.y = 700,100
        self.gravity = 5
        self.jump = 0
        self.skill = 0
        self.start = 0
        self.end = 0
        self.motion = 0

    def draw(self):
        self.image.draw(self.x , self.y)
        pass
    def update(self):
        #0~8 제자리
        if(self.state == D5):
            self.motion = 0

            if(self.i > 8):
                self.i = 0
                self.jump = 0

        #12~15 걷기
        if((LEFT or RIGHT == True) and self.jump ==0 ):
            self.state = D4
            # 또는 D6
            self.jump = 0
        elif((LEFT or RIGHT == False) and self.jump ==0):
            self.state = D5
            self.jump = 0

        #29~33 점프
        if(UP == True and (LEFT == True)):
            self.state = D7
            self.jump = 1
        elif(UP == True and (RIGHT == True)):
            self.state = D9
            self.jump = 1

        elif(UP == True):
            self.state = D8
            self.jump = 1

        if (ATT_PUNCH == True):
            self.state = PUNCH
        if(ATT_KICK == True):
            self.state = KICK

        #앉기
        if( DOWN == True):
            self.start = time.time()
            self.state = D2
            self.skill = 1
            if (LEFT == True)and self.skill ==1 :

                self.state = WKDVNDQKFTK
                # if (self.state == PUNCH):
                #     # self.end = time.time() - self.start
                #     # if(self.end < 0.2):
                #     self.state = WKDVNDQKFTK


        elif(DOWN==True ) and LEFT ==True:
            self.state = D1
        elif (DOWN == True)and RIGHT == True:
            self.state = D3



        #############################################################
        if(self.state == PUNCH):
            if(self.i < 117):
                self.i = 117
            elif(self.i >= 119):
                self.state = D5
        #177~ 183
        if(self.state == KICK):
            if(self.i < 177):
                self.i = 177
            elif(self.i >= 183):
                self.state = D5

        if(self.state == WKDVNDQKFTK):

            if(self.i < 267):
                self.i = 267
            elif(self.i >= 274):
                self.state = D5
                self.skill = 0






        if(self.state == D4):

            if(self.i < 9):
                self.i = 9
            if(LEFT==1):
                self.x-=5
            elif(RIGHT ==1):
                self.x +=5
            if(self.i > 18):
                self.i = 9

        #점프
        if(self.state ==D7 ):
            if(self.i < 29):
                self.i = 29
            elif(self.i > 29 and self.i < 33):
                self.y+= self.gravity
                self.x -= 5
            elif(self.i >= 33):
                self.i = 33
                self.y -= self.gravity
                self.x -= 5
                if(self.y <=100):
                    self.state = D5
                    self.jump = 0


        elif(self.state ==D9 ):
            if(self.i < 29):
                self.i = 29
            elif(self.i > 29 and self.i < 33):
                self.y+= self.gravity
                self.x += 5
            elif(self.i >= 33):
                self.i = 33
                self.y -= self.gravity
                self.x += 5
                if(self.y <=100):
                    self.state = D5
                    self.jump = 0

        elif(self.state ==D8 ):
            if(self.i < 29):
                self.i = 29
            elif(self.i > 29 and self.i < 33):
                self.y+= self.gravity
            elif(self.i >= 33):
                self.i = 33
                self.y -= self.gravity
                if(self.y <=100):
                    self.state = D5
                    self.jump = 0

        #34~41 앉기
        if(self.state ==D2 ):
            if(self.i < 29):
                self.i = 29

            elif(self.i >= 33):
                self.i = 33


        #54~61 뛰기


        self.i += Speed
        self.image = load_image("Iori Yagami/Iori Yagami_%d.png" % self.i)
        # self.image.draw(200, 30)
        pass


class Boy:
    image = None
    LEFT_RUN , RIGHT_RUN = 0,1
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame = random.randint(0,7)
        self.dir = 1
        self.state = self.RIGHT_RUN
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')

    def update(self):
        if self.state == self.RIGHT_RUN:
            self.frame = (self.frame + 1 ) % 8
            self.x += (self.dir * 15)
        elif self.state == self.LEFT_RUN:
            self.frame = (self.frame + 1 ) % 8
            self.x += (self.dir * 15)

        if self.x > 800:
            self.dir = -1
            self.x = 800
            self.state = self.LEFT_RUN
        elif self.x < 0:
            self.dir = 1
            self.x = 0
            self.state = self.RIGHT_RUN

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)


def handle_events():
    global running
    global LEFT,DOWN,RIGHT,UP
    global ATT_PUNCH
    global ATT_KICK
    global MAP_ON

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

            elif event.key == SDLK_LEFT:
                LEFT =True
            elif event.key == SDLK_RIGHT:
                RIGHT = True
            elif event.key == SDLK_UP:
                UP = True
            elif event.key == SDLK_DOWN:
                DOWN = True
            elif event.key == SDLK_a:
                ATT_PUNCH = True
            elif event.key == SDLK_s:
                ATT_KICK = True
            elif event.key == SDLK_F1:
                MAP_ON =(MAP_ON + 1) %2


        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                LEFT = False
            elif event.key == SDLK_RIGHT:
                RIGHT = False
            elif event.key == SDLK_UP:
                UP = False
            elif event.key == SDLK_DOWN:
                DOWN = False
            elif event.key == SDLK_a:
                ATT_PUNCH = False
            elif event.key == SDLK_s:
                ATT_KICK = False
            elif event.key == SDLK_F1:
                pass



def main():

    global grass
    open_canvas(xSize,ySize)
    #boy = Boy()
    grass = Grass()
    oswald = OsWald()
    wkdvnd = WKDVND()
    udlr = U_D_L_R()
    background = BackGround()
    global running
    running = True

    while running:
        handle_events()

        grass.update()
        oswald.update()
        #boy.update()
        wkdvnd.update()
        udlr.update()

        background.update()
        clear_canvas()
        if(MAP_ON == 1):
            background.draw()
        grass.draw()
        #boy.draw()
        oswald.draw()
        udlr.draw()
        wkdvnd.draw()

        update_canvas()

        delay(1/60)

    close_canvas()


if __name__ == '__main__':
    main()