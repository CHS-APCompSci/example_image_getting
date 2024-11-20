import pygame as pg
from pygame.math import clamp

import constants as k


class m_sprite(pg.sprite.Sprite):
    images = []
    speed = k.hero_speed


    def __init__(self,photobook):
        for i in photobook:
            self.images.append(i)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=k.SCREENRECT.midbottom)
        self.origtop = self.rect.top
        self.facing = -1

    def move(self,direction):
        if direction:
            self.facing = direction
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(k.m_screen)
        if direction < 0:
            self.image