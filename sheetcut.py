# methods for cutting images out of a spritesheet

# IMPORTS
import pygame as pg

class spritesheet():

    def __init__(self):
        self.filename = ""
        self.fullimage = None
        self.photobook = []
        self.height = None
        self.width = None
        self.rows = None
        self.images_in_row = None
        self.b_top = None
        self.b_left = None
        self.b_hor_gap = None
        self.b_vert_gap = None
        self.length = None

    def set_filename(self, file):
        # this should be in a try ... except block
        self.filename = file
        #
        self.fullimage = pg.image.load(self.filename)

    def set_parameters(self,wide,high,numb_in_row=1,numb_rows=1,left_border=0,top_border=0,hor_gap=0,vert_gap=0):
        self.width = wide
        self.height = high
        self.images_in_row = numb_in_row
        self.rows = numb_rows
        self.b_left = left_border
        self.b_top = top_border
        self.b_hor_gap = hor_gap
        self.b_vert_gap = vert_gap

    def slice(self):
        for j in range(self.rows):
            for i in range(self.images_in_row):
                starty = self.b_top + j * (self.height + self.b_vert_gap)
                startx = self.b_left + i * (self.width + self.b_hor_gap)
                rect = pg.Rect(startx, starty, self.width, self.height)
                image = pg.Surface((self.width, self.height), pg.SRCALPHA).convert_alpha()
                image.blit(self.fullimage, (0, 0), rect)
                self.photobook.append(image)
        self.length = len(self.photobook)

    def show_sprite(self,instance):
        return self.photobook[instance]


