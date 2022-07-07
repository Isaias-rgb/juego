import os
import sys
import pygame as pg



class Bolita(pg.sprite.Sprite):
    def __init__(self,ancho,alto) -> None:
        self.ancho = ancho
        self.alto = alto
        self.image = pg.image.load("imagenes/bolita.png")
        self.rect = self.image.get_rect()
        self.rect.center = (ancho/2,alto/2)
        #formas de posicionar una imagen
        #self.rect.bottom = alto/2
        #self.rect.centerx = ancho / 2
        #self.rect.centery = alto / 2 
        self.speed = [3,3]

    def update(self):
        self.rect.move_ip(self.speed)
        if self.rect.bottom >= self.alto or self.rect.top <= 0 :
            self.speed[1] = -self.speed[1]
        if self.rect.right >= self.ancho or self.rect.left <=0:
            self.speed[0] = -self.speed[0]    