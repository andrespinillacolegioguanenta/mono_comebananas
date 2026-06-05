import pygame
from settings import RUTA_SONIDO_GANA, RUTA_SONIDO_PERDEDOR


class AudioJuego:
    def __init__(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        self.sonido_banana = pygame.mixer.Sound(RUTA_SONIDO_GANA)
        self.sonido_perdio = pygame.mixer.Sound(RUTA_SONIDO_PERDEDOR)

    def reproducir_mono(self):
        self.sonido_mono.play()

    def reproducir_banana_aparece(self):
        self.sonido_banana.play()

    def reproducir_banana_coja(self):
        self.sonido_banana.play()

    def reproducir_perdio(self):
        self.sonido_perdio.play()