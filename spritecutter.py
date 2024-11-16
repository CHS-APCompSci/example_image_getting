from select import select

import pygame as pg

class imagecutter:

    def __init__(self,filename,width,height,numb_sprites_per_row=1, numb_rows_sprites=1,
                 left_border=0,top_border=0,hoz_gap=0, vert_gap=0):
        # VARIABLES
        self.i_name = filename
        self.photobook = []
        self.i_width = width
        self.i_height = height
        self.i_left_border = left_border
        self.i_top_border = top_border
        self.i_vert_gap = vert_gap
        self.i_hoz_gap = hoz_gap
        self.i_rows = numb_rows_sprites
        self.i_images_per_row = numb_sprites_per_row
        self.i_image = pg.image.load(self.i_name)

    def cut(self):
        for j in range(self.i_rows):
            for i in range(self.i_images_per_row):
                starty = self.i_top_border + j * (self.i_height + self.i_vert_gap)
                startx = self.i_left_border + i * (self.i_width + self.i_hoz_gap)
                rect  = pg.Rect(startx,starty,self.i_width,self.i_height)
                image = pg.Surface((self.i_width, self.i_height), pg.SRCALPHA).convert_alpha()
                image.blit(self.i_image, (0, 0), rect)
                self.photobook.append(image)

