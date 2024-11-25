import pygame as pg
from spritecutter import imagecutter
import constants as k


pg.init()

myscreen = pg.display.set_mode(k.m_screen)
myscreen.fill("blue")
clock = pg.time.Clock()

vapors = imagecutter("vapor_cloud 2.png",128,128,
                     5,5)
vapors.cut()

ghosts = imagecutter("ghosts.svg",130,130,
                     6,4)
ghosts.cut()

hero = imagecutter("female_dark_yellow.png",48,48,
                   3,1,0,6*48)
hero.cut()

myanimatedsprites = hero

running = True
# ANIMATE
currentimage = 0
reversedirection = True
def animate():
    global currentimage,reversedirection

    # show the current image here, then update
    if currentimage == len(myanimatedsprites.photobook)-1 or currentimage == 0:
        reversedirection = not reversedirection
    if reversedirection:
        plusvalue = -1
    else:
        plusvalue = 1

    currentimage = currentimage + plusvalue
    myscreen.blit(pg.transform.scale(myanimatedsprites.photobook[currentimage],(200,200)),(100,100))
    #myscreen.blit(myanimatedsprites.photobook[currentimage], (100, 100))
    pg.display.update()



while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    # get any keys that are pressed
    keys = pg.key.get_pressed()
    # when D or A are pressed
    # set the direction of the hero
    direction = keys[pg.K_d] - keys[pg.K_a]


    myscreen.fill("blue")
    animate()
    pg.display.flip()
    dt = clock.tick(20) #test 3

# LOOP ENDED
pg.quit()