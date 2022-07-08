import sys
import pygame as pg
import bolita
import jugador
import nivel1

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
muro= nivel1.Muro (cantidad_ladrillos=112,ancho=ancho) 
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
    
    #Colision entre bola y paleta
    if pg.sprite.collide_rect(bolita,jugador):
        bolita.speed[1] = -bolita.speed[1]   
    #Colisicion de la pelota con ladrillos
    lista = pg.sprite.spritecollide(bolita, muro, False)
    if lista:
        ladrillo = lista[0]
        cx = bolita.rect.centerx #obtiene la pos en x
        if cx < ladrillo.rect.left or cx > ladrillo.rect.right:
            bolita.speed[0] = -bolita.speed[0]
        else:
            bolita.speed[1] = -bolita.speed[1]
        muro.remove(ladrillo)
                
    #Rellenamos la pantalla
    pantalla.fill(color_fondo)           
    
    #dibuja la bolita en la pantalla
    pantalla.blit(bolita.image,bolita.rect)
    
    #Dibuja paleta
    pantalla.blit(jugador.image,jugador.rect)
    
    #Dibuja el muro
    muro.draw(pantalla) 
    
    #Actualiza los objetos en la pantalla
    pg.display.flip()

    