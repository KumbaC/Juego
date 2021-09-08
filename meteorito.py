import pygame
import sys
from pygame import color 
from pygame.locals import *
#Importar clases
from clases import asteroides, jugador
from clases import Asteroide
from random import randint 
from time   import clock
#variables
Ancho = 480
Alto = 700
contador = 0
ListaAsteroides = []
puntuacion = 0
colorFuente = (255,255,255)
#Booleano 
jugando = True

#Funciones principales
#Carga asteroides 
def cargarAsteroides(x, y):
    meteoro = asteroides.Asteroide(x,y)
    ListaAsteroides.append(meteoro)
def gameOver():
    global jugando
    jugando = False 
    for meteoritos in ListaAsteroides:
        ListaAsteroides.remove(meteoritos)
def meteoritos():
    pygame.init()
    ventana = pygame.display.set_mode((Ancho, Alto))
    #Sonidos 
    pygame.mixer.music.load('sonidos/fondo.wav')
    pygame.mixer.music.play(3)
    sonidoColision = pygame.mixer.Sound('sonidos/colision.aiff')
    #Fuente de la Puntuacion 
    fuenteMarcador = pygame.font.SysFont('Impact', 47) 
    #Imagen de fondo 
    fondo = pygame.image.load('imagenes/fondo.png')
    
    
    #Titulo
    pygame.display.set_caption('Asteroides')
    #Crear objeto
    nave = jugador.Nave()
    contador = 0
    #Ciclo de juego 
    while True: 
       ventana.blit(fondo,(0,0))
       nave.dibujar(ventana)
       #Tiempo
       tiempo = clock()
       
       #Puntuacion
       global puntuacion
       textMarcador = fuenteMarcador.render('Puntos: '+ str(puntuacion),0,colorFuente)
       ventana.blit(textMarcador, (0,0))
       #Creamos asteroides
       if tiempo - contador > 1:
           contador = tiempo 
           posX = randint(2, 490)
           cargarAsteroides(posX, 0)
        
        #Comprobamos lista Asteroides 
       if len(ListaAsteroides) > 0:
            for x in ListaAsteroides:
                if jugando == True:
                   x.dibujar(ventana)
                   x.recorrido()
                if x.rect.top > 700:
                    ListaAsteroides.remove(x)
                else:
                    if x.rect.colliderect(nave.rect): 
                        ListaAsteroides.remove(x)
                        sonidoColision.play()
                        nave.vida = False
                        gameOver() 
       #disparo
       if len(nave.listaDisparo) > 0:
            for x in nave.listaDisparo:
                x.dibujar(ventana)
                x.recorrido()
                if x.rect.top < -10:
                    nave.listaDisparo.remove(x)
                else: 
                    for meteoritos in ListaAsteroides: 
                        if x.rect.colliderect(meteoritos.rect):
                            ListaAsteroides.remove(meteoritos)
                            nave.listaDisparo.remove(x)
                            puntuacion += 1
                            #print("Colision nave disparo")
       nave.mover()
       
    
       for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if jugando == True:
                if evento.key == K_LEFT:
                   nave.rect.left-=nave.velocidad
                elif evento.key == K_RIGHT:
                   nave.rect.right+=nave.velocidad
                elif evento.key == K_SPACE:
                  x, y = nave.rect.center
                  nave.disparar(x, y)
        if jugando == False: 
            FuenteGameOver = pygame.font.SysFont('Impact', 105)
            textoGameOver = FuenteGameOver.render('Game Over', 0, colorFuente)
            ventana.blit(textoGameOver,(40,350))
            pygame.mixer.music.fadeout(5000)
       pygame.display.update( )

#Llamar a la funciones 
meteoritos()