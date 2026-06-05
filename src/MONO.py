import pygame
from settings import RUTA_IMAGEN_MONO, VELOCIDAD_MONO


class Mono:
    def __init__(self):
        self.imagen = pygame.image.load(RUTA_IMAGEN_MONO)
        self.rect = self.imagen.get_rect()
        self.rect.midbottom = (400, 560)
        self.velocidad = VELOCIDAD_MONO

    def actualizar(self, direccion):
        if direccion == -1:
            self.rect.x -= self.velocidad
        elif direccion == 1:
            self.rect.x += self.velocidad

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.rect)