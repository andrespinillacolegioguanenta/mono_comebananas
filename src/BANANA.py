import pygame
import random
from settings import RUTA_IMAGEN_BANANA, VELOCIDAD_BANANA


class Banana:
    def __init__(self):
        self.imagen = pygame.image.load(RUTA_IMAGEN_BANANA)
        self.rect = self.imagen.get_rect()
        self.rect.x = random.randint(20, 760)
        self.rect.y = -50
        self.velocidad = VELOCIDAD_BANANA

    def actualizar(self):
        self.rect.y += self.velocidad

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.rect)

    def cayo(self):
        return self.rect.top > 600

    def agarrada(self, mono_rect):
        return self.rect.colliderect(mono_rect)
