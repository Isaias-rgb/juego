import sys
import pygame as pg
import bolita
import jugador

ancho = 640
alto = 480
color_fondo = (0,0,0)

#tamaño de la ventana
pantalla = pg.display.set_mode((ancho,alto))

#Crea el reloj
reloj = pg.time.Clock()

#titulo del la panatalla
pg.display.set_caption('Juego de ladrillos')

#Crea la bolita
bolita = bolita.Bolita(ancho,alto)
jugador = jugador.Jugador(ancho,alto)

#Ajustar repeticion de evento de teclapresionada
pg.key.set_repeat(30)

while True:
    #Establece los FPS
    reloj.tick(60)
    #Revisa todos los eventos que acurren
    for eveto in pg.event.get():
        if eveto.type == pg.QUIT:
            #cierra el juego
            sys.exit()  
        #eventos para mover la pañeta 
        elif eveto.type == pg.KEYDOWN:
            jugador.update(eveto)
    
    #Actualiza la posicion de la bolita 
    bolita.update()  
    #Rellenamos la pantalla
    pantalla.fill(color_fondo)           
    #dibuja la bolita en la pantalla
    pantalla.blit(bolita.image,bolita.rect)
    #Dibuja paleta
    pantalla.blit(jugador.image,jugador.rect) 
    #Actualiza los objetos en la pantalla
    pg.display.flip()

    