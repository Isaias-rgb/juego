import os
import pygame as pg

class Jugador(pg.sprite.Sprite):
    def __init__(self,ancho,alto) -> None:
        self.ancho = ancho
        self.alto = alto
        self.image = pg.image.load('imagenes/paleta.png')
        self.rect = self.image.get_rect()
        self.rect.center = (ancho/2,alto-20)
        self.speed = [0,0]

    def update(self,evevto):
        self.rect.move_ip(self.speed)
        if evevto.key == pg.K_LEFT and self.rect.left > 0:
            self.speed = [-5,0]
        elif evevto.key == pg.K_RIGHT and self.rect.right < self.ancho:
            self.speed = [5,0]
        else :
            self.speed = [0,0]    