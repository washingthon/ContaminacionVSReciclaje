import pygame
WHITE = [255, 255, 255]

class Enemigo:
    def __init__(self,screen, x, y, imagen):
        self.screen = screen 
        self.x = x
        self.y = y
        self.imagen = imagen
    #un comentario
    def drawEnemigo (self):
        self.imagen = pygame.transform.scale(self.imagen, (50, 50))
        self.imagen.set_colorkey(WHITE)
        self.screen.blit(self.imagen,(self.x, self.y))