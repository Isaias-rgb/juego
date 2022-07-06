from curses.ascii import alt
from pickle import TRUE
import sys
import pygame as pg

ancho = 640
alto = 480
pantalla = pg.display.set_mode((ancho,alto))

while TRUE:
    for eveto in pg.event.get():
        if eveto.type == pg.QUIT:
            sys.exit
    pg.display.flip()