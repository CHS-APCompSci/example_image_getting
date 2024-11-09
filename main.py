# IMPORTS
import pygame as pg
import sheetcut
import pygame_widgets as widget
from pygame_widgets.button import Button
import constants as k



# INITIALIZE
pg.init()
myscreen = pg.display.set_mode(k.SCREENRECT.size)
myscreen.fill("blue")
# create a clock for timing of screen flips
clock = pg.time.Clock()
# for framerate
framerate = 15

# * * * * * * * * * * * * * * * * * * * *
# let's move these into their own file for
# future use

#background = pg.image.load("vapor_cloud 2.png")
#photobook = []
#width = 128
#high = 128
#for j in range (5):
#    for i in range (5):
#        starty = 0 + j*high
#        startx = 0 + i*width
#        rect = pg.Rect(startx,starty,width,high)
#        image = pg.Surface((width,high),pg.SRCALPHA).convert_alpha()
#        image.blit(background,(0,0),rect)
#        photobook.append(image)
#
# * * * * * * * * * * * * * * * * * * * *

# CLASS INSTANCES
vapors = sheetcut.spritesheet()
vapors.set_filename("vapor_cloud 2.png")
vapors.set_parameters(128, 128, 5, 5)
vapors.slice()

pacman = sheetcut.spritesheet()
pacman.set_filename("ghosts copy.svg")
pacman.set_parameters(130,130,6,4,5,5,0,0)
pacman.slice()

# COMMANDS
def my_quit():
    global running
    running = False

def switchsheet():
    global pacman,vapors,current_sprites,framerate
    if current_sprites==pacman:
        current_sprites = vapors
        framerate = 10
    else:
        current_sprites = pacman
        framerate = 4

# BUTTONS
my_quit = (Button(myscreen,k.QUITBUTTONRECT.x,k.QUITBUTTONRECT.y,k.QUITBUTTONRECT.width,k.QUITBUTTONRECT.height,
                 text="Quit", radius = 5, onClick=my_quit))

my_switch = (Button(myscreen,k.SWITCHBUTTONRECT.x,k.SWITCHBUTTONRECT.y,k.SWITCHBUTTONRECT.width,k.SWITCHBUTTONRECT.height,
                 text="Switch", radius = 5, onClick=switchsheet))

# set our default current class
current_sprites = sheetcut.spritesheet()
current_sprites = vapors
running = True

# ANIMATE
currentimage = 0
reversedirection = True
def animate():
    global currentimage,reversedirection

    myscreen.blit(current_sprites.show_sprite(currentimage), (100, 100))

    if currentimage == (current_sprites.length - 1) or currentimage == 0:
        reversedirection = not reversedirection
    if reversedirection:
        plusvalue = -1
    else:
        plusvalue = 1

    currentimage = currentimage + plusvalue


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    myscreen.fill("blue")
    animate()
    widget.update(event)
    pg.display.flip()
    dt = clock.tick(framerate)


# LOOP ENDED
pg.quit()