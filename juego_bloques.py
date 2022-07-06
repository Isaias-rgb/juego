from curses.ascii import alt
from pickle import TRUE
import pygame as pg

ancho = 640
alto = 480
pantalla = pg.display.set_mode((ancho,alto))

while TRUE:
    pg.display.flip()