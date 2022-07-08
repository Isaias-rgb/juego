import pygame as pg
from soupsieve import select
class Ladrillo(pg.sprite.Sprite):
    def __init__(self,posicion) -> None:
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('imagenes/ladrillo.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion

class Muro(pg.sprite.Group):
    def __init__(self,cantidad_ladrillos,ancho) -> None:
        pg.sprite.Group.__init__(self)

        pos_x = 0
        pos_y = 30
        for i in range(cantidad_ladrillos):
            ladrillo = Ladrillo((pos_x,pos_y))
            self.add(ladrillo)

            pos_x += ladrillo.rect.width         

            if pos_x >= ancho:
                pos_x = 0
                pos_y += ladrillo.rect.height