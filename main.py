import pygame as pg


pg.init()
myscreen = pg.display.set_mode((400,400))
myscreen.fill("blue")
clock = pg.time.Clock()

# * * * * * * * * * * * * * * * * * * * *

background = pg.image.load("vapor_cloud 2.png")
photobook = []
width = 128
high = 128
for j in range (5):
    for i in range (5):
        starty = 0 + j*high
        startx = 0 + i*width
        rect = pg.Rect(startx,starty,width,high)
        image = pg.Surface((width,high),pg.SRCALPHA).convert_alpha()
        image.blit(background,(0,0),rect)
        photobook.append(image)

# * * * * * * * * * * * * * * * * * * * *

running = True

# ANIMATE
currentimage = 0
reversedirection = True
def animate():
    global currentimage,reversedirection

    # show the current image here, then update
    if currentimage == 24 or currentimage == 0:
        reversedirection = not reversedirection
    if reversedirection:
        plusvalue = -1
    else:
        plusvalue = 1

    currentimage = currentimage + plusvalue
    myscreen.blit(photobook[currentimage], (100, 100))
    pg.display.update()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    myscreen.fill("blue")
    animate()
    # myscreen.blit(m_bubble.get_sprite(0),(200,200))
    pg.display.flip()
    dt = clock.tick(10)


# LOOP ENDED
pg.quit()