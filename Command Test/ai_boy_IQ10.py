import sys
from Move import RYU

sys.path.append('../LabsAll/Labs')

import random

from pico2d import *
from Move import *

running = None
Select = 1

class asd:
    global Select
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        if Select == 1:
            self.image.draw(400, 300)
        elif Select ==0:
            self.image.draw(400, 30)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



def handle_events():
    global running,Select

    global IDLE,HADOKEN,SHORUKEN
    global LEFT,DOWN,RIGHT,UP

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

            if event.type == SDL_KEYDOWN:
                if event.key== SDLK_UP:
                    LEFT
                elif event.key== SDLK_DOWN:
                    RYU.state = SHORUKEN
                elif event.key == SDLK_LEFT:
                    RYU.state = IDLE




def main():

    open_canvas()

    boy = RYU()
    asdf = asd()
    grass = Grass()

    global running
    running = True

    while running:
        handle_events()

        boy.update()

        clear_canvas()
        grass.draw()
        asdf.draw()
        boy.draw()
        update_canvas()

        delay(0.04)

    close_canvas()


if __name__ == '__main__':
    main()