import pygame
class Asteroide(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.imagenAsteroide = pygame.image.load('imagenes/asteoride1.png')
        self.rect = self.imagenAsteroide.get_rect()
        self.velocidad = 3
        self.rect.top = posY
        self.rect.left = posX
        self.ListaAsteroides = []

    def recorrido(self):
        self.rect.top = self.rect.top + self.velocidad
    def dibujar(self, superficie):
        superficie.blit(self.imagenAsteroide, self.rect)